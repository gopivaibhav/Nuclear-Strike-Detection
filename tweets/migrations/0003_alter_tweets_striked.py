# Generated by Django 4.1.1 on 2022-10-06 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tweets', '0002_alter_tweets_striked'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweets',
            name='striked',
            field=models.FloatField(),
        ),
    ]
