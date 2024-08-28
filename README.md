Модели в БД:

YouTubeModel:

  'Информация о YouTube канале'

    link = ('Ссылка на канал', max_length=255) - тип varchar
    
    api_key = ('API KEY для работы с API Google', max_length=255) - тип varchar
    
    channel_id = ('ID канал на YouTube', max_length=255) - тип varchar


ContactsModel:

  'Контакты'
  
    whatsapp_link = ('Ссылка на WhatsApp', max_length=255) - тип varchar
    
    telegram_link = ('Ссылка на Telegram', max_length=255) - тип varchar
    
    instagram_link = ('Ссылка на Instagram', max_length=255) - тип varchar
    
    youtube = внешний ключ на YouTubeModel

MainPagePosterModel:

  'Постер на главной странице'
  
    title = ('Заголовок', max_length=255) - тип varchar
    
    clients_rate = ('Рейтинг клиентов') - тип numeric
    
    market_age = ('Лет на рынке', max_length=20) - тип varchar
    
    brought_auto = ('Привезенных авто', max_length=20) - тип varchar
    
    repeated_appeal = ('Повторно обращается', max_length=100) - тип varchar

CityModel:

  'Города'
  
    name = ('Город', max_length=255) - тип varchar

BodyTypeModel:

  'Типы кузова'
  
    name = ('Тип кузова', max_length=255) - тип varchar

CountryModel:

  'Страны'
  
    country_name = ('Название страны', max_length=255) - тип varchar

PhotoCarsModel:

  'Фото машин'

    image = (upload_to="main_page_cars/") - фото автомобилей

MainPageCarsModel:

  'Машины на главной странице'
  
    brand = (verbose_name='Марка машины', max_length=255) - тип varchar
    
    model = (verbose_name='Модель машины', max_length=255) - тип varchar
    
    img = внешний ключ (PhotoCarsModel, null=True, 'Фотографии авто') 
    
    price = (verbose_name='Цена') тип integer
    
    rating = (verbose_name='Оценка') - тип numeric
    
    year = (verbose_name='Год') - тип integer
    
    body_type = внешний ключ (BodyTypeModel, on_delete=models.CASCADE)
    
    mileage = (verbose_name='Пробег') - тип integer
    
    country = внешний ключ (CountryModel, on_delete=models.CASCADE)
    

DeliveryModel:

  'Доставка'
  
    city = внешний ключ (CityModel, on_delete=models.CASCADE)
    
    body_type = внешний ключ (BodyTypeModel, on_delete=models.CASCADE)
    
    price = (verbose_name='Цена доставки') - тип integer
    
    path_time = (verbose_name='Суток в пути') - тип integer
    

ExternalReviewsModel:

  'Оценки на внешних ресурсах'
  
    title = ('Название ресурса', max_length=255) - тип varchar
    
    link = ('Ссылка', max_length=255) - тип varchar
    
    api_id = ('API ID компании в 2GIS', max_length=255, null=True, blank=True) - тип varchar
    
    company_id = ('ID компании в VL.RU или в 2GIS') - тип integer
    
    rate = ('Оценка', null=True, blank=True) - тип numeric
    
    reviews_count = ('Количество отзывов', null=True, blank=True) - тип integer
    

YouTubeVideosModel:

  'Видео'
  
    title = ('Заголовок видео', max_length=255) - тип varchar
    
    video_id = ('ID видео на YouTube', max_length=255) - тип varchar
    
    cover_url = ('URL на кавер видео', max_length=255) - тип varchar
    

YouTubePlaylistsModel:

  'Плейлисты'
  
    name = ('Название плейлиста', max_length=255) - тип varchar
    
    playlist_id = ('ID плейлиста на YouTube', max_length=255) - тип varchar
    
    videos = внешний ключ ManyToMany ('Видео из плейлиста', to=YouTubeVideosModel, blank=True, null=True)
    

AlembicVersion:

  'Версии миграций Alembic'
  
    version_num = ('Номер версии',primary_key=True, max_length=32) - тип varchar

Autodata:

'Данные по автомобилям'

    id = api id с аукционов (primary_key=True) - тип varchar
    
    auction_date = дата проведения аукциона (blank=True, null=True) - тип date
    
    auction = название аукциона (blank=True, null=True) - тип varchar
    
    marka_id = id марки (blank=True, null=True) - тип integer

    model_id = id модели (blank=True, null=True) - тип integer
    
    marka_name = название марки (blank=True, null=True) - тип varchar
    
    model_name = название модели (blank=True, null=True) - тип varchar
    
    year = год авто(blank=True, null=True) - тип integer
    
    age = возраст авто (blank=True, null=True) - тип integer
    
    is_sanction = равен ли возраст 3 или 5 (blank=True, null=True)
    
    eng_v = объем двигателя (blank=True, null=True) - тип integer
    
    pw = мощность двигателя (blank=True, null=True) - тип varchar
    
    kuzov = номер кузова (blank=True, null=True) - тип varchar
    
    grade = грейд авто (blank=True, null=True) - тип varchar
    
    color = цвет с таблицы при парсинге (blank=True, null=True) - тип varchar
    
    true_color = цвет приведенный к общему (blank=True, null=True) - тип varchar
    
    kpp = кпп (blank=True, null=True) - тип varchar
    
    kpp_type = id кпп (blank=True, null=True) - тип integer
    
    priv = привод с таблицы с парсинге (blank=True, null=True) - тип varchar
    
    true_priv = привод приведенный к общему (blank=True, null=True) - тип varchar
    
    mileage = пробег (blank=True, null=True) - тип integer
    
    equip = эквип (blank=True, null=True) - тип varchar
    
    rate = оценка (blank=True, null=True) - тип varchar
    
    finish = финишная цена на аукционе (blank=True, null=True) - тип integer
    
    images = фото авто (blank=True, null=True) - тип varchar
    
    country_provider = страна производитель (blank=True, null=True) - тип varchar
    
    wheel_type = тип руля (blank=True, null=True) - тип varchar
    
    last_updated_currency = последнее обновление курса (blank=True, null=True) - тип date
    
    last_parsing_date = дата парсинга (blank=True, null=True) - тип date
    
    inside_rub_price = цена в рублях в РФ (max_digits=65535, decimal_places=65535, blank=True, null=True) - тип numeric
    
    outside_rub_price = цена в рублях вне РФ (max_digits=65535, decimal_places=65535, blank=True, null=True) - тип numeric

Currency:

'Курс валют'

    last_updated = последнее обновление курса (blank=True, null=True) - тип date
    
    usd = доллар (max_digits=65535, decimal_places=65535, blank=True, null=True) - тип numeric
    
    eur = евро (max_digits=65535, decimal_places=65535, blank=True, null=True) - тип numeric
    
    jpy = йена (max_digits=65535, decimal_places=65535, blank=True, null=True) - тип numeric
    
    krw = корейская вона (max_digits=65535, decimal_places=65535, blank=True, null=True) - тип numeric
    
    cny = юань (max_digits=65535, decimal_places=65535, blank=True, null=True) - тип numeric

Основные эндпоинты:

1) http://localhost:8000/cars_api/api/delivery

Данный эндпоинт необходим для запроса цены и времени в пути за доставку

POST:
  
  Request body:
```json
  {
    "bodyType": "Джип" ,
    "city": "Курган"
  }
```
  
  Response body:
```json
  {
    "price": 175000,
    "path_time": 35
  }
```

2) http://localhost:8000/cars_api/api/feedback

Данный эндпоинт необходим для обработки данных с формы

POST:

Валидация: 
  Имя содержит только буквы кириллицы
  Телефон в формате "+7 (XXX) XXX-XX-XX"
  Поле с вопросом не должно содержать js-тегов, html-тегов (пока нужно протестить и сделать лучшую обработку)

  Request body:
```json
  {
    "name": "Никита",
    "phone": "+7 (345) 324-12-78",
    "question": "Вопрос" 
  }
```
  Response body:
```json
  {
    "success": "Form is valid"
  }
```

3) http://localhost:8000/cars_api/api/get_by_price

Данный эндпоинт необходим для фильтрации авто на главной странице по цене

POST:

Возможные категории: 'car-500k', 'car-600k', 'car-1kk', 'car-2kk', 'car-3kk', 'car-4kk', 'car-5kk'

  Request body:
```json
  {
    "country": "Китай",
    "price_cat": "car-5kk"
  }
```
  
  Response body:
```json
  {
    "car-5kk": [
        {
            "id": 5,
            "country": "Китай",
            "img": "/media/main_page_cars/bf901a30-55fd-11ef-8aa4-d843ae384d18.webp",
            "body_type": "Кроссовер",
            "brand": "Changan",
            "model": "UNI-K",
            "price": 3050000,
            "rating": 5.0,
            "year": 2023,
            "mileage": 30000
        },
        {
            "id": 6,
            "country": "Китай",
            "img": "/media/main_page_cars/f0f68bb2-55fd-11ef-8f11-d843ae384d18.webp",
            "body_type": "Джип",
            "brand": "Geely",
            "model": "Monjaro",
            "price": 2600000,
            "rating": 4.0,
            "year": 2023,
            "mileage": 50000
        }
    ]
}
```
