from django.db import models

# Create your models here.
NULLABLE = {'blank': True, 'null': True}


class Product(models.Model):
    product_name = models.CharField(max_length=100, verbose_name='Наименование продукта')
    description = models.TextField( verbose_name='Описание')
    avatar = models.ImageField(upload_to='products/', verbose_name='Превью', null=True, blank=True)
    category = models.CharField(max_length=100, verbose_name='Категория')
    price = models.IntegerField(verbose_name='Цена')
    date_of_creation = models.DateTimeField(verbose_name='Дата создания')
    date_of_last_chanage = models.DateTimeField(verbose_name='Дата последнего изменения')


    def __str__(self):
        return f'{self.product_name} {self.description}'

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ('product_name',)

class Category(models.Model):
    product_name = models.CharField(max_length=100, verbose_name='Наименование продукта')
    description = models.TextField( verbose_name='Описание')

    def __str__(self):
        return f'{self.product_name} {self.description}'

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ('product_name',)