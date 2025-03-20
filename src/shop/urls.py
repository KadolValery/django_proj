from django.urls import path
from shop.views import first_views, second_views,first_html

urlpatterns = [
    path('main_page/path:year', first_views),
    path('second_page/path:year', second_views),
    path('hello/first_html', first_html)
]