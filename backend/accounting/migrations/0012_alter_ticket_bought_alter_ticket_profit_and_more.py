# Generated by Django 4.2.2 on 2023-07-02 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounting', '0011_alter_ticket_closed_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='bought',
            field=models.IntegerField(default=0, verbose_name='Bought'),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='profit',
            field=models.IntegerField(blank=True, null=True, verbose_name='Profit'),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='sold',
            field=models.IntegerField(blank=True, null=True, verbose_name='Sold'),
        ),
    ]
