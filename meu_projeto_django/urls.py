from django.contrib import admin
from django.urls import path
from api.views import update_dados

urlpatterns = [
    path('admin/', admin.site.urls), # O erro estava aqui (.urls em vez de .path)
    path('api/update/', update_dados),
]
