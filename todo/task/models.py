from django.db import models

# Create your models here.
class Tasks(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField(blank= True)
    complete = models.BooleanField(default= False)
    time_created= models.DateTimeField(auto_now_add=True)

    def __str__(self) :
        return self.title