# Generated by Django 3.1.1 on 2020-09-20 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quickstart', '0011_auto_20200917_0413'),
    ]

    operations = [
        migrations.AlterField(
            model_name='breed',
            name='size',
            field=models.CharField(max_length=2),
        ),
    ]
