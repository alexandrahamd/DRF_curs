import datetime
import requests
from config.celery import app
from django.conf import settings
from habits.models import Habit


@app.task
def send_telegram_massage(habit_pk=1):
    '''функция отправки сообщения в телеграмм'''

    habit = Habit.objects.get(pk=habit_pk)
    now = datetime.datetime.now()
    now_time = datetime.datetime.now().hour
    token = settings.TOKEN
    days = (now.replace(tzinfo=datetime.timezone.utc) - habit.last_send).days
    if now_time < habit.time.hour and days > habit.period:
        # получаем id_chat
        url = f"https://api.telegram.org/bot{token}/getUpdates"
        req = requests.get(url).json()
        chat_id = (req['result'][1]['message']['chat']['id'])
        message = habit
        url = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={message}"
        # меняем дату последнего отправления
        habit.last_send = datetime.datetime.now()
        habit.save()
