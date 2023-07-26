from django.contrib import admin
from mytodo.models import Mytodolist,ToDoItem

admin.site.register(Mytodolist)
admin.site.register(ToDoItem)