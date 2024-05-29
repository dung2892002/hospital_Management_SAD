from djongo import models


class Department(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, null=False)
    
    class Meta:
        db_table = "departments"

    def __str__(self):
        return self.name
    
class Position(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, null=False)
    
    class Meta:
        db_table = "positions"

    def __str__(self):
        return self.name
    
class Degree(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, null=False)
    
    class Meta:
        db_table = "degrees"

    def __str__(self):
        return self.name

class Fullname(models.Model):
    id= models.AutoField(primary_key=True)
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

class Doctor(models.Model):
    id = models.AutoField(primary_key=True)
    mobile_number = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    
    fullname = models.ForeignKey(Fullname, on_delete=models.CASCADE)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    position = models.ForeignKey(Position, on_delete=models.CASCADE)
    degree = models.ForeignKey(Degree, on_delete=models.CASCADE)
    
    class Meta:
        db_table = "doctors"
        
    def __str__(self):
        return f"{self.fullname.first_name} {self.fullname.last_name} - {self.email}"