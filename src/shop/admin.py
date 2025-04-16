from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from authentication.models import CustomUser



from shop.models import (
    Order,
    ProductDetail,
    Provider,
    ProductOrder,
    Feedback,
    Product

)

admin.site.register(Order)
admin.site.register(ProductDetail)
admin.site.register(Provider)
admin.site.register(ProductOrder)
admin.site.register(Feedback)
admin.site.register(Product)

