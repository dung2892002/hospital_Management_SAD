from django.db import models

# Create your models here.
class Equipment(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    quantity = models.IntegerField()
    department_id = models.CharField(max_length=10)
    
    class Meta:
        db_table = "equipment"