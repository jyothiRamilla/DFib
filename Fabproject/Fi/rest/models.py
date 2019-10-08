from django.db import models

# Create your models here.
class emp(models.Model):
    fn=models.CharField(max_length=10)
    ln=models.CharField(max_length=10)
    emp_id=models.IntegerField()
    def __str__(self):
        return self.fn