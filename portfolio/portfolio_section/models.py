from django.db import models

# Create your models here.


class Project(models.Model):
    title= models.CharField(max_length=150)
    description= models.TextField()
    link= models.URLField(max_length=180)
    image= models.ImageField()
    created_at= models.DateTimeField(auto_now_add= True) #agrega la fecha de creacion automaticamente
    updated_at= models.DateTimeField(auto_now= True) #cambia la fecha cada vez que se modifica el registro
    
    class Meta:
        ordering = ['-created']
    
    def __str__(self):
        return self.title
    
    