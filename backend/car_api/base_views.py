from django.views.generic.list import BaseListView
from django.views.generic.base import TemplateResponseMixin
from django.db.models import Q
from .models import Autodata
from .forms import FeedbackForm
from .paginator import CustomPaginator, get_page

class FilteredCarListView(BaseListView, TemplateResponseMixin):
    template_name = "templates/catalog/catalog.html"
    context_object_name = "cars"
    paginate_by = 8
    link_url = None
    title = None
    car_link = None
    url_api = None

    def update_query(self):
        form = self.filter_form()
        self.filter = Q(id__isnull=False)
        if form.is_valid():
            try:
                if form.cleaned_data["marka_name"]:
                    self.filter &= Q(marka_name=form.cleaned_data["marka_name"])
                    
                if form.cleaned_data["model_name"]:
                    self.filter &= Q(model_name=form.cleaned_data["model_name"])
                    
                if form.cleaned_data["color"]:
                    self.filter &= Q(true_color=form.cleaned_data["color"])
                    
                if form.cleaned_data["mileage_min"]:
                    mileage = int(
                        form.cleaned_data["mileage_min"].replace(" ", "")
                    )
                    self.filter &= Q(mileage__gt=mileage)

                if form.cleaned_data["mileage_max"]:
                    mileage = int(
                        form.cleaned_data["mileage_max"].replace(" ", "")
                    )
                    self.filter &= Q(mileage__lt=mileage)
                    
                if form.cleaned_data["year_min"]:
                    self.filter &= Q(year__gt=form.cleaned_data['year_min'])

                if form.cleaned_data["year_max"]:
                    self.filter &= Q(year__lt=form.cleaned_data['year_max'])

                if form.cleaned_data["transmission"]:
                    kpp_dict = {
                        'Автомат': 2,
                        'Механика': 1
                    }
                    kpp_type = kpp_dict.get(form.cleaned_data["transmission"])
                    self.filter &= Q(kpp_type=kpp_type)

                if form.cleaned_data["priv"]:
                    self.filter &= Q(true_priv=form.cleaned_data["priv"])

                if form.cleaned_data["engine_volume_min"]:
                    eng = int(
                        form.cleaned_data["engine_volume_min"].replace(" ", "")
                    )
                    self.filter &= Q(eng_v__gt=eng)
                    
                if form.cleaned_data["engine_volume_max"]:
                    eng = int(
                        form.cleaned_data["engine_volume_max"].replace(" ", "")
                    )
                    self.filter &= Q(eng_v__lt=eng)

                if form.cleaned_data["wheel_type"]:
                    self.filter &= Q(wheel_type=form.cleaned_data["wheel_type"])

            except Exception as e:
                print(e)
    
    def filter_form(self):
        return self.form_filter(self.request.GET or None)

    def count_page(self):
        auto_objs_count = Autodata.objects.filter(self.filter).count()
        return auto_objs_count

    def get_context_data(self, **kwargs):
        self.update_query()

        total_count = self.count_page()
        page_number = int(self.request.GET.get("page", 1))
        paginator = CustomPaginator(
            count=total_count,
            per_page=self.paginate_by,
            filter=self.filter,
            page_number=page_number,
        )
        
        page_number = self.request.GET.get("page", 1)
        page_obj = get_page(paginator=paginator, page_number=page_number)

        print(page_obj.object_list)
                
        return {
            "page_obj": page_obj,
            "is_paginated": page_obj.has_other_pages(),
            "cars": page_obj.object_list,
            "filter_form": self.filter_form(),
            "link_url": self.link_url,
            "feedbackForm": FeedbackForm(),
            "title": self.title,
            "car_link": self.car_link,
        }

    def get(self, request, *args, **kwargs):
        context = self.get_context_data()
        return self.render_to_response(context)