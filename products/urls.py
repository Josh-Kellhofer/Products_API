from django.urls import path
from . import views

urlpatterns = [
    path('', views.Product_List.as_view()),
    path('<int:pk>/', views.Product_Detail.as_view()),
]