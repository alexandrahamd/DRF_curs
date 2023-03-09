from rest_framework import serializers
from habits.models import Habit
from habits.validators import HabitPeriodValidator, HabitValidator


class HabitSerializer(serializers.ModelSerializer):

    class Meta:
        model = Habit
        fields = '__all__'
        validators = [HabitPeriodValidator(field='period'), HabitValidator(field='reward')]
