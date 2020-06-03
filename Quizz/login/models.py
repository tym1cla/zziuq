from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
from category.models import Geography, Entertainment, History, Literature, Science, Sport
import operator

gender = (
    ('mężczyzna', "♂"),
    ('kobieta', "♀"),
)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    sex = models.CharField(max_length=32, choices=gender, default="♀")
    score = models.IntegerField(default=0)
    creation_date = models.DateField(default=now)
    geography = models.ManyToManyField(Geography)
    entertainment = models.ManyToManyField(Entertainment)
    history = models.ManyToManyField(History)
    literature = models.ManyToManyField(Literature)
    science = models.ManyToManyField(Science)
    sport = models.ManyToManyField(Sport)

    def __str__(self):
        return str(self.user)

    objects = models.Manager()
