# Generated by Django 4.1.7 on 2023-04-26 05:41

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("base", "0003_todolist"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="email",
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
