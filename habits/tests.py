from rest_framework.test import APITestCase
from habits.models import Habit
from user.models import User
from rest_framework import status


class HabitTestCase(APITestCase):

    def setUp(self) -> None:
        super().setUp()
        self.user = User.objects.create(
            email='zaqw12@yandex.ru',
        )
        self.user.set_password('zaq123')
        self.user.save()

        response = self.client.post(
            '/user/api/token/',
            {'email': 'zaqw12@yandex.ru', 'password': 'zaq123'}
        )

        self.access_token = response.json().get('access')
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')

    def test_habit_create(self):

        odj = User.objects.get(email='zaqw12@yandex.ru')
        self.user = odj

        context = {
            "place": "везде",
            "time": "06:00:00",
            "action": "выпить стакан воды",
            "is_pleasant_habit": True,
            "period": 1,
            "lead_time": 120,
            "is_public": False,
            "user": odj.id,
        }

        response = self.client.post('/habits/create/',
                                    context,
                                    format='json')

        self.assertEqual(response.status_code,
                         status.HTTP_201_CREATED)

    def test_habit_create_pleasant_habit(self):
        'проверка создания приятной привычки, к которой есть награда'

        odj = User.objects.get(email='zaqw12@yandex.ru')
        self.user = odj

        context = {
            "place": "везде",
            "time": "06:00:00",
            "action": "выпить стакан воды",
            "is_pleasant_habit": True,
            "reward": "похвалить себя, ты молодец",
            "period": 1,
            "lead_time": 120,
            "is_public": False,
            "user": odj.id,
        }

        response = self.client.post('/habits/create/',
                                    context,
                                    format='json')

        self.assertEqual(response.status_code,
                         status.HTTP_400_BAD_REQUEST)

    def test_habit_update(self):
        self.test_habit_create()

        odj = Habit.objects.get(action="выпить стакан воды")

        context = {
                "place": "везде",
                "time": "06:00:00",
                "action": "выпить стакан теплой воды!",
                "is_pleasant_habit": True,
                "period": 1,
                "lead_time": 120,
                "is_public": False,
                "user": self.user.id
        }

        response = self.client.put(
            f'/habits/update/{odj.id}/', context)

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )
        p = Habit.objects.get()
        self.assertEqual(p.action, 'выпить стакан теплой воды!')

    def test_habit_delete(self):
        self.test_habit_create()
        odj = Habit.objects.get(action='выпить стакан воды')

        response = self.client.delete(
            f'/habits/delete/{odj.id}/',
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )

    def test_habit_list(self):
        self.test_habit_create()

        response = self.client.get(
            '/habits/',
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_habit_my_list(self):
        self.test_habit_create()

        response = self.client.get(
            '/habits/my_habits/',
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )
