# from django.db import models

# # Create your models here.
# class TestData(models.Model):
#     testname = models.CharField(max_length=100)
#     testvalue = models.IntegerField()

from django.db import models

class Word(models.Model):
    word = models.CharField(max_length=255)

    def __str__(self):
        return self.word
