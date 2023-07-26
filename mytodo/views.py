from django.views.generic import ListView, DetailView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import ToDoItem
from .serializers import ToDoItemSerializer

class ToDoListView(ListView):
    model = ToDoItem
    template_name = 'todolist.html'
    context_object_name = 'todo_items'

class ToDoItemDetailView(DetailView):
    model = ToDoItem
    template_name = 'todoitem.html'
    context_object_name = 'todo_item'

class ToDoItemListCreateView(ListCreateAPIView):
    queryset = ToDoItem.objects.all()
    serializer_class = ToDoItemSerializer

class ToDoItemRetrieveUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    queryset = ToDoItem.objects.all()
    serializer_class = ToDoItemSerializer
