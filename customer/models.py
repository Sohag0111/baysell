from django.db import models

class User_Ifo(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    email = models.EmailField()
    is_married = models.BooleanField()
    birthda = models.DateField()
    birth_time = models.TimeField(auto_now_add=True)
    bio = models.TextField(max_length=150)



