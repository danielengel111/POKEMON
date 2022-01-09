from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator, MaxLengthValidator,MinLengthValidator

# Create your models here.


class Pokemon(models.Model):
    Name = models.CharField(validators=[MaxLengthValidator(50),MinLengthValidator(2)], primary_key=True)
    Type = models.CharField(max_length=50)
    Generation = models.IntegerField(validators=[MaxValueValidator(6),MinValueValidator(1)])
    Legendary = models.BooleanField()
    Hp = models.IntegerField(validators=[MaxValueValidator(300),MinValueValidator(1)])
    Attack=models.IntegerField(validators=[MaxValueValidator(300),MinValueValidator(1)])
    Defense = models.IntegerField(validators=[MaxValueValidator(300),MinValueValidator(1)])