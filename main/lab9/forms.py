from django import forms
from .models import Waybill


class WaybillForm(forms.ModelForm):

    class Meta:
        model = Waybill
        fields = ['driver', 'departure_time', 'check_in_time', 'initial_mileage',
                  'initial_mileage', 'final_milage']

