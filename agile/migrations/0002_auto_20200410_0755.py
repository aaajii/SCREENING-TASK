# Generated by Django 3.0.5 on 2020-04-10 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agile', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='details',
            field=models.CharField(max_length=500),
        ),
    ]
