from django.urls import path
from habits.apps import HabitsConfig
from habits.views import HabitDestroyAPIView, HabitUpdateAPIView, HabitListAllAPIView, HabitListMyAPIView, \
    HabitCreateAPIView


app_name = HabitsConfig.name


urlpatterns = [
    path('', HabitListAllAPIView.as_view(), name='habits_list'),
    path('my_habits/', HabitListMyAPIView.as_view(), name='my_habits_list'),
    path('update/<int:pk>/', HabitUpdateAPIView.as_view(), name='habit_update'),
    path('create/', HabitCreateAPIView.as_view(), name='habit_create'),
    path('delete/<int:pk>/', HabitDestroyAPIView.as_view(), name='habit_delete'),
              ]