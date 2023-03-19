from django.db import models


class Phones(models.Model):
    brand =models.ForeignKey('Brand', on_delete=models.DO_NOTHING, null=True)
    title = models.CharField(max_length=80, verbose_name='Модель')
    content = models.TextField(null=True, blank=True, verbose_name='характеристики')
    price = models.FloatField(null=True, blank=True, verbose_name='цена')
    published = models.DateTimeField(auto_now_add=True, db_index=True)

    class Meta:
        db_table = 'Phone'
        verbose_name_plural = 'Телефоны'
        verbose_name = 'Телефон'
        ordering = ('price',)

    def __str__(self):
        return f'{self.title}'


class Brand(models.Model):
    name = models.CharField(max_length=700)


    def __str__(self):
        return f"{self.name}"




# class PhoneModels(models.Model):
#     brand = models.ForeignKey('PhoneModels', on_delete=models.CASCADE, verbose_name='Марка')
#     model = models.CharField(max_length=150, verbose_name='Модель')
#     description = models.TextField(null=True, blank=True, verbose_name='Описание')
#     price = models.IntegerField(null=True, verbose_name='Цена')
#     date = models.DateTimeField(auto_now_add=True, db_index=True)
#     vin = models.IntegerField(null=True, name='Number car: ', verbose_name='Вин номер')
#     color = models.CharField(max_length=50, default='black', verbose_name='Цвет')
