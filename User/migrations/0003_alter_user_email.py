# Generated by Django 5.1.6 on 2025-02-19 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("User", "0002_alter_user_managers_alter_user_email_alter_user_role"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="email",
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]
