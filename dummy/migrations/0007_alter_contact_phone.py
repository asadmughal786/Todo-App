# Generated by Django 4.0.4 on 2022-05-20 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dummy', '0006_delete_sign_up'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='phone',
            field=models.IntegerField(max_length=20),
        ),
    ]