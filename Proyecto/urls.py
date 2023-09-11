from django.contrib import admin
from django.urls import path

from app1 import views as v1

from app2 import views as v2




urlpatterns = [
    path('admin/', admin.site.urls),
    path("vista1/",v1.vistaUno),
    path('vista2/',v2.vista2),
]
