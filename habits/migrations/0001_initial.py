# Generated by Django 4.1.7 on 2023-03-07 10:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Habit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chat_id', models.CharField(blank=True, max_length=150, null=True, verbose_name='chat id')),
                ('place', models.CharField(blank=True, max_length=150, null=True, verbose_name='место')),
                ('time', models.TimeField(blank=True, null=True, verbose_name='время')),
                ('action', models.CharField(blank=True, max_length=150, null=True, verbose_name='действие')),
                ('is_pleasant_habit', models.BooleanField(blank=True, default=False, null=True, verbose_name='приятная привычка')),
                ('period', models.CharField(choices=[('day', 'day'), ('week', 'week'), ('month', 'month')], default='day', max_length=15, verbose_name='период')),
                ('reward', models.CharField(blank=True, max_length=150, null=True, verbose_name='вознаграждение')),
                ('lead_time', models.IntegerField(blank=True, default=120, null=True, verbose_name='время выполнения')),
                ('is_public', models.BooleanField(blank=True, default=True, null=True, verbose_name='публикация')),
                ('associated_habit', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='associated', to='habits.habit', verbose_name='связанная привычка')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='пользователь')),
            ],
            options={
                'verbose_name': 'Привычка',
                'verbose_name_plural': 'Привычки',
            },
        ),
    ]
