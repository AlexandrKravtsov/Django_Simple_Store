from django.db import models


class ProductCategory(models.Model):
    name = models.CharField(max_length=64, unique=True, verbose_name='название')
    description = models.TextField(blank=True, verbose_name='описание')

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=256, verbose_name='название')
    image = models.ImageField(upload_to='products_images', blank=True)
    description = models.TextField(blank=True, verbose_name='описание')
    short_description = models.CharField(max_length=64, blank=True, verbose_name='краткое описание')
    price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='цена')
    quantity = models.PositiveIntegerField(default=0, verbose_name='количество')
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'

    def __str__(self):
        return f'{self.name} | {self.category.name}'
