from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from django.views.generic import TemplateView
from .forms import FeedbackForm, CarJapanFilterForm
from .models import MainPageCarsModel, ContactsModel, MainPagePosterModel, YouTubePlaylistsModel
from .base_views import FilteredCarListView

class MainPageView(TemplateView):

    def build_youtube_list(self):
        yt_reviews = []

        yt_playlist_main_1 = YouTubePlaylistsModel.objects.get(name='СВЕЖИЙ ПРИВОЗ')
        yt_playlist_main_2 = YouTubePlaylistsModel.objects.get(name='Обзоры авто из Японии, Кореи, Китая')
        yt_playlist_reviews = YouTubePlaylistsModel.objects.get(name='Батарейка 25rus отзывы')
        yt_playlist_shorts = YouTubePlaylistsModel.objects.get(name='shorts #shorts')

        for i in range(0, max(yt_playlist_main_1.videos.count(), yt_playlist_main_2.videos.count())):
            if i < yt_playlist_main_1.videos.count():
                yt_reviews.append(yt_playlist_main_1.videos.all()[i])
            if i < yt_playlist_main_2.videos.count():
                yt_reviews.append(yt_playlist_main_2.videos.all()[i])

        for obj in yt_playlist_reviews.videos.all():
            yt_reviews.append(obj)

        yt_shorts = [obj for obj in yt_playlist_shorts.videos.all()]

        return yt_reviews, yt_shorts

    def get(self, request):
        contacts = get_object_or_404(ContactsModel)
        poster = get_object_or_404(MainPagePosterModel)
        feedback_form = FeedbackForm()
        japan = MainPageCarsModel.objects.filter(country=1)
        korea = MainPageCarsModel.objects.filter(country=2)
        europe = MainPageCarsModel.objects.filter(country=4)
        china = MainPageCarsModel.objects.filter(country=3)
        yt_reviews, yt_shorts = self.build_youtube_list()

        return render(request, 'templates/main/main.html',
                      context={'japan': japan, 'korea': korea, 'europe': europe,
                               'china': china, 'contacts': contacts, 'poster': poster,
                               'feedBackForm': feedback_form, 'yt_reviews': yt_reviews, 'yt_shorts': yt_shorts})
    

class CarsJapan(FilteredCarListView):
    form_filter = CarJapanFilterForm
    link_url = "car_list_japan"
    title = "Авто из Японии"
    car_link = "car_japan"
    url_api = "/api/cars/china/"
