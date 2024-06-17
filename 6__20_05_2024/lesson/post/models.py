from django.db import models


# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(null=True, blank=True)
    description = models.CharField(max_length=255, null=True, blank=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='posts')
    published_date = models.DateField(auto_now_add=True)
    is_published = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.id}. {self.title}"

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = 'Посты'
        ordering = ['id']


class Category(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)

    def __str__(self):
        return f"{self.pk}. {self.name}"

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = 'Категории'
        ordering = ['id']

