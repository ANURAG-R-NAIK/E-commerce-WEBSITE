from django.urls import path #we here make a urls.py site for blog and will add all the paths down here
from .  import views

urlpatterns = [
    path("",views.index, name="BlogHome")
]