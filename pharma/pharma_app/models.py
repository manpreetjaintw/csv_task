from django.db import models


class Pharma(models.Model):
    datum = models.DateField()
    m01ab = models.FloatField()
    m01ae = models.FloatField()
    n02ba = models.FloatField()
    n02be = models.FloatField()
    n05b = models.FloatField()
    n05c = models.FloatField()
    r03 = models.FloatField()
    r06 = models.FloatField()
    year = models.IntegerField()


class Drug(models.Model):
    condition = models.CharField(max_length=100)
    date = models.DateField()
    drugName = models.CharField(max_length=250)
    rating = models.IntegerField()
    review = models.TextField()
    uniqueId = models.IntegerField()
    usefulCount = models.IntegerField()
