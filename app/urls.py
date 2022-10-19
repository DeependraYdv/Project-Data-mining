from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('dictionary/', views.dictionary, name='dictionary'),
    path('news/', views.news, name='news'),
    path('flipkart/', views.ecommerce, name='flipkart'),
    path('contact/', views.contact, name='contact'),
]


