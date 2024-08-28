from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Q
from django.shortcuts import get_list_or_404
from .models import DeliveryModel, CityModel, BodyTypeModel, CountryModel, MainPageCarsModel, AutoMarkaModel
from .serializers import DeliverySerializer, MainPageCarsSerializer
from .forms import FeedbackForm

class DeliveryAPI(APIView):
    def post(self, request):
        body_type = request.data.get('bodyType')
        city = request.data.get('city')

        body_type_obj = BodyTypeModel.objects.get(name=body_type)
        city_obj = CityModel.objects.get(name=city)

        delivery_obj = DeliveryModel.objects.get(city=city_obj, body_type=body_type_obj)
        serializer = DeliverySerializer(delivery_obj)

        return Response(serializer.data, status=status.HTTP_200_OK)
    

class FilterAutoByPrice(APIView):

    _price_cats = {
        'car-500k': 500000,
        'car-600k': 600000,
        'car-1kk': 1000000,
        'car-2kk': 2000000,
        'car-3kk': 3000000,
        'car-4kk': 4000000,
        'car-5kk': 5000000
    }

    def post(self, request):
        price_cat = request.data.get('price_cat')
        price = self._price_cats.get(price_cat)

        country = request.data.get('country')
        country_obj = CountryModel.objects.get(country_name=country)

        cars_objects = get_list_or_404(MainPageCarsModel, price__lt=price, country=country_obj)
        serialized_cars = MainPageCarsSerializer(cars_objects, many=True)

        return Response(data={f'{price_cat}': serialized_cars.data})
    

class FeedbackFormAPI(APIView):
    def post(self, request):
        form = FeedbackForm(request.data)

        if form.is_valid():
            return Response(data={'success': 'Form is valid'}, status=status.HTTP_200_OK)
        return Response(data={'error': 'Form isnt valid'},
                        status=status.HTTP_422_UNPROCESSABLE_ENTITY)
    

class GetUniqueModels(APIView):
    def get(self, request):
        marka_name = request.GET.get('marka_name')
        model_names = [model_obj.model_name for model_obj in AutoMarkaModel.objects.filter(marka_name=marka_name)]
        return Response(data={"data": model_names}, status=status.HTTP_200_OK)
