# Generated by Django 4.1.7 on 2023-03-08 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todolist',
            old_name='title',
            new_name='task',
        ),
        migrations.AddField(
            model_name='todolist',
            name='details',
            field=models.TextField(blank=True, null=True),
        ),
    ]