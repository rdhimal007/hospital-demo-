from django import forms
from django.utils import timezone

from accounts.models import PatientProfile
from .models import ScheduleVaccine

INPUT_STYLE = "bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-purple-600 focus:border-purple-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"


class PatientProfileForm(forms.ModelForm):
    class Meta:
        model = PatientProfile
        exclude = ["user"]

    def __init__(self, *args, **kwargs):
        super(PatientProfileForm, self).__init__(*args, **kwargs)

        for field in self.fields.values():
            field.widget.attrs["class"] = INPUT_STYLE


class ScheduleVaccineForm(forms.ModelForm):
    schedule_date = forms.DateField(initial=timezone.now())
    schedule_time = forms.TimeField(
        widget=forms.TimeInput(format="%H:%M"), initial=timezone.now()
    )

    class Meta:
        model = ScheduleVaccine
        # fields = "__all__"
        exclude = ["nurse", "patient", "on_holding"]

    def __init__(self, *args, **kwargs):
        super(ScheduleVaccineForm, self).__init__(*args, **kwargs)

        for field in self.fields.values():
            field.widget.attrs["class"] = INPUT_STYLE
