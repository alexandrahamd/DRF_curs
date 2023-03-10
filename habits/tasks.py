import datetime
import requests
from config.celery import app
from django.conf import settings
from habits.models import Habit


@app.task
def send_telegram_massage():
    '''функция отправки сообщения в телеграмм'''

    obj_habits = Habit.objects.all()
    now = datetime.datetime.now()
    now_time = datetime.datetime.now().hour
    for item in obj_habits:
        days = (now.replace(tzinfo=datetime.timezone.utc) - item.last_send).days
        # если время на данный момент больше чем время рассылки в модели и прошло больше дней,
        # чем в периоде, указанном в модели
        if now_time > item.time.hour and days < item.period:
            text = str(item)
            token = settings.TOKEN
            chat_id = item.user.chat_id
            # chat_id = '@hamdaouialex'
            url_req = "https://api.telegram.org/bot" + token + "/sendMessage" + "?chat_id=" + chat_id + "&text=" + text
            # меняем дату последнего отправления
            item.last_send = datetime.datetime.now()
            results = requests.get(url_req)
            print(results.json())
