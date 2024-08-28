from django import forms
from django.core.validators import RegexValidator
from .get_unique import *
import re

class FeedbackForm(forms.Form):
    name = forms.CharField(
        max_length=50,
        label='Имя',
        validators=[
            RegexValidator(
                r'^[а-яА-ЯёЁ\s]*$',
                message='Имя должно содержать только буквы кириллицы'
            )
        ],
        error_messages={
            'required': 'Поле имя обязательно для заполнения',
            'max_length': 'Максимальное количество символов 50'
        }
    )

    phone = forms.CharField(
        label='Телефон',
        validators=[
            RegexValidator(
                r'^\+7 \(\d{3}\) \d{3}-\d{2}-\d{2}$',
                message='Телефон должен быть в формате +7 (XXX) XXX-XX-XX'
            )
        ],
        error_messages={
            'required': 'Поле телефон обязательно для заполнения'
        }
    )

    question = forms.CharField(
        widget=forms.Textarea,
        label='Уточнение вопроса',
        max_length=300,
        error_messages={
            'required': 'Поле уточнение вопроса обязательно для заполнения',
            'max_length': 'Максимальное количество символов 300'
        }
    )

    def clean_question(self):
        question = self.cleaned_data['question']
        if re.search(r'<script>', question, re.IGNORECASE):
            raise forms.ValidationError('Недопустимый ввод')
        return question
    
    
class CarFilterForm(forms.Form):
    marka_name = forms.ChoiceField(
        choices=[],
        required=False,
        label="Марка",
        widget=forms.Select(
        )
    )
    model_name = forms.ChoiceField(
        choices=[],
        required=False,
        label="Модель",
        widget=forms.Select(
        )
    )

    mileage_min = forms.ChoiceField(
        choices=[(i, i) for i in range(0, 300000, 20000)],
        required=False,
        label="Пробег от",
        widget=forms.Select(
        )
    )
    mileage_max = forms.ChoiceField(
        choices=[(i, i) for i in range(0, 300000, 20000)],
        required=False,
        label="до",
        widget=forms.Select(
        )
    )

    year_min = forms.ChoiceField(
        choices=[],
        required=False,
        label="Год от",
        widget=forms.Select(
        )
    )
    year_max = forms.ChoiceField(
        choices=[],
        required=False,
        label="до",
        widget=forms.Select(
        )
    )

    engine_volume_min = forms.ChoiceField(
        choices=[(i, i) for i in range(0, 6000, 1000)],
        required=False,
        label="Объем от",
        widget=forms.Select(
        )
    )
    engine_volume_max = forms.ChoiceField(
        choices=[(i, i) for i in range(0, 6000, 1000)],
        required=False,
        label="до",
        widget=forms.Select(
        )
    )

    transmission = forms.ChoiceField(
        choices=[],
        required=False,
        label="Тип КПП",
        widget=forms.Select(
        )
    )

    priv = forms.ChoiceField(
        choices=[],
        required=False,
        label="Тип привода",
        widget=forms.Select(
        )
    )

    wheel_type = forms.ChoiceField(
        choices=[],
        required=False,
        label='Тип руля',
        widget=forms.Select(  
        )
    )

    color = forms.ChoiceField(
        choices=[],
        required=False,
        label="Цвет",
        widget=forms.Select(
        )
    )

    def is_valid(self):
        valid = super(CarFilterForm, self).is_valid()
        if not valid:
            print(self.errors)
            if "model" in self.errors:
                model = self.errors["model"]
                match = re.search(
                    r"Выберите корректный вариант\. (.*?) нет среди допустимых значений\.",
                    model[0],
                )
                value = match.group(1) if match else None
                # value["model"] = value
                self.cleaned_data["model"] = value
                print(value)
                del self.errors["model"]

            if "color" in self.errors:
                color = self.errors["color"]
                match = re.search(
                    r"Выберите корректный вариант\. (.*?) нет среди допустимых значений\.",
                    color[0],
                )
                value = match.group(1) if match else None
                # value["model"] = value
                self.cleaned_data["color"] = value
                print(value)
                del self.errors["color"]

            if "transmission" in self.errors:
                transmission = self.errors["transmission"]
                match = re.search(
                    r"Выберите корректный вариант\. (.*?) нет среди допустимых значений\.",
                    transmission[0],
                )
                value = match.group(1) if match else None
                # value["model"] = value
                self.cleaned_data["transmission"] = value
                print(value)
                del self.errors["transmission"]

            valid = not bool(self.errors)
        return valid
    
class CarJapanFilterForm(CarFilterForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["marka_name"].choices = [("", "Любое")] + get_unique_marka("japan")
        
        self.fields["model_name"].choices = [("", "Любое")]

        self.fields['year_min'].choices = [("", "Любое")] + get_unique_year("japan")

        self.fields['year_max'].choices = [("", "Любое")] + get_unique_year("japan")

        self.fields["transmission"].choices = [("", "Любое")] + get_unique_kpp()
        
        self.fields["priv"].choices = [("", "Любое")] + get_unique_priv()
        
        self.fields["color"].choices = [("", "Любое")] + get_unique_color()

        self.fields['wheel_type'].choices = [("", "Любое")] + get_wheel_type()