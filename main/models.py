from django.db import models
from users.models import User

class Reagent(models.Model):
    name = models.CharField(blank=False, max_length=50) 
    synonyms = models.CharField(blank=True, max_length=100) 
    formula = models.CharField(blank=True, max_length=50) 
    CAS = models.CharField(max_length=15) 
    molecular_weight = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(blank=True, upload_to='uploads')

    def __str__(self):
        return self.name

class Batch(models.Model):
    batch_number = models.CharField(blank=False, max_length=10) 
    reagent = models.ForeignKey('Reagent', on_delete=models.CASCADE) 
    quantity = models.DecimalField(max_digits=10, decimal_places=2)
    units = models.CharField(max_length=10) 

    def __str__(self):
        return f'{self.batch_number} | {self.reagent}'

class Tracking(models.Model):
    once_quantity_changed = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    common_quantity_changed = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_timestamp = models.DateTimeField(auto_now_add=True)
    batch = models.ForeignKey('Batch', on_delete=models.CASCADE)

    
    def __str__(self):
        return f'{self.batch.batch_number} | {self.batch.reagent}'


