# Generated by Django 2.2.1 on 2019-05-30 03:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exercises', '0003_exercises_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exercises',
            name='user',
        ),
    ]