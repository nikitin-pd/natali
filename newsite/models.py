from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE


class Service(models.Model):
    service_name = models.CharField('Название услуги', max_length=50)
    service_photo = models.ImageField(
        'Фотография услуги', upload_to='natal/newsite/templates/newsite/images')
    service_description = models.TextField('Описание услуги')
    service_price = models.IntegerField('Цена услуги')
    service_number = models.IntegerField('Номер отображения', default=100)
    service_is_active = models.BooleanField(
        'Видимость для покупки', default=True)

    def __str__(self):
        return (('Услуга: \"%s\"') % (self.service_name))

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'


class OrderStatus(models.Model):
    name = models.TextField('Название статуса')

    def __str__(self):
        return (self.name)

    class Meta:
        verbose_name = 'Статус'
        verbose_name_plural = 'Статусы'


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=CASCADE,
                             verbose_name='Пользователь')
    services = models.TextField('Список услуг в заказе')
    cost = models.IntegerField('Цена заказа')
    user_text = models.TextField('Примечание к заказу')
    status = models.ForeignKey(
        OrderStatus, on_delete=CASCADE, verbose_name='Статус')
    date = models.DateTimeField('Дата и время заказа', default='2000-01-01')

    def __str__(self):
        return (('Заказ №%s') % (self.pk))

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
