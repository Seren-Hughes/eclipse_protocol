from django import forms
from django_countries import countries
from .models import Order


class OrderForm(forms.ModelForm):
    """
    Order form for checkout process.
    
    Collects customer details and billing information.
    User field is handled separately in the view logic.
    """
    
    # Override country field to use country dropdown
    country = forms.ChoiceField(
    choices=[('', 'Select Country')] + list(countries),
    widget=forms.Select(attrs={
        'class': 'form-control',
        'required': True
    }),
    required=True
)
    
    class Meta:
        model = Order
        fields = [
            'full_name', 'email', 'phone_number',
            'street_address_1', 'street_address_2', 
            'city', 'postcode', 'country'
        ]
        
        widgets = {
            'full_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '* Full Name',
                'required': True
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': '* Email Address',
                'required': True
            }),
            'phone_number': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Phone Number (Optional)'
            }),
            'street_address_1': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '* Street Address',
                'required': True
            }),
            'street_address_2': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Address line 2 (Optional)'
            }),
            'city': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '* City',
                'required': True
            }),
            'postcode': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '* Postal Code',
                'required': True
            })
        }
        
        labels = {
            'full_name': 'Full Name',
            'email': 'Email Address',
            'phone_number': 'Phone Number',
            'street_address_1': 'Street Address',
            'street_address_2': 'Address Line 2',
            'city': 'City',
            'postcode': 'Postal Code',
            'country': 'Country'
        }
    
    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated labels
        and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        
        # Set UK as default country
        if not self.instance.pk:
            self.fields['country'].initial = 'GB'
        
        # Set autofocus on first field
        self.fields['full_name'].widget.attrs['autofocus'] = True
        
        # Add required attribute to required fields
        for field_name, field in self.fields.items():
            if field.required:
                field.widget.attrs['required'] = True