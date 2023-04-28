from django.db import models
# Create your models here.
class User (models.Model):
    name = models.CharField(max_length=100)
    password= models.CharField(max_length=64)
    email = models.CharField(max_length=100) 
    @property
    def getuser(self):
        return self.name

class ToDoList(models.Model):
    # fk of a user. User ID
    # One to Many 
    id=models.CharField(max_length=2000,primary_key=True)
    todoText = models.CharField(max_length=2000)
    isDone= models.BinaryField()
    User = models.ForeignKey(User,on_delete=models.CASCADE,default=None)
