# Generated by Django 4.1.7 on 2023-04-17 20:10

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("base", "0002_remove_user_user_id"),
    ]

    operations = [
        migrations.CreateModel(
            name="ToDoList",
            fields=[
                (
                    "id",
                    models.CharField(
                        max_length=2000, primary_key=True, serialize=False
                    ),
                ),
                ("todoText", models.CharField(max_length=2000)),
                ("isDone", models.BinaryField()),
            ],
        ),
    ]
