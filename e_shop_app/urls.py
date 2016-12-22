from django.conf.urls import url

from .views import MainView, CategoryListAPIView


urlpatterns = [
                url(r'main/', MainView.as_view(), name='main_view'),

                url(r'category/list/', CategoryListAPIView.as_view(), name='category_list_view'),

]