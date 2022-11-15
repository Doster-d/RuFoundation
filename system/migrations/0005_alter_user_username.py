# Generated by Django 4.0.6 on 2022-07-20 07:06

import django.contrib.auth.validators
import django.contrib.postgres.fields.citext
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0004_alter_user_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='username',
            field=django.contrib.postgres.fields.citext.CITextField(error_messages={'unique': 'Пользователь с данным именем уже существует'}, max_length=150, unique=True, validators=[
                                                                    django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='Имя пользователя'),
        ),
    ]
