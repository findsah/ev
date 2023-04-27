Electric Vehicles
Electric Vehicles is a Django project that provides an infographic to show the percentage split of make + model of electric vehicles. It also has a RESTful API that takes a VIN (value from the first column) as input, performs a search, and provides County, City, and Electric Range as the output when there is a match. When there is no match, the API responds with an error code.

Approach to Building the Electric Vehicles App
Created a Django project and an app called electric_vehicles.
Created the ElectricVehicle model with all the required fields for the data to be loaded.
Wrote a load data script to load data into the database. The script reads the input CSV file, creates ElectricVehicle objects, and commits them to the database. To handle null values in data, empty strings were checked before storing them in the database. An index was also added to the VIN field for faster lookup performance.
Created a view called electric_vehicle_make_model_split to generate the required plot of electric vehicle make count. Also, created a view called electric_vehicle_details to handle the search API. This view takes a VIN as input and returns County, City, and Electric Range if there is a match. If there is no match, it returns an error code.
Created a home view to render the infographic with the electric vehicle make count plot.
Wrote test cases to cover various edge cases of the electric_vehicle_details view, such as the case when a VIN that does not exist in the database is searched.
URLs for the Electric Vehicles App
http://127.0.0.1:8000/ : This is the base URL for the electric vehicles app. It renders the infographic with the electric vehicle make count plot.
http://127.0.0.1:8000/electric_vehicle_make_model_split/ : This URL generates the electric vehicle make count plot.
http://127.0.0.1:8000/electric-vehicles-search/str:vin/ : This URL is for the search API. To test the API, replace str:vin with a VIN that exists in the database. For example, http://127.0.0.1:8000/electric-vehicles-search/5YJ3E1EB4L/
Infographic
To view the infographic, run the Django development server using the command python manage.py runserver and navigate to http://127.0.0.1:8000/.

API Endpoint
electric-vehicles-search/str:vin/ : This endpoint takes a VIN (vehicle identification number) as input and returns County, City, and Electric Range as output when there is a match. When there is no match, the API responds with an error code.

Example: To test the API, run the Django development server using the command python manage.py runserver and navigate to http://127.0.0.1:8000/electric-vehicles-search/5YJ3E1EB4L/.

Performance
To maximize the performance of the search function, an index has been implemented on the vin field of the ElectricVehicle model. This index allows for faster lookup times and improved search performance. Additionally, the query has been optimized to only select the fields required for the response (county, city, and electric_range), reducing the amount of data that needs to be loaded from the database.