# Generated by Django 2.2.26 on 2022-12-15 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ma', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='result',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]