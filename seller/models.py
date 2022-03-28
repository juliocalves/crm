from django.db import models

class Seller(models.Model):
    first_name = models.CharField(max_length=30, blank=False)
    last_name = models.CharField(max_length=60, blank=False)
    birth_date = models.DateField(blank=False)
    cpf = models.CharField(max_length=14, blank=False)

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


    # id_customer = models.ForeignKey(Customer, blank=True, on_delete=models.CASCADE )

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