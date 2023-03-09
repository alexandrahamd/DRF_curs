from rest_framework import serializers


class HabitPeriodValidator:
    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        period = int(value.get('period'))
        if period > 7:
            message = 'Период не должен быть больше 7 дней'
            raise serializers.ValidationError(message)


class HabitValidator:
    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        reward = value.get('reward')
        associated_habit = value.get('associated_habit')
        is_pleasant_habit = value.get('is_pleasant_habit')
        if is_pleasant_habit is True:
            if reward:
                message = 'у приятной привычки не может быть вознаграждения'
                raise serializers.ValidationError(message)
            if associated_habit:
                message = 'у приятной привычки не может быть связаной привычки'
                raise serializers.ValidationError(message)

        else:
            if reward and associated_habit:
                message = 'у привычки не должно быть одновременно связанной привычки и вознаграждения'
                raise serializers.ValidationError(message)
            if reward is None and associated_habit is None:
                message = 'связанная привычка и вознаграждение одновремменно не могут быть пустыми'
                raise serializers.ValidationError(message)
            if associated_habit.is_pleasant_habit is False:
                message = 'связанные привычки могут попадать только привычки с признаком приятной привычки'
                raise serializers.ValidationError(message)
