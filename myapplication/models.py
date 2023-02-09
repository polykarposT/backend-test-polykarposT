from django.db import models


# Create your models here.
class Company(models.Model):
    address_detail = models.CharField(max_length=255)
    city_name = models.CharField(max_length=100)
    display_name = models.CharField(max_length=255, unique=True)
    region_name = models.CharField(max_length=255)
    zip_code = models.CharField(max_length=10)

    def __str__(self):
        return self.display_name

    class Meta:
        verbose_name_plural = "Companies"


class Employee(models.Model):
    email = models.EmailField(max_length=254)
    fullname = models.CharField(max_length=255)
    phoneNumber = models.CharField(max_length=15)
    company_id = models.ForeignKey(Company, on_delete=models.CASCADE)

    def __str__(self):
        return self.fullname


class Offer(models.Model):
    company_id = models.ForeignKey(Company, on_delete=models.CASCADE)
    product_1_budget = models.PositiveIntegerField(null=True, blank=True)
    product_1_issuing_value = models.DecimalField(
        null=True, blank=True, max_digits=4, decimal_places=2
    )
    product_1_mailing_value = models.DecimalField(
        null=True, blank=True, max_digits=4, decimal_places=2
    )
    product_1_value = models.DecimalField(
        null=True, blank=True, max_digits=4, decimal_places=2
    )
    product_2_budget = models.PositiveIntegerField(null=True)
    product_2_issuing_value = models.DecimalField(
        null=True, blank=True, max_digits=4, decimal_places=2
    )
    product_2_mailing_value = models.DecimalField(
        null=True, blank=True, max_digits=4, decimal_places=2
    )
    product_2_value = models.DecimalField(
        null=True, blank=True, max_digits=4, decimal_places=2
    )
    product_3_budget = models.PositiveIntegerField(null=True)
    product_3_issuing_value = models.DecimalField(
        null=True, blank=True, max_digits=4, decimal_places=2
    )
    product_3_mailing_value = models.DecimalField(
        null=True, blank=True, max_digits=4, decimal_places=2
    )
    product_3_value = models.DecimalField(
        null=True, blank=True, max_digits=4, decimal_places=2
    )
