import datetime
import telebot
import requests
from django.core.management import BaseCommand
from user.models import User
from habits.models import Habit


class Command(BaseCommand):

    def handle(self, *args, **options):

        users = [
            {'email': '123@yandex.ru', 'chat_id': '@hamdaouialex'},
            {'email': '321@yandex.ru', 'chat_id': '@h'},
            {'email': '213@yandex.ru', 'chat_id': '@h'},
        ]

        users_list = []
        for item in users:
            users_list.append(User(**item))

        User.objects.bulk_create(users_list)

        habits = [
            {'user': User.objects.get(id=1), 'place': 'везде', 'time': '06:00',
             'action': "выпить стакан воды", 'is_pleasant_habit': True,
             "period": 1, 'lead_time': '120', 'is_public': True},
            {'user': User.objects.get(id=2), 'place': 'дома', 'time': '06:00',
             'action': "сделать зарядку", 'is_pleasant_habit': False,
             "period": 1, 'reward': 'похвалить себя, ты молодец', 'lead_time': '1120', 'is_public': True},
            {'user': User.objects.get(id=1), 'place': 'везде', 'time': '06:00',
             'action': "позавтракать", 'is_pleasant_habit': False,
             "period": 1, 'reward': 'състь конфету', 'lead_time': '1120', 'is_public': True}
        ]

        habits_list = []
        for item in habits:
            habits_list.append(Habit(**item))

        Habit.objects.bulk_create(habits_list)