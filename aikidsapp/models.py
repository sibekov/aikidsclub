from django.db import models

# Create your models here.


class Item(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    done = models.BooleanField(null=False, blank=False,default=False)
    timer= models.TimeField(null=False, blank=False,default=False)


    def __str__(self):
        return f'{self.name}, status = {self.done},{self.timer}'
        

