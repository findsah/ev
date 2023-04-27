from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from django.http import JsonResponse
import matplotlib.pyplot as plt
import pandas as pd
from django.db import connection
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from electric_vehicles.models import ElectricVehicle
from electric_vehicles.serializers import ElectricVehicleSerializer

from django.http import HttpResponse
from django.shortcuts import render

from django.db.models import Count
from django.shortcuts import render
import numpy as np

import matplotlib
matplotlib.use('Agg')

import seaborn as sns

from django.urls import reverse
from django.core.files.base import ContentFile
import urllib.request

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from django.shortcuts import render
from electric_vehicles.models import ElectricVehicle
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from django.http import HttpResponse
from django.template import loader
import io
from django.http import HttpResponse
import seaborn as sns
from django.views.decorators.csrf import csrf_exempt
import base64

def home(request):
    # Get the plot image from the electric_vehicle_make_model_split view
    make_model_split_url = request.build_absolute_uri(reverse('electric_vehicle_make_model_split'))
    plot_image = io.BytesIO(urllib.request.urlopen(make_model_split_url).read())

    # Convert image data to base64 encoded string
    plot_image_str = base64.b64encode(plot_image.getvalue()).decode()

    # Render the home page with the plot image in the template context
    context = {'plot_image_str': plot_image_str}
    return render(request, 'infographic.html', context)


@csrf_exempt
def electric_vehicle_make_model_split(request):
    make_model_df = pd.DataFrame(ElectricVehicle.objects.values('make', 'model'))

    # create make count dataframe
    make_counts = make_model_df["make"].value_counts().sort_index()
    make_counts_df = pd.DataFrame(make_counts)

    # create make percentage dataframe
    make_percentage_df = pd.DataFrame(make_counts/len(make_model_df)*100)
    make_percentage_df.columns = ["percentage"]

    # create make-color dictionary
    unique_makes = make_model_df['make'].unique()
    make_color_dict = {make: "C{}".format(i) for i, make in enumerate(unique_makes)}

    # exclude GENESIS from the plot
    make_counts_df[make_counts_df.index != 'GENESIS'].plot(kind="bar", color=[make_color_dict[x] for x in make_counts_df.index if x != 'GENESIS'], legend=None)
    plt.xlabel("Make")
    plt.ylabel("Count")
    plt.title("Electric Vehicle Make Count")
    plt.tight_layout()

    # save figure to a BytesIO object
    fig_bytes = io.BytesIO()
    plt.savefig(fig_bytes, format='png')
    fig_bytes.seek(0)

    # generate the response as a PNG image
    response = HttpResponse(fig_bytes, content_type='image/png')
    return response


@api_view(['GET'])
def electric_vehicle_details(request, vin):
    try:
        ev = ElectricVehicle.objects.filter(vin=vin).values('county', 'city', 'electric_range').first()
        if ev:
            data = {
                "county": ev["county"],
                "city": ev["city"],
                "electric_range": ev["electric_range"]
            }
            return Response(data, status=status.HTTP_200_OK)
        else:
            return Response({"error": f"Electric vehicle with VIN {vin} not found"}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

