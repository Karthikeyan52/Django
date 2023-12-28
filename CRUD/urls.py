from django.urls import path, include
from . import views

urlpatterns = [
    path('read/', views.read, name='read'),
    path('update/<int:pk>', views.update, name='update'),
    path('delete/<int:pk>', views.delete, name='delete'),
]
