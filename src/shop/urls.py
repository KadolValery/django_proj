from django.urls import path
# from shop.views import first_views, second_views,first_html
from shop.views import home, info, products, users

urlpatterns = [
    path("", home, name="home"),
    path("info", info, name="info"),
    path("products", products, name="products"),
    path("users", users, name="users")
]
#     path('main_page/path:year', first_views),
#     path('second_page/path:year', second_views),
#     path('hello/first_html', first_html)

