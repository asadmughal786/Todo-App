# Generated by Django 4.0.4 on 2022-05-12 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dummy', '0003_alter_todos_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='todos',
            name='completed',
            field=models.BooleanField(default=False),
        ),
    ]