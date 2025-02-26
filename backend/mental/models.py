from django.db import models

# Create your models here.
class Blog(models.Model): 
    title = models.CharField(max_length=200)
    content= models.TextField()
    like = models.IntegerField(default=0) 
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


   
