from django.contrib import admin
from .models import Company, Employee, Offer

# Register your models here.
admin.site.register(Company)
admin.site.register(Employee)
admin.site.register(Offer)
