from django.db import models

class Room(models.Model):
    id =  models.AutoField(primary_key=True)
    room_type = models.CharField(max_length=255)
    status = models.BooleanField(default=False)
    capacity = models.IntegerField()

    class Meta:
        db_table = "rooms"
    def __str__(self):
        return self.name
    
class Bed(models.Model):
    id =  models.AutoField(primary_key=True)
    status = models.BooleanField(default=False)

    patient_id = models.IntegerField(null=True)
    room_id = models.ForeignKey(Room, on_delete=models.CASCADE)
    
    class Meta:
        db_table = "beds"
    def __str__(self):
        return self.name
