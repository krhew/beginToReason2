# Generated by Django 3.0.7 on 2020-06-30 14:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tutor', '0010_reasoning_mc_set'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reasoning',
            name='mc_set',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='tutor.MC_Set'),
        ),
    ]
