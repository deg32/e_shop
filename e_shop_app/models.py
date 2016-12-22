from django.db import models


class Category(models.Model):
    """Категория товара"""

    category_name = models.CharField(max_length=30, unique=True)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.category_name


