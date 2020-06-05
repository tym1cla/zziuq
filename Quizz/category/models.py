from django.db import models


class Geography(models.Model):
    question = models.CharField(max_length=1000)
    answer_1 = models.CharField(max_length=256)
    answer_2 = models.CharField(max_length=256)
    answer_3 = models.CharField(max_length=256)
    answer_4 = models.CharField(max_length=256)
    correct_answer = models.IntegerField(default=0)

    def __str__(self):
        return str(self.pk)

    objects = models.Manager()


class Entertainment(models.Model):
    question = models.CharField(max_length=1000)
    answer_1 = models.CharField(max_length=256)
    answer_2 = models.CharField(max_length=256)
    answer_3 = models.CharField(max_length=256)
    answer_4 = models.CharField(max_length=256)
    correct_answer = models.IntegerField(default=0)

    def __str__(self):
        return str(self.pk)

    objects = models.Manager()


class History(models.Model):
    question = models.CharField(max_length=1000)
    answer_1 = models.CharField(max_length=256)
    answer_2 = models.CharField(max_length=256)
    answer_3 = models.CharField(max_length=256)
    answer_4 = models.CharField(max_length=256)
    correct_answer = models.IntegerField(default=0)

    def __str__(self):
        return str(self.pk)

    objects = models.Manager()


class Literature(models.Model):
    question = models.CharField(max_length=1000)
    answer_1 = models.CharField(max_length=256)
    answer_2 = models.CharField(max_length=256)
    answer_3 = models.CharField(max_length=256)
    answer_4 = models.CharField(max_length=256)
    correct_answer = models.IntegerField(default=0)

    def __str__(self):
        return str(self.pk)

    objects = models.Manager()


class Science(models.Model):
    question = models.CharField(max_length=1000)
    answer_1 = models.CharField(max_length=256)
    answer_2 = models.CharField(max_length=256)
    answer_3 = models.CharField(max_length=256)
    answer_4 = models.CharField(max_length=256)
    correct_answer = models.IntegerField(default=0)

    def __str__(self):
        return str(self.pk)

    objects = models.Manager()


class Sport(models.Model):
    question = models.CharField(max_length=1000)
    answer_1 = models.CharField(max_length=256)
    answer_2 = models.CharField(max_length=256)
    answer_3 = models.CharField(max_length=256)
    answer_4 = models.CharField(max_length=256)
    correct_answer = models.IntegerField(default=0)

    def __str__(self):
        return str(self.pk)

    objects = models.Manager()
