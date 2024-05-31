from django.db import models

class Bill(models.Model):
    id = models.AutoField(primary_key=True)
    patient_id = models.IntegerField()
    created_date = models.DateTimeField(auto_now_add=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        db_table = "bills"
    
    def __str__(self):
        return f"Bill {self.id} - Patient ID: {self.patient_id}"

class BillMedicine(models.Model):
    id = models.AutoField(primary_key=True)
    medicine_id = models.CharField(max_length=10)
    quantity = models.IntegerField()
    bill = models.ForeignKey(Bill, related_name='medicines', on_delete=models.CASCADE)

    class Meta:
        db_table = "medicine_bills"
        
    def __str__(self):
        return f"Medicine ID: {self.medicine_id} x {self.quantity}"

class BillMedicalService(models.Model):
    id = models.AutoField(primary_key=True)
    medical_service_id = models.IntegerField()
    quantity = models.IntegerField() 
    bill = models.ForeignKey(Bill, related_name='services', on_delete=models.CASCADE)

    class Meta:
        db_table = "medical_service_bills"
    
    def __str__(self):
        return f"Service ID: {self.medical_service_id} x {self.quantity}"
