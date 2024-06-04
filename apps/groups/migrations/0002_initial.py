# Generated by Django 5.0.6 on 2024-06-02 08:31

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('groups', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='studentgroup',
            name='teacher',
            field=models.ForeignKey(limit_choices_to={'role': 2}, on_delete=django.db.models.deletion.PROTECT, related_name='teacher_groups', to=settings.AUTH_USER_MODEL),
        ),
    ]
