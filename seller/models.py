from django.db import models

class Seller(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=60)
    birth_date = models.DateField()
    cpf = models.CharField(max_length=14)

    email = models.EmailField()  
    area_code = models.CharField(max_length=3)
    phone_number = models.CharField(max_length=9)
    

    cep = models.CharField(max_length=9)
    country = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    street = models.CharField(max_length=30)
    street_number = models.CharField(max_length=5)

    contracting_date = models.DateTimeField(auto_now_add=True)
    termination_date = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    def get_full_phone_number(self):
        return f"({self.area_code}) {self.phone_number}"

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    def get_full_city(self):
        return f"{self.city} - {self.state}"

    class Meta:
        db_table = "SELLER"