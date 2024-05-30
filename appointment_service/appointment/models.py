from django.db import models

# Create your models here.
class Appointment(models.Model):
    id = models.AutoField(primary_key=True)
    doctor_id = models.CharField(max_length=10)
    patient_id = models.CharField(max_length=10, default=0)
    date = models.DateField()
    time = models.CharField(max_length=20, choices=[('morning', 'Morning'), ('noon', 'Noon'), ('afternoon', 'Afternoon'), ('night', 'Night')])
    description = models.CharField(max_length=1000)
    status = models.CharField(max_length=50, choices=[('scheduled', 'Scheduled'), ('completed', 'Completed'), ('cancelled', 'Cancelled')])
    
    class Meta:
        db_table = "appointments"