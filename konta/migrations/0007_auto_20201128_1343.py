# Generated by Django 3.1.3 on 2020-11-28 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('konta', '0006_auto_20201128_1341'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]