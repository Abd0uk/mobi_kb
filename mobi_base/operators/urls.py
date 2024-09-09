from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('<int:pk>', views.operator_detail, name = 'operator_detail'),
]
