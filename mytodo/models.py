from django.db import models

class Mytodolist(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title
    
class ToDoItem(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField(null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    due_on = models.DateTimeField(null=True)
    todo_list = models.ForeignKey(Mytodolist, on_delete=models.CASCADE)

    def __str__(self):
        return "{self.title}: due {self.due_on}"

