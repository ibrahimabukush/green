from django.db import models
       
class Signnup(models.Model):
    name = models.CharField(max_length=50)
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    def __str__(self) :
        return self.name

class Contact(models.Model):
    name= models.CharField(max_length=30)
    email= models.CharField(max_length=50)
    report=models.CharField(max_length=2048)
    def __str__(self):
        return self.name
    