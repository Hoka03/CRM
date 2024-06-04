# Generated by Django 5.0.6 on 2024-06-02 08:31

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attendance_date', models.DateField()),
                ('status', models.PositiveSmallIntegerField(choices=[(1, 'come'), (2, 'did not come'), (3, 'reason')])),
                ('reason', models.CharField(blank=True, max_length=150)),
                ('student', models.ForeignKey(limit_choices_to={'role': 3}, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('student', 'attendance_date')},
            },
        ),
    ]
