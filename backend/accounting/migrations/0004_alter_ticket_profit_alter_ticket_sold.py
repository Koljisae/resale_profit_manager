# Generated by Django 4.2.2 on 2023-06-25 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounting', '0003_alter_ticket_closed_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='profit',
            field=models.IntegerField(blank=True, help_text='54 = 0,54 $', null=True, verbose_name='Profit'),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='sold',
            field=models.IntegerField(blank=True, help_text='902 = 9,02 $', null=True, verbose_name='Sold'),
        ),
    ]
