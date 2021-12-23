from django.urls import path
from base import views

app_name = 'base'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('partners/', views.ApplyView.as_view(), name='partners'),
    path('contact/', views.ContactView.as_view(), name='contact'),
]