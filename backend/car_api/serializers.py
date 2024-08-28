from rest_framework import serializers
from .models import DeliveryModel, MainPageCarsModel, CountryModel, PhotoCarsModel, BodyTypeModel

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = CountryModel
        fields = ['country_name']

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhotoCarsModel
        fields = ['image']

class BodyTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = BodyTypeModel
        fields = ['name']

class DeliverySerializer(serializers.ModelSerializer):
    class Meta:
        model = DeliveryModel
        fields = ['price', 'path_time']

class MainPageCarsSerializer(serializers.ModelSerializer):
    country = serializers.CharField(source='country.country_name')
    img = ImageSerializer(many=True, read_only=True)
    body_type = serializers.CharField(source='body_type.name')

    def to_representation(self, instance):
        representation = super().to_representation(instance)

        if representation['img']:
            representation['img'] = representation['img'][0]['image']
        else:
            representation['img'] = None
        return representation

    class Meta:
        model = MainPageCarsModel
        fields = '__all__'
