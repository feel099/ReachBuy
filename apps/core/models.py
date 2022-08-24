from django.db import models
from django.contrib.auth.models import PermissionsMixin, AbstractUser
from django.urls import reverse


class User(AbstractUser):
    location = models.CharField(max_length=30, null=True, blank=True, verbose_name='Страна')
    birth_date = models.DateField(null=True, blank=True, verbose_name='День рождения')
    phone = models.CharField(max_length=20, null=True, blank=True, verbose_name='Номер телефона')
    avatar = models.ImageField(null=True, blank=True)
    city = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.get_username()


class Category(models.Model):

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    name = models.CharField(verbose_name='Название категории', max_length=200)
    description = models.TextField(null=True, blank=True, verbose_name='Описание категории')

    def __str__(self):
        return self.name


class Product(models.Model):

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    name = models.CharField(verbose_name='Название продукта', max_length=200)
    image = models.ImageField(upload_to='media', null=True, blank=True)
    description = models.TextField(verbose_name='Описание продукта')
    category = models.ForeignKey(
        Category, on_delete=models.SET('DELETED'),
        verbose_name='Категория')
    manufacturer = models.CharField(verbose_name='Фирма/Производитель', max_length=200, null=True, blank=True)
    city = models.CharField(verbose_name='Город', max_length=200, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('createReview')


class Review(models.Model):

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'

    title = models.CharField(verbose_name='Заголовок отзыва', max_length=300)
    description = models.TextField(verbose_name='Текст отзыва', max_length=15000)
    published = models.DateTimeField(verbose_name='Дата публикации', auto_now_add=True)
    rating = models.PositiveIntegerField(verbose_name='Рэйтинг')
    author = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE, verbose_name='Автор')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='О чем отзыв?')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('base')
