# Generated by Django 3.0.8 on 2020-11-02 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0017_auto_20201101_1038'),
    ]

    operations = [
        migrations.AddField(
            model_name='resume',
            name='addition',
            field=models.TextField(blank=True, verbose_name='Дополнительно'),
        ),
        migrations.AlterField(
            model_name='vacancy',
            name='responsibilities',
            field=models.TextField(blank=True, verbose_name='Обязанности'),
        ),
        migrations.AlterField(
            model_name='vacancy',
            name='town',
            field=models.CharField(max_length=15, verbose_name='Местоположение'),
        ),
    ]
