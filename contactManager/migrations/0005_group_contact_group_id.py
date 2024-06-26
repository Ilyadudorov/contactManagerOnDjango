# Generated by Django 4.2.4 on 2023-08-26 06:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contactManager', '0004_alter_contact_phonenumber'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='contact',
            name='group_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='contactManager.group'),
        ),
    ]
