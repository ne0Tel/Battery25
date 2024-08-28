import requests

from battery_core.celery import app
from .models import ExternalReviewsModel
from .reviews import gis_reviews, vl_reviews, parse_youtube


@app.task
def get_reviews_from_2gis():
    gis_data = gis_reviews()
    gis_obj = ExternalReviewsModel.objects.get(title='2GIS')
    gis_obj.rate = float(gis_data.get('rating'))
    gis_obj.reviews_count = int(gis_data.get('count'))

    gis_obj.save()

@app.task
def get_reviews_from_vl_ru():
    vl_data = vl_reviews()
    vl_obj = ExternalReviewsModel.objects.get(title='VL.RU')
    vl_obj.rate = float(vl_data.get('rating'))
    vl_obj.reviews_count = int(vl_data.get('count'))

    vl_obj.save()

@app.task
def get_data_from_youtube():
    parse_youtube()
