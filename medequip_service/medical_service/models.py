from django.db import models

# Create your models here.
class MedicalService(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=9, decimal_places=2)
    description = models.TextField()
    department_id = models.CharField(max_length=10)
    
    class Meta:
        db_table = "medical_service"