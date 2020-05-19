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
