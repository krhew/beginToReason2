# Generated by Django 3.0.7 on 2020-07-04 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutor', '0013_auto_20200704_1057'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reasoning',
            old_name='response_text',
            new_name='free_response_text',
        ),
        migrations.AlterField(
            model_name='reasoning',
            name='mc_set',
            field=models.ManyToManyField(blank=True, null=True, to='tutor.MC_Choice'),
        ),
    ]
