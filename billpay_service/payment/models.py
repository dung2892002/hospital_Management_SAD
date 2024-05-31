from django.db import models
from bill.models import Bill

class Payment(models.Model):
    id = models.AutoField(primary_key=True)
    bill = models.ForeignKey(Bill, related_name='payments', on_delete=models.CASCADE)
    payment_amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateField(auto_now_add=True)

    class Meta:
        db_table = "payments"
    
    def __str__(self):
        return f"Payment {self.id} - Bill ID: {self.bill.id} - Amount: {self.payment_amount} - Status: {self.status}"
