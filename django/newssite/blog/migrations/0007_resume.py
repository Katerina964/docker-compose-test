# Generated by Django 3.0.8 on 2020-10-22 13:12

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20200827_0921'),
    ]

    operations = [
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=15, verbose_name='Имя')),
                ('surname', models.CharField(max_length=15, verbose_name='Фамилия')),
                ('position', models.CharField(help_text='Желаемая должность', max_length=40, verbose_name='Позиция')),
                ('town', models.CharField(max_length=15, verbose_name='Город')),
                ('phone', models.CharField(max_length=30, verbose_name='Телефон')),
                ('email', models.EmailField(max_length=25, verbose_name='Почта')),
                ('passsword', models.EmailField(help_text='Запомните пароль или запишите', max_length=20, verbose_name='Пароль авторизации на сайте')),
                ('experience', models.TextField(help_text='Укажите  опыт в порядке убывания', verbose_name='Опыт работы')),
                ('skills', models.CharField(max_length=500, verbose_name='Навыки')),
                ('achievements', models.CharField(max_length=500, verbose_name='Достижения')),
                ('education', models.CharField(max_length=300, verbose_name='Образование')),
                ('tipe_work', models.CharField(help_text='Укажите важные для Вас критерии. Например: офис, удаленно, количество часов в день', max_length=100, verbose_name='Вид занятости')),
                ('published_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата размещения')),
            ],
        ),
    ]
