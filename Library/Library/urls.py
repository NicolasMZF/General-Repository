from django.contrib import admin
from django.urls import path, include
from Clients import views as client_views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('Clients/',include('Clients.urls')),
    path('', client_views.View1,name='index')
]
