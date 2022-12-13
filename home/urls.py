from django.urls import path
from . import views

urlpatterns = [
    path('home', views.home, name='home'),
    path('detail/<slug:pk>', views.details, name='details'),

]
