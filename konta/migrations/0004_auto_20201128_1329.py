# Generated by Django 3.1.3 on 2020-11-28 12:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('konta', '0003_produkt_zamowienie'),
    ]

    operations = [
        migrations.AddField(
            model_name='zamowienie',
            name='klient',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='konta.users'),
        ),
        migrations.AddField(
            model_name='zamowienie',
            name='produkt',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='konta.produkt'),
        ),
    ]
