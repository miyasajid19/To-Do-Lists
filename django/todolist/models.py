from django.db import models

# Create your models here.
class Todolist(models.Model):
    text=models.CharField(max_length=1000)
    completed=models.BooleanField(default=False)
    
    def __str__(self) -> str:
        return self.text