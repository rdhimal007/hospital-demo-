from django import forms
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError

User = get_user_model()


INPUT_STYLE = "bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-purple-600 focus:border-purple-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"


class RegisterForm(forms.ModelForm):
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(
        label="Password confirmation", widget=forms.PasswordInput
    )

    class Meta:
        model = User
        fields = [
            "first_name",
            "middle_name",
            "last_name",
            "email",
            "username",
        ]

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords don't match")
        return password2

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)

        for field in self.fields.values():
            field.widget.attrs["class"] = INPUT_STYLE

        self.fields["first_name"].widget.attrs["placeholder"] = "First name"
        self.fields["middle_name"].widget.attrs["placeholder"] = "Middle name"
        self.fields["last_name"].widget.attrs["placeholder"] = "Last name"
        self.fields["username"].widget.attrs["placeholder"] = "Username"
        self.fields["email"].widget.attrs["placeholder"] = "Email"
        self.fields["password1"].widget.attrs["placeholder"] = "Password"
        self.fields["password2"].widget.attrs["placeholder"] = "Confirm Password"

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        user.is_active = True
        if commit:
            user.save()
        return user


class NurseUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            "first_name",
            "middle_name",
            "last_name",
            "email",
            "username",
            "age",
            "gender",
            "phone_number",
            "address",
        ]

    def __init__(self, *args, **kwargs):
        super(NurseUpdateForm, self).__init__(*args, **kwargs)

        for field in self.fields.values():
            field.widget.attrs["class"] = INPUT_STYLE

        self.fields["first_name"].widget.attrs["placeholder"] = "First name"
        self.fields["middle_name"].widget.attrs["placeholder"] = "Middle name"
        self.fields["last_name"].widget.attrs["placeholder"] = "Last name"
        self.fields["username"].widget.attrs["placeholder"] = "Username"
        self.fields["email"].widget.attrs["placeholder"] = "Email"
        self.fields["age"].widget.attrs["placeholder"] = "Age"
        self.fields["phone_number"].widget.attrs["placeholder"] = "Phone Number"
        self.fields["address"].widget.attrs["placeholder"] = "Address"
        self.fields["gender"].widget.attrs["placeholder"] = "Gender"


class NurseUpdateDetails(forms.ModelForm):
    class Meta:
        model = User
        fields = ["phone_number", "address"]

    def __init__(self, *args, **kwargs):
        super(NurseUpdateDetails, self).__init__(*args, **kwargs)

        for field in self.fields.values():
            field.widget.attrs["class"] = INPUT_STYLE

        self.fields["phone_number"].widget.attrs["placeholder"] = "Phone Number"
        self.fields["address"].widget.attrs["placeholder"] = "Address"
