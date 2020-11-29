# Generated by Django 3.1.3 on 2020-11-28 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('konta', '0004_auto_20201128_1329'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='zamowienie',
            name='tags',
            field=models.ManyToManyField(to='konta.Tags'),
        ),
    ]