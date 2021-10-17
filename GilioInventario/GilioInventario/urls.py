from django.contrib import admin
from django.urls import path

from GilioInventario import views


urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.login, name="login"),
    
]
