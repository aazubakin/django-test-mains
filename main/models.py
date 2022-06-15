from enum import unique
from tabnanny import verbose
from django.db import models
from django.test import client

# Create your models here.


class Client(models.Model):
    """Клиент"""

    name = models.CharField('Имя клиента', max_length=255)

    class Meta:
        verbose_name = "Клиент"
        verbose_name_plural = "Клиенты"

    def __str__(self) -> str:
        return self.name


class Bill(models.Model):
    """Счет"""

    number = models.IntegerField('Номер счета')
    organization = models.ForeignKey(
        'main.Organization', verbose_name='Организация', on_delete=models.CASCADE
    )
    sum_bill = models.CharField('Сумма', max_length=255)
    date_created = models.DateTimeField(
        'Дата', auto_now_add=True, db_index=True)

    number_org = models.CharField('Уникальное поле', max_length=255, unique=True)

    def save(self, *args, **kwargs):
        self.number_org = str(self.number) + self.organization.name
        return super(Bill, self).save(*args, **kwargs)


    class Meta:
        verbose_name = "Счет"
        verbose_name_plural = "Счета"

    def __str__(self) -> str:
        return f'Счет №: {self.number}'


class Organization(models.Model):
    """Организация"""

    clients = models.ForeignKey(
        'Client', verbose_name='Клиент', on_delete=models.CASCADE, blank=True, null=True
    )
    name = models.CharField('Название организации', max_length=255)

    client_name_org_name = models.CharField('Уникальное поле', max_length=255, unique=True)

    class Meta:
        verbose_name = "Организация"
        verbose_name_plural = "Организации"

    def save(self, *args, **kwargs):
        self.client_name_org_name = self.clients.name + self.name
        return super(Organization, self).save(*args, **kwargs)

    def __str__(self) -> str:
        return self.name
