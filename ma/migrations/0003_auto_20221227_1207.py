# Generated by Django 2.2.28 on 2022-12-27 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ma', '0002_auto_20221215_0604'),
    ]

    operations = [
        migrations.CreateModel(
            name='Examination',
            fields=[
                ('examination_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('sample_requirement', models.CharField(max_length=100)),
                ('edit_specification', models.CharField(max_length=2000)),
                ('description', models.CharField(blank=True, max_length=300, null=True)),
            ],
            options={
                'db_table': 'examination',
                'managed': False,
            },
        ),
        migrations.AlterModelOptions(
            name='result',
            options={'managed': False},
        ),
    ]