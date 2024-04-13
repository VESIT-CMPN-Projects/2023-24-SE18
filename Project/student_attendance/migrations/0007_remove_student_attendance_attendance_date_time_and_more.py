# Generated by Django 4.1.5 on 2023-11-22 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student_attendance', '0006_remove_student_attendance_attendance_date_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student_attendance',
            name='attendance_date_time',
        ),
        migrations.AddField(
            model_name='student_attendance',
            name='attendance_date',
            field=models.DateField(default=None, null=True),
        ),
        migrations.AddField(
            model_name='student_attendance',
            name='attendance_time',
            field=models.TimeField(default=None, null=True),
        ),
    ]