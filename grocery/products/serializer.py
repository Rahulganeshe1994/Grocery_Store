from rest_framework import serializers
from products .models import  *
from products .serializer import *


class ProductSerializer(serializers.ModelSerializer):
    #quantity_type = QuantityVariantSerializer(many =True)
    class Meta:
        model = Product
        fields = "__all__"
        #exclude = ['id',]
        


# class QuantityVariantSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = QuantityVariant
#         field = ['variant_name']
    