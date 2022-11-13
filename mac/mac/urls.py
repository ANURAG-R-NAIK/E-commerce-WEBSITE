"""mac URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin  #this is our main heard urls.py site
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('shop/',include('shop.urls')), #here we add paths for the shop and mac urls . so when a user comes for mac url 
                                        #he will be directed to the urls of shop and blog and ad the restt operations are followed there
    path('blog/',include('blog.urls'))
]
