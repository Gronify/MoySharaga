# Generated by Django 3.0.4 on 2020-03-23 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('panel', '0006_auto_20200323_1406'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timetable',
            name='subject_datetime_start',
            field=models.DateTimeField(verbose_name='Время начала пары'),
        ),
        migrations.AlterField(
            model_name='timetable',
            name='subject_datetime_stop',
            field=models.DateTimeField(verbose_name='Время конца пары'),
        ),
    ]
