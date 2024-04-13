# Generated by Django 4.1.5 on 2023-11-16 18:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('academic_sessions', '0002_academic_sessions_ongoing_and_more'),
        ('classes', '0001_initial'),
        ('student_attendance', '0002_remove_student_attendance_status_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='student_attendance',
            name='academic_session',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='stud_attendance_academic_session', to='academic_sessions.academic_sessions'),
        ),
        migrations.AddField(
            model_name='student_attendance',
            name='student_class',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='stud_attendance_class', to='classes.class_details'),
        ),
    ]