# Generated by Django 4.1.5 on 2023-11-22 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student_attendance', '0008_remove_student_attendance_attendance_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student_attendance',
            name='attendance_date_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
