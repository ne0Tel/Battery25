from django.contrib import admin
from .models import *

@admin.register(ContactsModel)
class ContactsModelAdmin(admin.ModelAdmin):
    pass

@admin.register(MainPagePosterModel)
class MainPagePosterModelAdmin(admin.ModelAdmin):
    pass

@admin.register(CityModel)
class CityModelAdmin(admin.ModelAdmin):
    pass

@admin.register(BodyTypeModel)
class BodyTypeModelAdmin(admin.ModelAdmin):
    pass

@admin.register(MainPageCarsModel)
class MainPageCarsModelAdmin(admin.ModelAdmin):
    pass

@admin.register(DeliveryModel)
class DeliveryModelAdmin(admin.ModelAdmin):
    pass

@admin.register(PhotoCarsModel)
class PhotoCarsModelAdmin(admin.ModelAdmin):
    pass

@admin.register(CountryModel)
class CountryModelAdmin(admin.ModelAdmin):
    pass

@admin.register(ExternalReviewsModel)
class ExternalReviewsModelAdmin(admin.ModelAdmin):
    pass

@admin.register(YouTubeModel)
class YoutubeModelAdmin(admin.ModelAdmin):
    pass

@admin.register(YouTubePlaylistsModel)
class YouTubePlaylistsModelAdmin(admin.ModelAdmin):
    pass

@admin.register(YouTubeVideosModel)
class YouTubeVideosModelAdmin(admin.ModelAdmin):
    pass

@admin.register(Autodata)
class AutodataModelAdmin(admin.ModelAdmin):
    pass

@admin.register(AutoColorDefaultsModel)
class AutoColorDefaultsModelAdmin(admin.ModelAdmin):
    pass

@admin.register(AutoKPPTypeModel)
class AutoKPPTypeModelAdmin(admin.ModelAdmin):
    pass

@admin.register(AutoMarkaModel)
class AutoMarkaModel(admin.ModelAdmin):
    pass

@admin.register(AutoPrivDefaultsModel)
class AutoPrivDefaultsModelAdmin(admin.ModelAdmin):
    pass

@admin.register(AutoWheelTypeModel)
class AutoWheelTypeModelAdmin(admin.ModelAdmin):
    pass

@admin.register(AutoYearDefaultsModel)
class AutoYearDefaultsModelAdmin(admin.ModelAdmin):
    pass
