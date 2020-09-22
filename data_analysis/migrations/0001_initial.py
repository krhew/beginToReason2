# Generated by Django 3.1.1 on 2020-09-22 19:24

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DataLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_stamp', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('status', models.CharField(max_length=50)),
                ('code', models.TextField(default='null')),
                ('explanation', models.TextField()),
                ('lesson_key', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='core.lesson')),
                ('lesson_set_key', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='core.lessonset')),
                ('user_key', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
