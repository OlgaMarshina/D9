from django.db import models
from django.contrib.auth.models import User

from django.core.validators import MinValueValidator
from django.db.models import Sum
from django.urls import reverse


class Author(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, verbose_name='Имя')
    rating = models.IntegerField(default=0.0)


class Category(models.Model):
    name = models.CharField(unique = True, max_length=255, verbose_name='Категории' )
    subscribers = models.ManyToManyField(User, blank=True, null=True, related_name='Подписчики')

    def subscribe(self):
        pass

    def get_category(self):
        return self.name

    def __str__(self):
        return self.name


class Post(models.Model):
    news = 'NE'
    article = 'AR'

    POST_TYPES = [
        (news, 'Новость'),
        (article, 'Статья')
    ]
    author = models.CharField(max_length=255, default='Default author', verbose_name='имя автора')
    post_type = models.CharField(max_length=2, choices=POST_TYPES, default=article, verbose_name='Вид поста')
    date_create = models.DateTimeField(auto_now_add=True, verbose_name='дата и время создания')
    date_update = models.DateTimeField(auto_now=True, verbose_name='дата и время изменения')
    categories = models.ManyToManyField(Category, verbose_name='Категории')
    title = models.CharField(max_length=255, default='Default title', verbose_name='заголовок')
    content = models.TextField(default='Default content', verbose_name='текст')

    def __str__(self):
        return f'{self.title}: {self.date_create.strftime("%d-%m-%Y, %H:%M:%S")}: {self.content[:20]}'

    def get_absolute_url(self):
        return reverse('news')


class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete = models.CASCADE, verbose_name='Пост')
    category = models.ForeignKey(Category, on_delete = models.CASCADE, verbose_name='Категории')


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete = models.CASCADE, verbose_name='Пост')
    user = models.ForeignKey(User, on_delete = models.CASCADE, verbose_name='Пользователь')
    text_comment = models.TextField(default = 'Default comment', verbose_name='текст комментария' )
    datetime_create = models.DateTimeField(auto_now_add=True, verbose_name='дата и время создания комментария')
    rating = models.IntegerField(default=0.0)
