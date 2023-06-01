from django.contrib import admin
from products .models import *


# Register your models here.

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(QuantityVariant)
admin.site.register(Color_variant)
admin.site.register(SizeVariant)
admin.site.register(ProductImages)
