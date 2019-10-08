
from __future__ import unicode_literals


from django.db import models

# Create your models here.
class FibonacciResults(models.Model):

    number = models.IntegerField()
    result = models.CharField(max_length=255)
    time_taken = models.CharField(max_length=255)

    class Meta:
        pass
       # db_table = 'fibonacci_results'

    def __unicode__(self):
        return self.number