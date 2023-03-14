import datetime

import requests
from django.conf import settings
from django.core.management import BaseCommand

from habits.models import Habit


class Command(BaseCommand):

    def handle(self, *args, **options):
        '''функция отправки сообщения в телеграмм'''

        # habit = Habit.objects.get(pk=1)
        # now = datetime.datetime.now()
        # now_time = datetime.datetime.now().hour
        # token = settings.TOKEN
        # days = (now.replace(tzinfo=datetime.timezone.utc) - habit.last_send).days
        # # если время на данный момент больше чем время рассылки в модели и прошло больше дней,
        # # чем в периоде, указанном в модели
        # print(now_time)
        # print(habit.time.hour)
        # print(days)
        # print(habit.period)
        # if now_time > habit.time.hour and days > habit.period:
        #     print('123')
        #     url = f"https://api.telegram.org/bot{token}/getUpdates"
        #     req = requests.get(url).json()
        #     chat_id = (req['result'][1]['message']['chat']['id'])
        #     message = habit
        #     url = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={message}"
        #     # меняем дату последнего отправления
        #     habit.last_send = datetime.datetime.now()
        #     habit.save()

        habit = Habit.objects.get(pk=1)
        now = datetime.datetime.now()
        now_time = datetime.datetime.now().hour
        token = settings.TOKEN
        days = (now.replace(tzinfo=datetime.timezone.utc) - habit.last_send).days
        # if now_time > habit.time.hour and days < habit.period:
        # получаем id_chat
        url = f"https://api.telegram.org/bot{token}/getUpdates"
        req = requests.get(url).json()
        chat_id = (req['result'][1]['message']['chat']['id'])
        message = habit
        url = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={message}"
        # меняем дату последнего отправления
        results = requests.get(url)
        print(results.json())
        habit.last_send = datetime.datetime.now()
        habit.save()
