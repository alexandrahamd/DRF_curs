import datetime
import requests
from celery import shared_task, app
from django.conf import settings
from habits.models import Habit
from celery import Celery


@shared_task
def send_massage(habit_pk=1):

    habit = Habit.objects.get(pk=habit_pk)
    now = datetime.datetime.now()
    now_time = datetime.datetime.now().hour
    token = settings.TOKEN
    days = (now.replace(tzinfo=datetime.timezone.utc) - habit.last_send).days
    # если время на данный момент больше чем время рассылки в модели и прошло больше дней,
    # чем в периоде, указанном в модели
    if now_time > habit.time.hour and days > habit.period:
        print('123')
        url = f"https://api.telegram.org/bot{token}/getUpdates"
        try:
            req = requests.get(url).json()
            chat_id = (req['result'][1]['message']['chat']['id'])
            message = habit
            url = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={message}"
            # меняем дату последнего отправления
            habit.last_send = datetime.datetime.now()
            habit.save()
        except: ValueError
