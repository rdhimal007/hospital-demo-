from django import forms

from .models import Vaccine


INPUT_STYLE = "bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-purple-600 focus:border-purple-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"


class VaccineForm(forms.ModelForm):
    class Meta:
        model = Vaccine
        exclude = ["slug"]

    def __init__(self, *args, **kwargs):
        super(VaccineForm, self).__init__(*args, **kwargs)

        for field in self.fields.values():
            field.widget.attrs["class"] = INPUT_STYLE

        self.fields["availability"].widget.attrs["class"] = ""
