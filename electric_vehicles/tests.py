from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from electric_vehicles.models import ElectricVehicle

class ElectricVehicleDetailsTestCase(TestCase):
    
    def setUp(self):
        self.client = APIClient()
        # create some electric vehicle objects for testing
        ElectricVehicle.objects.create(vin='11111111111111111', county='test county', city='test city', state='WA', postal_code='12345', model_year=2022, make='test make', model='test model', electric_vehicle_type='BEV', cafv_eligibility='Eligible', electric_range=300, base_msrp=None, legislative_district=37, dol_vehicle_id=1111, vehicle_location='test location', electric_utility='test utility', census_tract=1234)
        ElectricVehicle.objects.create(vin='22222222222222222', county='test county', city='test city', state='WA', postal_code='12345', model_year=2022, make='test make', model='test model', electric_vehicle_type='BEV', cafv_eligibility='Eligible', electric_range=300, base_msrp=None, legislative_district=None, dol_vehicle_id=1111, vehicle_location='test location', electric_utility='test utility', census_tract=None)
    
    def test_electric_vehicle_details_success(self):
        # test case for successful search with existing VIN
        response = self.client.get('/electric-vehicles-search/11111111111111111/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {'county': 'test county', 'city': 'test city', 'electric_range': 300})
    
    def test_electric_vehicle_details_failure(self):
        # test case for search with non-existing VIN
        response = self.client.get('/electric-vehicles-search/123456789/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(response.data, {'error': 'Electric vehicle with VIN 123456789 not found'})
    
    def test_electric_vehicle_details_null_fields(self):
        # test case for search with VIN that has some null fields
        response = self.client.get('/electric-vehicles-search/22222222222222222/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {'county': 'test county', 'city': 'test city', 'electric_range': 300})
