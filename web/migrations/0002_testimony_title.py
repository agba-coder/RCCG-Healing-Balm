# Generated by Django 4.2 on 2023-07-31 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='testimony',
            name='title',
            field=models.CharField(default=0, help_text='e.g Deliverance from depression. Short and precise.', max_length=50),
            preserve_default=False,
        ),
    ]
