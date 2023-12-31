# Generated by Django 4.2.2 on 2023-06-25 19:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=150, verbose_name='Categories')),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Operation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Title')),
                ('bought', models.IntegerField(default=0)),
                ('sold', models.IntegerField(blank=True)),
                ('profit', models.IntegerField(blank=True)),
                ('created_at', models.DateTimeField(auto_now=True, verbose_name='Date of creation')),
                ('closed_at', models.DateTimeField(verbose_name='Closing date')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='accounting.category', verbose_name='Category')),
            ],
            options={
                'verbose_name': 'Operation',
                'verbose_name_plural': 'Operations',
                'ordering': ['-created_at'],
            },
        ),
    ]
