from django.db import models


class Skill(models.Model):
    title= models.CharField(max_length=150)
    image= models.ImageField(upload_to= 'skills_added')
    
class Academic(models.Model):
    header= models.CharField(max_length=150)
    title= models.CharField(max_length=150)
    description= models.TextField()
    start_date= models.DateField()
    finished= models.BooleanField()
    finish_date= models.DateField(blank= True, null= True)
    
    class Meta:
        ordering= ['-start_date']