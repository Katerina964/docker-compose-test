# Generated by Django 3.0.8 on 2020-10-23 09:54

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20201022_1320'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vacancy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.CharField(help_text='Желаемая должность', max_length=50, verbose_name='Позиция')),
                ('company', models.CharField(blank=True, max_length=40, verbose_name='Kомпания')),
                ('type_work', models.CharField(help_text='Укажите важные для Вас критерии. Например: офис, удаленно, количество часов в день', max_length=100, verbose_name='Вид занятости')),
                ('town', models.CharField(max_length=15, verbose_name='Город')),
                ('phone', models.CharField(max_length=30, verbose_name='Телефон')),
                ('email', models.EmailField(max_length=30, verbose_name='Почта')),
                ('password', models.EmailField(help_text='Запомните пароль или запишите', max_length=20, verbose_name='Пароль авторизации на сайте')),
                ('description', models.TextField(verbose_name='Описание вакансии')),
                ('Responsibilities', models.TextField(blank=True, verbose_name='Обязанности')),
                ('skills', models.CharField(max_length=500, verbose_name='Навыки')),
                ('offer', models.TextField(verbose_name='Мы предлагаем')),
                ('published_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата размещения')),
            ],
        ),
        migrations.AlterField(
            model_name='resume',
            name='achievements',
            field=models.CharField(blank=True, max_length=500, verbose_name='Достижения'),
        ),
        migrations.AlterField(
            model_name='resume',
            name='email',
            field=models.EmailField(max_length=30, verbose_name='Почта'),
        ),
        migrations.AlterField(
            model_name='resume',
            name='position',
            field=models.CharField(help_text='Желаемая должность', max_length=50, verbose_name='Позиция'),
        ),
        migrations.AlterField(
            model_name='resume',
            name='town',
            field=models.CharField(blank=True, max_length=15, verbose_name='Город'),
        ),
    ]
