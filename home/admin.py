from django.contrib import admin

# Register your models here.
from .models import Customer, Vehicle, fruits
#data fair
admin.site.register(Customer)
admin.site.register(Vehicle)
admin.site.register(fruits)     