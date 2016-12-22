from django.shortcuts import render
from django.views.generic import TemplateView
from rest_framework.generics import ListAPIView

from .models import Category
from .serializers import CategorySerializer

class MainView(TemplateView):
    """Отображение главной страницы магазина"""

    template_name = 'e_shop_app/index.html'


class CategoryListAPIView(ListAPIView):
    """Вывод сериализованного списка всех категории товаров"""

    serializer_class = CategorySerializer

    queryset = Category.objects.all()





