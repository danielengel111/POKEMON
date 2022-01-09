from django.db import models

# Create your models here.

class Pokemon(models.Model):
    Name=models.Charfield(max_length=50,min_length=2,primary_key=True)
    Type=models.Charfield(max_length=50)
    Generation =models.Intfield(max_int=6,min_int=1)
    Legendary=models.Booleanfield()
    Hp=models.Intfield(max_int=300,min_int=1)
    Attack=models.Intfield(max_int=300,min_int=1)
    Defense = models.Intfield(max_int=300, min_int=1)