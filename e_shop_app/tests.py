from django.test import TestCase
from django.test import Client
from django.urls import resolve, reverse

from .models import Category


class TestURLs(TestCase):
    """Тестирование urls"""

    client = Client()

    def test_MainView_url(self):
        """Тестирование url главной страницы"""

        code = self.client.get('/shop/main/').status_code

        resolver = resolve('/shop/main/')

        reverser = reverse('main_view')

        self.assertEqual(code, 200)

        self.assertEqual(resolver.func.__name__, 'MainView')

        self.assertEqual(resolver.view_name, 'main_view')

        self.assertEqual(resolver.url_name, 'main_view')

        self.assertEqual(reverser, '/shop/main/')

    def test_CategoryListAPIView_url(self):
        """Тестирование url API вывода списка категорий товаров"""

        code = self.client.get('/shop/category/list/').status_code

        resolver = resolve('/shop/category/list/')

        reverser = reverse('category_list_view')

        self.assertEqual(code, 200)

        self.assertEqual(resolver.func.__name__, 'CategoryListAPIView')

        self.assertEqual(resolver.view_name, 'category_list_view')

        self.assertEqual(resolver.url_name, 'category_list_view')

        self.assertEqual(reverser, '/shop/category/list/')


class TestModels(TestCase):
    """Тестирование моделей"""

    def test_category_create(self):
        """Тестирование создания новой категории товаров"""

        Category(category_name="category").save()

        Category(category_name="category2").save()

        Category(category_name="category3").save()

        self.assertEqual(Category.objects.all().count(), 3)

        Category(category_name="category4").save()

        self.assertEqual(Category.objects.all().count(), 4)
