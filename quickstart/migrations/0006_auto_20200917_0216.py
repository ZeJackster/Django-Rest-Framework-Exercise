# Generated by Django 3.1.1 on 2020-09-17 06:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quickstart', '0005_auto_20200917_0215'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dogs',
            name='breed',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Breeds_name', to='quickstart.breed'),
        ),
    ]
