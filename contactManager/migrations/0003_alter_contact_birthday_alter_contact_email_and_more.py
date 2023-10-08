# Generated by Django 4.2.3 on 2023-08-06 15:43

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contactManager', '0002_contact_is_favorite_contact_note_contact_photo_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='birthday',
            field=models.CharField(blank=True, max_length=40, validators=[django.core.validators.RegexValidator(regex='(?:(?:31(\\/|-|\\.)(?:0?[13578]|1[02]))\\1|(?:(?:29|30)(\\/|-|\\.)(?:0?[13-9]|1[0-2])\\2))(?:(?:1[6-9]|[2-9]\\d)?\\d{2})$|^(?:29(\\/|-|\\.)0?2\\3(?:(?:(?:1[6-9]|[2-9]\\d)?(?:0[48]|[2468][048]|[13579][26])|(?:(?:16|[2468][048]|[3579][26])00))))$|^(?:0?[1-9]|1\\d|2[0-8])(\\/|-|\\.)(?:(?:0?[1-9])|(?:1[0-2]))\\4(?:(?:1[6-9]|[2-9]\\d)?\\d{2})')]),
        ),
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.EmailField(blank=True, max_length=254),
        ),
        migrations.AlterField(
            model_name='contact',
            name='phoneNumber',
            field=models.CharField(blank=True, max_length=50, unique=True, validators=[django.core.validators.RegexValidator(regex='^\\+[1-9]\\d{1,16}$')]),
        ),
        migrations.AlterField(
            model_name='contact',
            name='position',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]
