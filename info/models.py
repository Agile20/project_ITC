from django.db import models
import modeltranslation

READY = 'ready'
ACTIVE = 'В разработке'
AWAIT_P = 'В очереди'
STAGE = [
    (READY,'Готов'),
    (ACTIVE,'В разработке'),
    (AWAIT_P,'В очереди')
]


    

class Staff(models.Model):
    city = models.CharField(max_length=127, verbose_name='Город разработчика', default=None)
    name = models.CharField(max_length=127, verbose_name='Имя разработчика')
    position = models.CharField(max_length=127, verbose_name='Позиция разработчика')
    experience = models.CharField(max_length=127, verbose_name='Опыт разработки')
    activity = models.CharField(max_length=127, verbose_name='Активность')

    
    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Персонал'
    
    def __str__(self) -> str:
        return f'{self.name}, {self.position}'

        
class Projects(models.Model):
    image = models.ImageField(upload_to='project',null=True,blank=True, verbose_name='Фото прокта')
    name_of_project = models.CharField(max_length=127, verbose_name='Название проекта')
    stage = models.CharField(max_length=127,choices=STAGE, verbose_name='Стадия разработки')
    staff = models.ManyToManyField(Staff, verbose_name='Персонал работяющий над проектом', null=True, related_name='projects', blank=True)    
    url = models.URLField(max_length=350, verbose_name='Ссылка на проект', default=None)
    
    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'
    
    def __str__(self) -> str:
        return f'{self.name_of_project} {self.stage}'


class AboutUs(models.Model):
    upper_text = models.CharField(max_length=127, verbose_name='Заголовок')
    description = models.TextField(verbose_name='Описание')
    image = models.ImageField(upload_to='anoutusImage/', verbose_name='Фото')

    @property
    def count_ready(self):
        return Projects.objects.filter(stage=READY).count()

    @property
    def count_active(self):
        return Projects.objects.filter(stage=ACTIVE).count()

    @property
    def count_await_p(self):
        return Projects.objects.filter(stage=AWAIT_P).count()

    class Meta:
        verbose_name = 'Про нас'
        verbose_name_plural = 'Про нас'
    
    def __str__(self) -> str:
        return f'Содержание части "Про нас"'


class Image(models.Model):
    image = models.ImageField(upload_to='what_we_useImage',verbose_name='Иконка')

    class Meta:
        verbose_name = 'Иконка'
        verbose_name_plural = 'Иконки'

    def __str__(self) -> str:
        return f'Иконка'

class WhatWeUse(models.Model):
    title = models.CharField(max_length=123, verbose_name='Заголовок')
    description = models.TextField(verbose_name='Описание')
    image = models.ManyToManyField(Image, verbose_name='Фото')

    class Meta:
        verbose_name = 'Наша технология'
        verbose_name_plural = 'Наши технологии'

    def __str__(self) -> str:
        return f'Содержание части "Наши технологии"'

class TypeOfWork(models.Model):
    introduction = models.TextField(verbose_name='вступление')
    type_of_service = models.CharField(max_length=127,verbose_name='Ваши услуги')
    image = models.ImageField(upload_to='workImage/', verbose_name='Фото',default=None)
    description_of_service = models.TextField(verbose_name='Описание вашей услуги')

    class Meta:
        verbose_name = 'Наша услуга'
        verbose_name_plural = 'Наши услуги'
    
    def __str__(self) -> str:
        return f'Содержание части "Наши услуги"'


class OurPartner(models.Model):
    name = models.CharField(max_length=127,verbose_name='Название компании партнера')
    logo = models.ImageField(upload_to = 'logo/',default=None,verbose_name='Лого')
    url = models.URLField(max_length=350, verbose_name='Ссылка на партнера', default=None)

    class Meta:
        verbose_name = 'Наш партнер'
        verbose_name_plural = 'Наши партнеры'
   
    def __str__(self) -> str:
        return self.name


class EventLent(models.Model):
    name = models.CharField(max_length=127,verbose_name='Заголовок')
    image = models.ImageField(upload_to = 'image/',default=None,verbose_name='Фото в новостной ленте')
    description = models.TextField(verbose_name='Описание')

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Лента новостей'

    def __str__(self) -> str:
        return self.name


class FreeVacancy(models.Model):
    position = models.CharField(max_length=127,verbose_name='Позиция контрагента')
    period = models.CharField(max_length=127,verbose_name='Срок')
    requirements = models.TextField(verbose_name='Требования')
    responsibilities = models.TextField(verbose_name='Обязаности')
    you_ll_recive = models.TextField(verbose_name='Контрагент получит')

    class Meta:
        verbose_name = 'Свободная вакансия'
        verbose_name_plural = 'Свободные вакансии'

    def __str__(self) -> str:
        return f"{self.position} {self.period}"



class SubmitApplication(models.Model):
    name = models.CharField(max_length=127,verbose_name='ФИО контрагента')
    email = models.EmailField(max_length=127,verbose_name='E-mail')
    resume = models.TextField(verbose_name='Резюме')
    freevacancy = models.ForeignKey(FreeVacancy, on_delete=models.CASCADE,default=FreeVacancy ,verbose_name='подал на место')
    cvfile = models.ImageField(upload_to='applicationImage/', verbose_name='CV файл - фото/резюме')

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'

    def __str__(self) -> str:
        return f'Поступила заявка от: {self.name}. На место {self.freevacancy} '


class Connection(models.Model):
    adress = models.CharField(max_length=127, verbose_name='Адресс(офиса)')
    email = models.CharField(max_length=127, verbose_name='Email адресс для связи')
    phone_number = models.CharField(max_length=127, verbose_name='Номер для связи')
    social_network = models.URLField(max_length=500, verbose_name='Соц. сети',  default=None)
    
    class Meta:
        verbose_name = 'Контакт/Связь'
        verbose_name_plural = 'Контакты/Связь'
    
    def __str__(self) -> str:
        return self.adress


class QuestionAnswer(models.Model):
    question = models.CharField(max_length=127, verbose_name='Вопрос')
    answer = models.TextField(verbose_name='Ответ',default='нет ответа')
    
    class Meta:
        verbose_name = 'Часто задаваемый Вопрос/Ответ'
        verbose_name_plural = 'Часто задаваемые Вопросы/Ответы'

    def __str__(self) -> str:
        return self.question


# class Feedback(models.Model):
#     feedback = models.TextField(verbose_name='Отзыв')
#     name = models.CharField(max_length=127, verbose_name='ФИО')

#     class Meta:
#         verbose_name = 'Отзыв'
#         verbose_name_plural = 'Отзывы'

#     def __str__(self) -> str:
#         return self.name

class GetConsult(models.Model):
    name = models.CharField(max_length=127,verbose_name='Фио')
    question = models.CharField(max_length=127,verbose_name='Вопрос клиента')
    contact = models.CharField(max_length=150, verbose_name='Контакты клиента')
    got_answer = models.CharField(max_length=127, verbose_name='получил ли клиент ответ', default='ожидание ответа/нет ответа')

    class Meta:
        verbose_name = 'Консультация'
        verbose_name_plural = 'Консультация'

    def __str__(self) -> str:
        return self.got_answer


class Ad(models.Model):
    name = models.CharField(max_length=127, verbose_name='Название компании рекламодателя')
    image = models.ImageField(upload_to='adImage/', verbose_name='Рекламное фото')
    logo = models.ImageField(upload_to='adLogo/', verbose_name='Логотип рекламодателя')
    description = models.TextField(verbose_name='Описание')
    url = models.URLField(max_length=350, verbose_name='Ссылка на рекламодателя',default=None)

    class Meta:
        verbose_name = 'Реклама'
        verbose_name_plural = 'Реклама'

    def __str__(self) -> str:
        return self.name

