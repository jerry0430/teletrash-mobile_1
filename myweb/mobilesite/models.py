from django.db import models

# Create your models here.
class DataInfo(models.Model):
    nums_title = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return nums_title