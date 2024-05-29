from djongo import models


class Fullname(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    class Meta:
        db_table = "fullnames"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Address(models.Model):
    id = models.AutoField(primary_key=True)
    no_house = models.CharField(max_length=10)
    street = models.CharField(max_length=50)
    ward = models.CharField(max_length=50)
    district = models.CharField(max_length=50)
    province = models.CharField(max_length=50)

    class Meta:
        db_table = "addresses"

    def __str__(self):
        return f"{self.no_house}, {self.street}, {self.ward}, {self.district}, {self.province}"

class Blood(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)

    class Meta:
        db_table = "bloods"
        
    def __str__(self):
        return self.name
    
class Patient(models.Model):
    id = models.AutoField(primary_key=True)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=10, choices=[('male', 'Male'), ('female', 'Female')])
    mobile_number = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    allergies = models.TextField(blank=True, null=True)
    medical_history = models.TextField(blank=True, null=True)

    fullname = models.ForeignKey(Fullname, on_delete=models.CASCADE)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    blood = models.ForeignKey(Blood, on_delete=models.CASCADE)
    class Meta:
        db_table = "patients"

    def __str__(self):
        return f"{self.fullname.first_name} {self.fullname.last_name} - {self.mobile_number}"
