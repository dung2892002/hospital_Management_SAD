from django.db import models

# Create your models here.
class Medicine(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=9, decimal_places=2)
    description = models.TextField()
    
    class Meta:
        db_table = "medicines"
        
class Supplier(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    
    class Meta:
        db_table = "suppliers"
        
class MedBatch(models.Model):
    id = models.AutoField(primary_key=True)
    medicine = models.ForeignKey(Medicine, on_delete=models.CASCADE)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    sold = models.IntegerField()
    manufacture_date = models.DateField()
    expiration_date = models.DateField()
    received_date = models.DateField()
    
    class Meta:
        db_table = "medicine_batch"
        
    def sell(self, quantity):
        if quantity > 0 and quantity <= self.quantity - self.sold:
            self.sold += quantity
            self.save()
            return True
        return False