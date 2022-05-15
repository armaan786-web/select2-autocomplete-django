from django.db import models

# Create your models here.

class displaydd1(models.Model):
    colorname = models.CharField(max_length=100)

    def __str__(self):
        return self.colorname
    
    class Meta:
        db_table = "colors"
