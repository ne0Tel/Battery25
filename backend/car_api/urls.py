from django.urls import path
from .views import *
from .rest_api import *

rest_patterns = [
    path('api/delivery', DeliveryAPI.as_view()),
    path('api/get_by_price', FilterAutoByPrice.as_view()),
    path('api/feedback', FeedbackFormAPI.as_view()),
    path('api/get_models', GetUniqueModels.as_view())
]


urlpatterns = [
    path('main/', MainPageView.as_view()),
    path('catalog/', CarsJapan.as_view()),
    path('card/', card, name="card"),
    path('shipping_calculator/', shipping_calculator, name="shipping_calculator"),
    path('feedback_form/', feedback_form, name="feedback_form"),
    path('similar_cars/' , similar_cars, name="similar_cars")
] + rest_patterns
