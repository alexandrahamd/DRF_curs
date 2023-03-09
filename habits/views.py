from django.db.models import QuerySet
from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from habits.models import Habit
from habits.permissions import IsOwner
from habits.serializers import HabitSerializer
import requests


# Create your views here.
class HabitListMyAPIView(generics.ListAPIView):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        assert self.queryset is not None, (
            "'%s' should either include a `queryset` attribute, "
            "or override the `get_queryset()` method."
            % self.__class__.__name__
        )

        queryset = Habit.objects.filter(user=self.request.user)
        if isinstance(queryset, QuerySet):
            # Ensure queryset is re-evaluated on each request.
            queryset = queryset.all()
        return queryset


class HabitListAllAPIView(generics.ListAPIView):
    queryset = Habit.objects.filter(is_public=True)
    serializer_class = HabitSerializer


class HabitCreateAPIView(generics.CreateAPIView):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated]


class HabitDestroyAPIView(generics.DestroyAPIView):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated & IsOwner]


class HabitUpdateAPIView(generics.UpdateAPIView):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated, IsOwner]


