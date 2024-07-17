from django.urls import path
from . import views

urlpatterns = [
    path('',views.View1,name='view1')
]