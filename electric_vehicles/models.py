from django.db import models

class ElectricVehicle(models.Model):
    vin = models.CharField(max_length=17, primary_key=True)
    county = models.CharField(max_length=500,blank=True, null=True)
    city = models.CharField(max_length=500,blank=True, null=True)
    state = models.CharField(max_length=2,blank=True, null=True)
    postal_code = models.CharField(max_length=10,blank=True, null=True)
    model_year = models.IntegerField(blank=True, null=True)
    make = models.CharField(max_length=500,blank=True, null=True)
    model = models.CharField(max_length=500,blank=True, null=True)
    electric_vehicle_type = models.CharField(max_length=500,blank=True, null=True)
    cafv_eligibility = models.CharField(max_length=500,blank=True, null=True)
    electric_range = models.IntegerField(blank=True, null=True)
    base_msrp = models.IntegerField(blank=True, null=True)
    legislative_district = models.IntegerField(blank=True, null=True)
    dol_vehicle_id = models.IntegerField(blank=True, null=True)
    vehicle_location = models.CharField(max_length=500,blank=True, null=True)
    electric_utility = models.CharField(max_length=500,blank=True, null=True)
    census_tract = models.BigIntegerField(blank=True, null=True)

    def __str__(self):
        return self.vin
