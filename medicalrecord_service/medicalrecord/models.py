from django.db import models

class MedicalRecord(models.Model):
    id =  models.AutoField(primary_key=True)
    patient_id = models.IntegerField()
    doctor_id = models.IntegerField()
    diagnosis = models.CharField(max_length=1000) # chuẩn đoán
    treatment = models.CharField(max_length=1000) # điều trị
    notes = models.CharField(max_length=2000)
    

    class Meta:
        db_table = "medicalrecord"
    def __str__(self):
        return self.name
