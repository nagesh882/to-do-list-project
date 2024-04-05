from django.db import models

# I have created model class for creating database table 

class ToDoList(models.Model):

    title = models.CharField(max_length=255, default=None, null=False)
    descripton = models.TextField(default=None, null=False)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title