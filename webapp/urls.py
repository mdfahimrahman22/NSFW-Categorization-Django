from django.urls import path
from webapp import views
urlpatterns = [
    path('', views.home,name='index'),
    path('home', views.home,name='home'),
]