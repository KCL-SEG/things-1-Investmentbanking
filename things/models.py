from django.db import models

# Create your models here.

class Thing(models):
    name = models.CharField(

    )

    description = models.CharField(

    )

    quantity = models.IntegerField(
        
    )
