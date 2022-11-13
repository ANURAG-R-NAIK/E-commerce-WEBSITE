from django.urls import path #we also make a urls.py for the shop and add the paths here
from .  import views

urlpatterns = [
    path("",views.index, name="ShopHome")
]