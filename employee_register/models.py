from django.db import models

# Create your models here.
class Position(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
class Assets(models.Model):
    year_of_purchase = models.IntegerField()
    historical_cost = models.DecimalField(max_digits=50, decimal_places=2)
    purchase_order = models.IntegerField()
    user = models.CharField(max_length=100)
    location = models.CharField(max_length=500)
    specification = models.CharField(max_length=500)
    rate = models.DecimalField(max_digits=50, decimal_places=2)
    accumulated_balance = models.DecimalField(max_digits=50, decimal_places=2)
    book_value = models.DecimalField(max_digits=50, decimal_places=2)
    
    bookValue = models.DecimalField(max_digits=50, decimal_places=2)
    service = models.IntegerField()
    fromYear = models.IntegerField()
    result = models.DecimalField(max_digits=50, decimal_places=2)

    
    
    
    
    position = models.ForeignKey(Position,on_delete=models.CASCADE)
