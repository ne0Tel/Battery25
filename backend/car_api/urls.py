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
    path('catalog/', CarsJapan.as_view())
] + rest_patterns
