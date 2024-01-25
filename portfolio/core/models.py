from django.db import models

class Skill(models.Model):
    title= models.CharField(max_length=150)
    image= models.ImageField(upload_to= 'skills_added')
    