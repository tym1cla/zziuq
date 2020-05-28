from django.db import models


# Create your models here.


class User(models.Model):
    gender = (
        ('mężczyzna', "♂"),
        ('kobieta', "♀"),
    )
    name = models.CharField(max_length=128, unique=True)
    password = models.CharField(max_length=25)
    email = models.EmailField(unique=True)
    sex = models.CharField(max_length=32, choices=gender, default="♀")
    c_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["-c_time"]
        verbose_name = "użytkownik"
        verbose_name_plural = "użytkownik"


class Biology(models.Model):
    question=models.CharField(max_length=1000)
    a_1=models.CharField(max_length=256)
    a_2 = models.CharField(max_length=256)
    a_3 = models.CharField(max_length=256)
    a_4 = models.CharField(max_length=256)
    correct= models.CharField(max_length=8)

class Entertainment(models.Model):
    question=models.CharField(max_length=1000)
    a_1=models.CharField(max_length=256)
    a_2 = models.CharField(max_length=256)
    a_3 = models.CharField(max_length=256)
    a_4 = models.CharField(max_length=256)
    correct= models.CharField(max_length=8)

class History(models.Model):
    question=models.CharField(max_length=1000)
    a_1=models.CharField(max_length=256)
    a_2 = models.CharField(max_length=256)
    a_3 = models.CharField(max_length=256)
    a_4 = models.CharField(max_length=256)
    correct= models.CharField(max_length=8)

class Literature(models.Model):
    question=models.CharField(max_length=1000)
    a_1=models.CharField(max_length=256)
    a_2 = models.CharField(max_length=256)
    a_3 = models.CharField(max_length=256)
    a_4 = models.CharField(max_length=256)
    correct= models.CharField(max_length=8)

class Science(models.Model):
    question=models.CharField(max_length=1000)
    a_1=models.CharField(max_length=256)
    a_2 = models.CharField(max_length=256)
    a_3 = models.CharField(max_length=256)
    a_4 = models.CharField(max_length=256)
    correct= models.CharField(max_length=8)

class Sport(models.Model):
    question=models.CharField(max_length=1000)
    a_1=models.CharField(max_length=256)
    a_2 = models.CharField(max_length=256)
    a_3 = models.CharField(max_length=256)
    a_4 = models.CharField(max_length=256)
    correct= models.CharField(max_length=8)

 
        
