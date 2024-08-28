# Generated by Django 5.1 on 2024-08-23 00:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car_api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AutoMarkaModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marka_name', models.CharField(max_length=255, verbose_name='Название марки авто')),
                ('model_name', models.CharField(max_length=255, verbose_name='Название модели авто')),
            ],
            options={
                'verbose_name': 'Марка и модель авто',
                'verbose_name_plural': 'Марки и модели авто',
            },
        ),
    ]
