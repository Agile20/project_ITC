from django import forms

from .models import GetConsult

# форма получения консультации
class GetConsultForm(forms.ModelForm):
    model = GetConsult
    fields = (
        'name',
        'question',
        'contact',
    )