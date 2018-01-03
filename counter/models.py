from django.db import models
from datetime import datetime


class CounterName(models.Model):
    title = models.CharField(max_length=250)
    description = models.CharField(max_length=500)
    is_favorite = models.BooleanField(default=False)

    def __str__(self):
        return self.title + ' - ' + self.description


# class Chart(models.Model):
#    CounterName = models.ForeignKey(CounterName, on_delete=models.CASCADE)
#    file_type = models.CharField(max_length=10)


class NetCount(models.Model):
    CounterName = models.ForeignKey(CounterName, on_delete=models.CASCADE)
    numCount = models.IntegerField(default=0)
    time = models.DateTimeField(default=datetime.now())

    def __str__(self):
        return str(self.CounterName.title) + ' = ' + str(self.numCount)
