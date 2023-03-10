# Generated by Django 3.2.7 on 2023-02-13 13:09

from django.db import migrations, models
import django.db.models.deletion
import info.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('info', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('upper_text', models.CharField(max_length=127, verbose_name='Заголовок')),
                ('upper_text_ru', models.CharField(max_length=127, null=True, verbose_name='Заголовок')),
                ('upper_text_en', models.CharField(max_length=127, null=True, verbose_name='Заголовок')),
                ('description', models.TextField(verbose_name='Описание')),
                ('description_ru', models.TextField(null=True, verbose_name='Описание')),
                ('description_en', models.TextField(null=True, verbose_name='Описание')),
                ('image', models.ImageField(upload_to='anoutusImage/', verbose_name='Фото')),
            ],
            options={
                'verbose_name': 'Про нас',
                'verbose_name_plural': 'Про нас',
            },
        ),
        migrations.CreateModel(
            name='Ad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=127, verbose_name='Название компании рекламодателя')),
                ('image', models.ImageField(upload_to='adImage/', verbose_name='Рекламное фото')),
                ('logo', models.ImageField(upload_to='adLogo/', verbose_name='Логотип рекламодателя')),
                ('description', models.TextField(verbose_name='Описание')),
                ('url', models.URLField(default=None, max_length=350, verbose_name='Ссылка на рекламодателя')),
            ],
            options={
                'verbose_name': 'Реклама',
                'verbose_name_plural': 'Реклама',
            },
        ),
        migrations.CreateModel(
            name='Connection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adress', models.CharField(max_length=127, verbose_name='Адресс(офиса)')),
                ('email', models.CharField(max_length=127, verbose_name='Email адресс для связи')),
                ('phone_number', models.CharField(max_length=127, verbose_name='Номер для связи')),
                ('social_network', models.URLField(default=None, max_length=500, verbose_name='Соц. сети')),
            ],
            options={
                'verbose_name': 'Контакт/Связь',
                'verbose_name_plural': 'Контакты/Связь',
            },
        ),
        migrations.CreateModel(
            name='EventLent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=127, verbose_name='Заголовок')),
                ('name_ru', models.CharField(max_length=127, null=True, verbose_name='Заголовок')),
                ('name_en', models.CharField(max_length=127, null=True, verbose_name='Заголовок')),
                ('image', models.ImageField(default=None, upload_to='image/', verbose_name='Фото в новостной ленте')),
                ('description', models.TextField(verbose_name='Описание')),
                ('description_ru', models.TextField(null=True, verbose_name='Описание')),
                ('description_en', models.TextField(null=True, verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Новость',
                'verbose_name_plural': 'Лента новостей',
            },
        ),
        migrations.CreateModel(
            name='FreeVacancy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.CharField(max_length=127, verbose_name='Позиция контрагента')),
                ('position_ru', models.CharField(max_length=127, null=True, verbose_name='Позиция контрагента')),
                ('position_en', models.CharField(max_length=127, null=True, verbose_name='Позиция контрагента')),
                ('period', models.CharField(max_length=127, verbose_name='Срок')),
                ('period_ru', models.CharField(max_length=127, null=True, verbose_name='Срок')),
                ('period_en', models.CharField(max_length=127, null=True, verbose_name='Срок')),
                ('requirements', models.TextField(verbose_name='Требования')),
                ('requirements_ru', models.TextField(null=True, verbose_name='Требования')),
                ('requirements_en', models.TextField(null=True, verbose_name='Требования')),
                ('responsibilities', models.TextField(verbose_name='Обязаности')),
                ('responsibilities_ru', models.TextField(null=True, verbose_name='Обязаности')),
                ('responsibilities_en', models.TextField(null=True, verbose_name='Обязаности')),
                ('you_ll_recive', models.TextField(verbose_name='Контрагент получит')),
                ('you_ll_recive_ru', models.TextField(null=True, verbose_name='Контрагент получит')),
                ('you_ll_recive_en', models.TextField(null=True, verbose_name='Контрагент получит')),
            ],
            options={
                'verbose_name': 'Свободная вакансия',
                'verbose_name_plural': 'Свободные вакансии',
            },
        ),
        migrations.CreateModel(
            name='GetConsult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=127, verbose_name='Фио')),
                ('question', models.CharField(max_length=127, verbose_name='Вопрос клиента')),
                ('contact', models.CharField(max_length=150, verbose_name='Контакты клиента')),
                ('got_answer', models.CharField(default='ожидание ответа/нет ответа', max_length=127, verbose_name='получил ли клиент ответ')),
            ],
            options={
                'verbose_name': 'Консультация',
                'verbose_name_plural': 'Консультация',
            },
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='what_we_useImage', verbose_name='Иконка')),
            ],
            options={
                'verbose_name': 'Иконка',
                'verbose_name_plural': 'Иконки',
            },
        ),
        migrations.CreateModel(
            name='OurPartner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=127, verbose_name='Название компании партнера')),
                ('logo', models.ImageField(default=None, upload_to='logo/', verbose_name='Лого')),
                ('url', models.URLField(default=None, max_length=350, verbose_name='Ссылка на партнера')),
            ],
            options={
                'verbose_name': 'Наш партнер',
                'verbose_name_plural': 'Наши партнеры',
            },
        ),
        migrations.CreateModel(
            name='QuestionAnswer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=127, verbose_name='Вопрос')),
                ('question_ru', models.CharField(max_length=127, null=True, verbose_name='Вопрос')),
                ('question_en', models.CharField(max_length=127, null=True, verbose_name='Вопрос')),
                ('answer', models.TextField(default='нет ответа', verbose_name='Ответ')),
                ('answer_ru', models.TextField(default='нет ответа', null=True, verbose_name='Ответ')),
                ('answer_en', models.TextField(default='нет ответа', null=True, verbose_name='Ответ')),
            ],
            options={
                'verbose_name': 'Часто задаваемый Вопрос/Ответ',
                'verbose_name_plural': 'Часто задаваемые Вопросы/Ответы',
            },
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=127, verbose_name='Имя разработчика')),
                ('name_ru', models.CharField(max_length=127, null=True, verbose_name='Имя разработчика')),
                ('name_en', models.CharField(max_length=127, null=True, verbose_name='Имя разработчика')),
                ('position', models.CharField(max_length=127, verbose_name='Позиция разработчика')),
                ('position_ru', models.CharField(max_length=127, null=True, verbose_name='Позиция разработчика')),
                ('position_en', models.CharField(max_length=127, null=True, verbose_name='Позиция разработчика')),
                ('experience', models.CharField(max_length=127, verbose_name='Опыт разработки')),
                ('experience_ru', models.CharField(max_length=127, null=True, verbose_name='Опыт разработки')),
                ('experience_en', models.CharField(max_length=127, null=True, verbose_name='Опыт разработки')),
                ('activity', models.CharField(max_length=127, verbose_name='Активность')),
                ('activity_ru', models.CharField(max_length=127, null=True, verbose_name='Активность')),
                ('activity_en', models.CharField(max_length=127, null=True, verbose_name='Активность')),
            ],
            options={
                'verbose_name': 'Сотрудник',
                'verbose_name_plural': 'Персонал',
            },
        ),
        migrations.CreateModel(
            name='TypeOfWork',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('introduction', models.TextField(verbose_name='вступление')),
                ('introduction_ru', models.TextField(null=True, verbose_name='вступление')),
                ('introduction_en', models.TextField(null=True, verbose_name='вступление')),
                ('type_of_service', models.CharField(max_length=127, verbose_name='Ваши услуги')),
                ('type_of_service_ru', models.CharField(max_length=127, null=True, verbose_name='Ваши услуги')),
                ('type_of_service_en', models.CharField(max_length=127, null=True, verbose_name='Ваши услуги')),
                ('image', models.ImageField(default=None, upload_to='workImage/', verbose_name='Фото')),
                ('description_of_service', models.TextField(verbose_name='Описание вашей услуги')),
                ('description_of_service_ru', models.TextField(null=True, verbose_name='Описание вашей услуги')),
                ('description_of_service_en', models.TextField(null=True, verbose_name='Описание вашей услуги')),
            ],
            options={
                'verbose_name': 'Наша услуга',
                'verbose_name_plural': 'Наши услуги',
            },
        ),
        migrations.CreateModel(
            name='WhatWeUse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=123, verbose_name='Заголовок')),
                ('title_ru', models.CharField(max_length=123, null=True, verbose_name='Заголовок')),
                ('title_en', models.CharField(max_length=123, null=True, verbose_name='Заголовок')),
                ('description', models.TextField(verbose_name='Описание')),
                ('description_ru', models.TextField(null=True, verbose_name='Описание')),
                ('description_en', models.TextField(null=True, verbose_name='Описание')),
                ('image', models.ManyToManyField(to='info.Image', verbose_name='Фото')),
            ],
            options={
                'verbose_name': 'Наша технология',
                'verbose_name_plural': 'Наши технологии',
            },
        ),
        migrations.CreateModel(
            name='SubmitApplication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=127, verbose_name='ФИО контрагента')),
                ('email', models.EmailField(max_length=127, verbose_name='E-mail')),
                ('resume', models.TextField(verbose_name='Резюме')),
                ('cvfile', models.ImageField(upload_to='applicationImage/', verbose_name='CV файл - фото/резюме')),
                ('freevacancy', models.ForeignKey(default=info.models.FreeVacancy, on_delete=django.db.models.deletion.CASCADE, to='info.freevacancy', verbose_name='подал на место')),
            ],
            options={
                'verbose_name': 'Заявка',
                'verbose_name_plural': 'Заявки',
            },
        ),
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='project', verbose_name='Фото прокта')),
                ('name_of_project', models.CharField(max_length=127, verbose_name='Название проекта')),
                ('stage', models.CharField(choices=[('ready', 'Готов'), ('В разработке', 'В разработке'), ('В очереди', 'В очереди')], max_length=127, verbose_name='Стадия разработки')),
                ('url', models.URLField(default=None, max_length=350, verbose_name='Ссылка на проект')),
                ('staff', models.ManyToManyField(blank=True, null=True, related_name='projects', to='info.Staff', verbose_name='Персонал работяющий над проектом')),
            ],
            options={
                'verbose_name': 'Проект',
                'verbose_name_plural': 'Проекты',
            },
        ),
    ]
