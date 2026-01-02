from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User

from django_countries import countries

from .models import Address


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Add CSS classes and placeholders
        self.fields["username"].widget.attrs.update(
            {"class": "form-control", "placeholder": "User Name *"}
        )
        self.fields["email"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Email address *"}
        )
        self.fields["password1"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Password *"}
        )
        self.fields["password2"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Confirm password *"}
        )

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user


class CustomAuthenticationForm(AuthenticationForm):
    """Custom authentication form that works with email or username."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Add CSS classes and placeholders
        self.fields["username"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Email or Username"}
        )
        self.fields["password"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Password"}
        )

        self.fields["username"].label = "Email or Username"


class AddressForm(forms.ModelForm):
    """
    Form for managing user addresses (billing/shipping).

    Includes country dropdown and proper field styling.
    """

    # Override country field to use country dropdown
    country = forms.ChoiceField(
        choices=[("", "Select Country")] + list(countries),
        widget=forms.Select(attrs={"class": "form-control", "required": True}),
        required=True,
    )

    class Meta:
        model = Address
        fields = [
            "address_type",
            "full_name",
            "address_line_1",
            "address_line_2",
            "city",
            "postcode",
            "country",
        ]

        widgets = {
            "address_type": forms.Select(
                attrs={"class": "form-control", "required": True}
            ),
            "full_name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "* Full Name",
                    "required": True,
                }
            ),
            "address_line_1": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "* Street Address",
                    "required": True,
                }
            ),
            "address_line_2": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Address line 2 (Optional)",
                }
            ),
            "city": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "* City",
                    "required": True,
                }
            ),
            "postcode": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "* Postal Code",
                    "required": True,
                }
            ),
        }

        labels = {
            "address_type": "Address Type",
            "full_name": "Full Name",
            "address_line_1": "Street Address",
            "address_line_2": "Address Line 2",
            "city": "City",
            "postcode": "Postal Code",
            "country": "Country",
        }

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, set default values
        """
        super().__init__(*args, **kwargs)

        # Set UK as default country for new addresses
        if not self.instance.pk:
            self.fields["country"].initial = "GB"
            self.fields["address_type"].initial = Address.BILLING

        # Set autofocus on first field
        self.fields["address_type"].widget.attrs["autofocus"] = True

        # Add required attribute to required fields
        for field_name, field in self.fields.items():
            if field.required:
                field.widget.attrs["required"] = True
