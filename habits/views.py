from django.db.models import QuerySet
from django.shortcuts import render
from requests import Response
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.renderers import TemplateHTMLRenderer

from habits.models import Habit
from habits.permissions import IsOwner
from habits.serializers import HabitSerializer
import requests


# Create your views here.
class HabitListMyAPIView(generics.ListAPIView):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated]
    template_name = 'base.html'

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


class MyHTMLRenderer(TemplateHTMLRenderer):
    def get_template_context(self, *args, **kwargs):
        context = super().get_template_context(*args, **kwargs)
        if isinstance(context, list):
            context = {"items": context}
        return context


class HabitListAllAPIView(generics.ListAPIView):
    # queryset = Habit.objects.filter(is_public=True)
    serializer_class = HabitSerializer
    renderer_classes = [MyHTMLRenderer]
    template_name = 'habits/base.html'

    def get(self, request, *args, **kwargs):
        queryset = Habit.objects.all()
        return Response({'profiles': queryset})

    # def get(self, request, *args, **kwargs):
    #     queryset = Habit.objects.all()
    #     content = {'habits': queryset}
    #     return Response(content)

    # def list(self, request, *args, **kwargs):
    #     queryset = self.filter_queryset(self.get_queryset())
    #
    #     page = self.paginate_queryset(queryset)
    #     if page is not None:
    #         serializer = self.get_serializer(page, many=True)
    #         return self.get_paginated_response(serializer.data)
    #
    #     serializer = self.get_serializer(queryset, many=True)
    #     return Response(serializer.data, "habits/base.html")
    #     # return render(serializer.data, "habits/base.html")


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


