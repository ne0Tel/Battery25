import uuid

from django.db import models
from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile

class YouTubeModel(models.Model):
    class Meta:
        verbose_name = 'Информация о YouTube канале'    
        verbose_name_plural = 'Информация о YouTube канале'

    link = models.CharField(verbose_name='Ссылка на канал', max_length=255)
    api_key = models.CharField(verbose_name='API KEY для работы с API Google', max_length=255)
    channel_id = models.CharField(verbose_name='ID канал на YouTube', max_length=255)

    def __str__(self) -> str:
        return self.link

class ContactsModel(models.Model):
    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'

    whatsapp_link = models.CharField(help_text='Ссылка на WhatsApp', max_length=255)
    telegram_link = models.CharField(help_text='Ссылка на Telegram', max_length=255)
    instagram_link = models.CharField(help_text='Ссылка на Instagram', max_length=255)
    youtube = models.ForeignKey(YouTubeModel, on_delete=models.CASCADE, null=True, blank=True)
    
    def __str__(self) -> str:
        return 'Контакты'

class MainPagePosterModel(models.Model):
    class Meta:
        verbose_name = 'Постер на главной странице'
        verbose_name_plural = 'Постер на главной странице'
    
    title = models.CharField(max_length=255)
    clients_rate = models.FloatField(verbose_name='Рейтинг клиентов')
    market_age = models.CharField(verbose_name='Лет на рынке', max_length=20)
    brought_auto = models.CharField(verbose_name='Привезенных авто', max_length=20)
    repeated_appeal = models.CharField(verbose_name='Повторно обращается', max_length=100)

class CityModel(models.Model):
    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'

    name = models.CharField(verbose_name='Город', max_length=255)

    def __str__(self) -> str:
        return self.name

class BodyTypeModel(models.Model):
    class Meta:
        verbose_name = 'Тип кузова'
        verbose_name_plural = 'Типы кузова'

    name = models.CharField(verbose_name='Тип кузова', max_length=255)

    def __str__(self) -> str:
        return self.name

class CountryModel(models.Model):
    class Meta:
        verbose_name = 'Страна'
        verbose_name_plural = 'Страны'

    country_name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.country_name

class AutoMarkaModel(models.Model):
    class Meta:
        verbose_name = 'Марка и модель авто'
        verbose_name_plural = 'Марки и модели авто'

    marka_name = models.CharField(verbose_name='Название марки авто', max_length=255)
    model_name = models.CharField(verbose_name='Название модели авто', max_length=255)
    country = models.ForeignKey(verbose_name='Страна', to=CountryModel, on_delete=models.CASCADE, default=None)

    def __str__(self) -> str:
        return self.marka_name

class AutoPrivDefaultsModel(models.Model):
    class Meta:
        verbose_name = 'Привод авто'
        verbose_name_plural = 'Приводы авто'

    priv_name = models.CharField(verbose_name='Вид привода', max_length=255)

    def __str__(self) -> str:
        return self.priv_name

class AutoColorDefaultsModel(models.Model):
    class Meta:
        verbose_name = 'Цвет авто'
        verbose_name_plural = 'Цвета авто'

    color_name = models.CharField(verbose_name='Название цвета', max_length=255)

    def __str__(self) -> str:
        return self.color_name

class AutoYearDefaultsModel(models.Model):
    class Meta:
        verbose_name = 'Год авто'
        verbose_name_plural = 'Года авто'

    year = models.IntegerField(verbose_name='Год автомобиля')
    country = models.ForeignKey(verbose_name='Страна', to=CountryModel, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.year

class AutoWheelTypeModel(models.Model):
    class Meta:
        verbose_name = 'Тип руля'
        verbose_name_plural = 'Типы руля'

    wheel_type = models.CharField(verbose_name='Тип руля', max_length=10)

    def __str__(self) -> str:
        return self.wheel_type

class AutoKPPTypeModel(models.Model):
    class Meta:
        verbose_name = 'Тип КПП'
        verbose_name_plural = 'Типы КПП'

    kpp_type = models.CharField(verbose_name='Тип КПП', max_length=255)

    def __str__(self) -> str:
        return self.kpp_type

class PhotoCarsModel(models.Model):
    image = models.ImageField(upload_to="main_page_cars/")

    def save(self, *args, **kwargs):
        name = str(uuid.uuid1())
        img = Image.open(self.image)
        img_io = BytesIO()
        img.save(img_io, format="WebP")
        img_file = InMemoryUploadedFile(
            img_io, None, f"{name}.webp", "image/webp", img_io.tell(), None
        )
        self.image.save(f"{name}.webp", img_file, save=False)

        super(PhotoCarsModel, self).save(*args, **kwargs)

    class Meta:
        verbose_name = "Фото машины"
        verbose_name_plural = "Фото машин"

    def __str__(self):
        return f"{self.image}"

class MainPageCarsModel(models.Model):
    class Meta:
        verbose_name = 'Машина на главной странице'
        verbose_name_plural = 'Машины на главной странице'

    brand = models.CharField(verbose_name='Марка машины', max_length=255) # сделать модель отдельно default = ''
    model = models.CharField(verbose_name='Модель машины', max_length=255)
    img = models.ManyToManyField(PhotoCarsModel, null=True, verbose_name='Фотографии авто') # on delete 
    price = models.IntegerField(verbose_name='Цена') # default = 1000000
    rating = models.FloatField(verbose_name='Оценка') # default = 4.9
    year = models.IntegerField(verbose_name='Год') # выбрать отдельную модель 
    body_type = models.ForeignKey(BodyTypeModel, on_delete=models.CASCADE)
    mileage = models.IntegerField(verbose_name='Пробег') # default = 30000
    country = models.ForeignKey(CountryModel, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.brand} {self.model} {self.year}"

class DeliveryModel(models.Model):
    class Meta:
        verbose_name = 'Доставка'
        verbose_name_plural = 'Доставка'

    city = models.ForeignKey(CityModel, on_delete=models.CASCADE)
    body_type = models.ForeignKey(BodyTypeModel, on_delete=models.CASCADE)
    price = models.IntegerField(verbose_name='Цена доставки')
    path_time = models.IntegerField(verbose_name='Суток в пути')

class ExternalReviewsModel(models.Model):
    class Meta:
        verbose_name = 'Оценка на внешних ресурсах'
        verbose_name_plural = 'Оценки на внешних ресурсах'

    title = models.CharField(verbose_name='Название ресурса', max_length=255)
    link = models.CharField(verbose_name='Ссылка', max_length=255)
    api_id = models.CharField(verbose_name='API ID компании в 2GIS', max_length=255, null=True, blank=True)
    company_id = models.IntegerField(verbose_name='ID компании в VL.RU или в 2GIS')
    rate = models.FloatField(verbose_name='Оценка', null=True, blank=True)
    reviews_count = models.IntegerField(verbose_name='Количество отзывов', null=True, blank=True)

    def __str__(self) -> str:
        return f'Отзывы на {self.title}'

class YouTubeVideosModel(models.Model):
    class Meta:
        verbose_name = 'Видео'
        verbose_name_plural = 'Видео'

    title = models.CharField(verbose_name='Заголовок видео', max_length=255)
    video_id = models.CharField(verbose_name='ID видео на YouTube', max_length=255)
    cover_url = models.CharField(verbose_name='URL на кавер видео', max_length=255)

    def __str__(self) -> str:
        return self.title

class YouTubePlaylistsModel(models.Model):
    class Meta:
        verbose_name = 'Плейлист'
        verbose_name_plural = 'Плейлисты'

    name = models.CharField('Название плейлиста', max_length=255)
    playlist_id = models.CharField(verbose_name='ID плейлиста на YouTube', max_length=255)
    videos = models.ManyToManyField(verbose_name='Видео из плейлиста', to=YouTubeVideosModel, blank=True, null=True)

    def __str__(self) -> str:
        return self.name
    
class AlembicVersion(models.Model):
    version_num = models.CharField(primary_key=True, max_length=32)

    class Meta:
        managed = False
        db_table = 'alembic_version'


class Autodata(models.Model):
    class Meta:
        verbose_name = 'Данные по авто'
        verbose_name_plural = 'Данные по авто'

    id = models.CharField(primary_key=True, max_length=255)
    auction_date = models.DateTimeField(blank=True, null=True)
    auction = models.CharField(blank=True, null=True, max_length=255)
    marka_id = models.IntegerField(blank=True, null=True)
    model_id = models.IntegerField(blank=True, null=True)
    marka_name = models.CharField(blank=True, null=True, max_length=255)
    model_name = models.CharField(blank=True, null=True, max_length=255)
    year = models.IntegerField(blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    is_sanction = models.BooleanField(blank=True, null=True)
    eng_v = models.IntegerField(blank=True, null=True)
    pw = models.CharField(blank=True, null=True, max_length=255)
    kuzov = models.CharField(blank=True, null=True, max_length=255)
    grade = models.CharField(blank=True, null=True, max_length=255)
    color = models.CharField(blank=True, null=True, max_length=255)
    true_color = models.CharField(blank=True, null=True, max_length=255)
    kpp = models.CharField(blank=True, null=True, max_length=255)
    kpp_type = models.IntegerField(blank=True, null=True)
    priv = models.CharField(blank=True, null=True, max_length=255)
    true_priv = models.CharField(blank=True, null=True, max_length=255)
    mileage = models.IntegerField(blank=True, null=True)
    equip = models.CharField(blank=True, null=True, max_length=255)
    rate = models.CharField(blank=True, null=True, max_length=255)
    finish = models.IntegerField(blank=True, null=True)
    images = models.CharField(blank=True, null=True, max_length=255)
    country_provider = models.CharField(blank=True, null=True, max_length=255)
    wheel_type = models.CharField(blank=True, null=True, max_length=255)
    last_updated_currency = models.DateField(blank=True, null=True)
    last_parsing_date = models.DateField(blank=True, null=True)
    inside_rub_price = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    outside_rub_price = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'autodata'


class Currency(models.Model):
    last_updated = models.DateField(blank=True, null=True)
    usd = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    eur = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    jpy = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    krw = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    cny = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'currency'

