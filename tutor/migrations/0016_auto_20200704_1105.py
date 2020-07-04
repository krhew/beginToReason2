# Generated by Django 3.0.7 on 2020-07-04 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutor', '0015_auto_20200704_1103'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reasoning',
            name='free_response_text',
            field=models.CharField(blank=True, default='Enter default message', max_length=100),
        ),
        migrations.AlterField(
            model_name='reasoning',
            name='mc_set',
            field=models.ManyToManyField(blank=True, null=True, to='tutor.MC_Choice'),
        ),
    ]
