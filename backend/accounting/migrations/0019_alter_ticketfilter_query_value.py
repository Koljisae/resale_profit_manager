# Generated by Django 4.2.2 on 2023-07-09 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounting', '0018_ticketfilter_url_value'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticketfilter',
            name='query_value',
            field=models.CharField(blank=True, max_length=150, verbose_name='Query'),
        ),
    ]
