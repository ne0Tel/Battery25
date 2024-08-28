from django.core.paginator import Paginator, Page
from django.utils.functional import cached_property
from django.core.paginator import EmptyPage, PageNotAnInteger
from .models import Autodata
from math import ceil


class CustomPaginator(Paginator):
    def __init__(self, count, per_page, filter, page_number):
        super().__init__([], per_page)
        self.filter = filter
        self._count = count
        self.page_number = page_number

    def _get_page(self, *args, **kwargs):
        page_number = args[1]
        offset = (page_number - 1) * self.per_page

        queryset = Autodata.objects.filter(self.filter)[offset:offset+self.per_page]
        cars = self.processing_data(queryset)

        return Page(cars, page_number, self)
    
    def processing_data(self, queryset):
        return self.get_cars(queryset)

    @staticmethod
    def get_cars(queryset):
        list_car = []

        for record in queryset:

            price_finish = record.finish  
                
            car = {
                "id": record.id,
                "marka_name": record.marka_name,
                "model_name": record.model_name,
                "year": record.year,
                "body_type": record.kuzov,
                "color": record.color,
                "transmission": "Автомат" if record.kpp_type == 2 else "Механика",
                "engine_volume": record.eng_v,
                "priv": record.priv,
                "mileage": record.mileage,
                "price": price_finish
            }
            try:     
                # car["price"], car["inside"], car["outside"], car["toll"] = calc_price(
                #     price=price,
                #     currency=currency,
                #     year=int(row.find("YEAR").text),
                #     volume=int(row.find("ENG_V").text),
                #     table=table,
                # )
                pass
            except:
                car["price"] = 0
            car["photos"] = record.images.replace("=50", "").split("#")
            list_car.append(car)

        return list_car

    @cached_property
    def num_pages(self):
        if self._count == 0 and not self.allow_empty_first_page:
            return 0
        hits = max(1, self._count - self.orphans)
        return ceil(hits / self.per_page)

def get_page(paginator: Paginator, page_number):
    try:
        page_obj = paginator.page(page_number)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)

    return page_obj
