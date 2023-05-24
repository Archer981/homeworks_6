from django.db import models
from django.shortcuts import get_object_or_404

from users.models import User


class Ad(models.Model):
    name = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    price = models.IntegerField()
    description = models.TextField()
    is_published = models.BooleanField()
    image = models.ImageField(upload_to='ad_image', blank=True, null=True)
    category = models.ForeignKey('ads.Category', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'
        ordering = ['-price']

    def __str__(self):
        return self.name

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'author': self.author_id,
            # 'author': get_object_or_404(User, pk=self.category_id).username,
            'price': self.price,
            'description': self.description,
            'is_published': self.is_published,
            'image': self.image.url if self.image else None,
            'category': self.category_id,
            # 'category': get_object_or_404(Category, pk=self.category_id).name,
        }


class Category(models.Model):
    name = models.CharField(max_length=200)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
        }
