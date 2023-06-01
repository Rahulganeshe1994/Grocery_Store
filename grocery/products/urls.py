
from django.urls import path
from products .views import *
urlpatterns = [

    path('products/', ProductView.as_view()),
    path('demo/',DemoView.as_view()),
]
