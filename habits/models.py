from django.conf import settings
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from rest_framework import serializers


# Create your models here.
class Habit(models.Model):

    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    place = models.CharField(max_length=150, null=True, blank=True, verbose_name='место')
    time = models.TimeField(blank=True, null=True, verbose_name='время')
    action = models.CharField(max_length=150, blank=True, null=True, verbose_name='действие')

    # привычка, которую можно привязать к выполнению полезной привычки
    is_pleasant_habit = models.BooleanField(default=False, null=True, blank=True,
                                            verbose_name='приятная привычка')

    # привычка, которая связана с другой привычкой, важно указывать для полезных привычек, но не для приятных
    associated_habit = models.ForeignKey('self', related_name='associated',
                                         on_delete=models.SET_NULL, null=True, blank=True,
                                         verbose_name='связанная привычка')

    # периодичность* (по умолчанию ежедневная) - периодичность выполнения привычки для напоминания в днях
    period = models.IntegerField(verbose_name='период', null=True, blank=True,
                                 validators=[MinValueValidator(1), MaxValueValidator(7)])

    # вознаграждение -* чем пользователь должен себя вознаградить после выполнения
    reward = models.CharField(max_length=150, null=True, blank=True, verbose_name='вознаграждение')

    # время на выполнение -* время, которое предположительно потратит пользователь на выполнение привычки
    lead_time = models.IntegerField(default=120, null=True, blank=True, verbose_name='время выполнения',
                                    validators=[MinValueValidator(0), MaxValueValidator(120)])

    # признак публичности -* привычки можно публиковать в общий доступ, чтобы другие пользователи могли брать в пример чужие привычки
    is_public = models.BooleanField(default=True, null=True, blank=True, verbose_name='публикация')
    last_send = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    class Meta:
        verbose_name = 'Привычка'
        verbose_name_plural = 'Привычки'

    def __str__(self):
        return f'Я буду {self.action} в {self.time} {self.place} '
