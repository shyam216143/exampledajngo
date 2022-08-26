from django.db import models

# Create your models here.

#DataFlair #DjangoTutorials
# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=255)

class Vehicle(models.Model):
    name = models.CharField(max_length=255)
    customer = models.OneToOneField(
        Customer,
        on_delete=models.CASCADE,
        related_name='vehicle'
    )




class fruits(models.Model):
        fruit_name = models.CharField(max_length=100)
        price = models.IntegerField()
        manufacturer_date =models.DateField()
        fruite_discription = models.TextField()
        is_fresh = models.BooleanField(default=True)


        def __str__(self) -> str:
             return self.fruit_name 



        class Meta:
            db_table = 'home_fruits'
            verbose_name = "home_fruits"
            ordering = ['-fruit_name']       
            unique_together = [['fruit_name', 'price']]
