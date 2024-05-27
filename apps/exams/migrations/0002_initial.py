# Generated by Django 5.0.6 on 2024-05-26 11:14

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('exams', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='examresult',
            name='student',
            field=models.ForeignKey(limit_choices_to=3, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterUniqueTogether(
            name='exam',
            unique_together={('subject', 'nth_month')},
        ),
    ]
