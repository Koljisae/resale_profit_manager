# Generated by Django 4.2.2 on 2023-07-02 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounting', '0010_alter_ticket_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='closed_at',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='Closing date'),
        ),
    ]
