# Generated by Django 3.1.3 on 2020-11-28 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=80)),
                ('password', models.CharField(max_length=80)),
                ('age', models.IntegerField()),
            ],
        ),
    ]