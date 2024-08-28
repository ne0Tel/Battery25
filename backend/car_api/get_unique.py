from .models import CountryModel, AutoMarkaModel, AutoYearDefaultsModel, AutoColorDefaultsModel, AutoKPPTypeModel, AutoPrivDefaultsModel, AutoWheelTypeModel


def get_unique_marka(country: str):
    country_obj = CountryModel.objects.get(country_name=country)
    marka_names = AutoMarkaModel.objects.filter(country=country_obj).distinct()
    return [(marka_obj.marka_name, marka_obj.marka_name) for marka_obj in marka_names]

def get_unique_year(country: str):
    country_obj = CountryModel.objects.get(country_name=country)
    years_objs = AutoYearDefaultsModel.objects.filter(country=country_obj)
    return [(year_obj.year, year_obj.year) for year_obj in years_objs]

def get_unique_color():
    color_objs = AutoColorDefaultsModel.objects.all()
    return [(color_obj.color_name, color_obj.color_name) for color_obj in color_objs]

def get_unique_kpp():
    kpp_objs = AutoKPPTypeModel.objects.all()
    return [(kpp_obj.kpp_type, kpp_obj.kpp_type) for kpp_obj in kpp_objs]

def get_unique_priv():
    priv_objs = AutoPrivDefaultsModel.objects.all()
    return [(priv_obj.priv_name, priv_obj.priv_name) for priv_obj in priv_objs]

def get_wheel_type():
    wheel_objs = AutoWheelTypeModel.objects.all()
    return [(wheel_obj.wheel_type, wheel_obj.wheel_type) for wheel_obj in wheel_objs]
