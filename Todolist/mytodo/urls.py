from django.urls import path
from . import views

urlpatterns = [
    path('', views.ToDoListView.as_view(), name='todo-list'),
    path('<int:pk>/', views.ToDoItemDetailView.as_view(), name='todo-detail'),

]