
from django.urls import path
from . import views

app_name = 'ariapp'
urlpatterns = [
    path('', views.index, name='index'),
    path('calculate_ari/', views.calculate_ari, name='calculate_ari'),
    path('delete/<int:book_id>/', views.delete_book, name='delete_book')
]
