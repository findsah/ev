import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'electricvehicles.settings')

import django
django.setup()

import sys

# add the path to your Django project in the sys.path list
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

# set the DJANGO_SETTINGS_MODULE environment variable

import csv
import psycopg2
from psycopg2.extras import execute_values
from electric_vehicles.models import ElectricVehicle

# Database connection settings
db_name = "electricvehicles"
db_user = "postgres"
db_password = "ilfaz786"
db_host = "localhost"
db_port = "5432"

# Connect to the database
conn = psycopg2.connect(
    dbname=db_name,
    user=db_user,
    password=db_password,
    host=db_host,
    port=db_port
)


# Read the input CSV file
# Read the input CSV file
with open('ev.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader)  # skip header row

    for row in reader:
        vin = row[0]
        ev, created = ElectricVehicle.objects.get_or_create(
            vin=vin,
            defaults={
                'county': row[1],
                'city': row[2],
                'state': row[3],
                'postal_code': row[4],
                'model_year': int(row[5]),
                'make': row[6],
                'model': row[7],
                'electric_vehicle_type': row[8],
                'cafv_eligibility': row[9],
                'electric_range': int(row[10]),
                'base_msrp': int(row[11]) if row[11] != '' else None,
                'legislative_district': int(row[12]) if row[12] != '' else None,
                'dol_vehicle_id': int(row[13]),
                'vehicle_location': row[15],
                'electric_utility': row[16],
                'census_tract': int(row[17]) if len(row) > 17 and row[17] != '' else None
            }
        )

# Add an index to the VIN field for faster lookup performance
with conn.cursor() as cur:
    cur.execute("CREATE INDEX electric_vehicle_vin_idx ON electric_vehicles_electricvehicle (vin)")

# Commit the changes to the database and close the connection
conn.commit()
conn.close()
