# Generated by Django 4.0.4 on 2022-05-12 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dummy', '0002_todos'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todos',
            name='title',
            field=models.CharField(max_length=50),
        ),
    ]
