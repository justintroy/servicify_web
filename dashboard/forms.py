from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import AuthenticationForm, PasswordResetForm, PasswordChangeForm, SetPasswordForm
from .models import *

from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberPrefixWidget
from location_field.forms.plain import PlainLocationField


class UserLoginForm(AuthenticationForm):

    username = forms.CharField(
        label='Username', max_length=100, help_text='Required')
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update(
            {'placeholder': 'Username', 'name': 'username', 'id': 'username'})
        self.fields['password'].widget.attrs.update(
            {'placeholder': 'Password', 'id': 'password'})


class RegistrationForm(forms.ModelForm):

    username = forms.CharField(
        label='Username', min_length=4, max_length=50, help_text='Required')
    email = forms.EmailField(label='Email', max_length=100, help_text='Required', error_messages={
        'required': 'This field is required.'})
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(
        label='Repeat password', widget=forms.PasswordInput)
    first_name = forms.CharField(
        label='First Name', min_length=1, max_length=50, help_text='Required')
    last_name = forms.CharField(
        label='Last Name', min_length=1, max_length=50, help_text='Required')

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name',)

    def clean_username(self):
        username = self.cleaned_data['username'].lower()
        r = User.objects.filter(username=username)
        if r.count():
            raise ValidationError("Username already exists")
        return username

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords do not match.')
        elif self.cleaned_data.get('username', '').lower() in cd['password'] or self.cleaned_data.get('email', '').lower() in cd['password'] or self.cleaned_data.get('first_name').lower() in cd['password'] or self.cleaned_data.get('last_name').lower() in cd['password']:
            raise forms.ValidationError(
                'Password must NOT include characters that are in your Email, Username, and Names.')

        try:
            validate_password(
                cd['password'], self.instance)
        except ValidationError as error:
            self.add_error("password", error)

        return cd['password2']

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError(
                'E-mail is already taken.')
        return email

    def __init__(self, *args, **kwargs):
        initial = kwargs['initial']
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update(
            {'placeholder': 'Username', 'name': 'username', 'id': 'username'})
        self.fields['email'].widget.attrs.update(
            {'placeholder': 'E-mail', 'name': 'email', 'id': 'email', 'value': initial['email']})
        self.fields['password'].widget.attrs.update(
            {'placeholder': 'Password'})
        self.fields['password2'].widget.attrs.update(
            {'placeholder': 'Repeat password'})
        self.fields['first_name'].widget.attrs.update(
            {'placeholder': 'Your first name', 'name': 'firstname', 'id': 'firstname', 'value': initial['first_name']})
        self.fields['last_name'].widget.attrs.update(
            {'placeholder': 'Your last name', 'name': 'lastname', 'id': 'lastname', 'value': initial['last_name']})
        
        if initial['email']:
            self.fields['email'].disabled = True
        
        if initial['first_name']:
            self.fields['first_name'].disabled = True
        
        if initial['last_name']:
            self.fields['last_name'].disabled = True


class MainUserRegistrationForm(forms.ModelForm):

    phone_number = PhoneNumberField(label='Phone Number', help_text='Required', region='PH', widget=PhoneNumberPrefixWidget)
    city = forms.CharField()
    location = PlainLocationField(based_fields=['city'], initial='14.572950835033037,480.992431640625')

    class Meta:
        model = MainUser
        fields = ['avatar', 'phone_number', 'city', 'location']
    
    def clean_phone_number(self):
        phone_number = self.cleaned_data['phone_number']
        if MainUser.objects.filter(phone_number=phone_number).exists():
            raise forms.ValidationError(
                'Phone number is already taken.')
        return phone_number

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['avatar'].widget.attrs.update(
            {'class': 'file-upload', 'name': 'avatar'})


class CreateWorkOfferForm(forms.ModelForm):
    work_name = forms.CharField(
        label='Name', min_length=5, max_length=100, help_text='Required')
    description = forms.CharField(label='Description', min_length=5,
                                  max_length=1000, help_text='Required', widget=forms.Textarea)
    min_pay = forms.DecimalField(
        label='Starting Bid (PHP)', max_digits=19, decimal_places=4, help_text='Required')

    class Meta:
        model = WorkOffer
        fields = ['work_name', 'description', 'min_pay']


class CreateServiceForm(forms.ModelForm):
    service_name = forms.CharField(
        label='Name', min_length=5, max_length=100, help_text='Required')
    description = forms.CharField(label='Description', min_length=5,
                                  max_length=1000, help_text='Required', widget=forms.Textarea)
    price = forms.DecimalField(
        label='Minimum Pay (PHP)', max_digits=19, decimal_places=4, help_text='Required')
    service_type = forms.ModelChoiceField(
        queryset=ServiceTypes.objects.all(), empty_label="Select category")
    city = forms.CharField()
    location = PlainLocationField(based_fields=['city'], initial='14.572950835033037,480.992431640625')

    class Meta:
        model = Service
        fields = ['service_name', 'description', 'price', 'service_type', 'city', 'location']


class AcquireServiceForm(forms.ModelForm):
    client_msg = forms.CharField(label='Message', min_length=5,
                                 max_length=1000, help_text='Required', widget=forms.Textarea)

    class Meta:
        model = ServiceClients
        fields = ['client_msg']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['client_msg'].widget.attrs.update(
            {'placeholder': 'Enter the details of what you need to be done.', 'name': 'client_msg', 'id': 'client_msg'})


class RateServiceForm(forms.ModelForm):
    message = forms.CharField(
        min_length=5, max_length=1000, help_text='Required', widget=forms.Textarea)

    class Meta:
        model = ServiceReview
        fields = ['message']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['message'].widget.attrs.update(
            {'placeholder': 'Help us improve the platform. Share with us your experience with this service.', 'name': 'message', 'id': 'message'})


class CreateWorkOfferBidForm(forms.ModelForm):
    bidder_msg = forms.CharField(label='Message', min_length=5,
                                 max_length=1000, help_text='Required', widget=forms.Textarea)
    bid_amount = forms.DecimalField(
        max_digits=19, decimal_places=4, help_text='Required')

    class Meta:
        model = Bid
        fields = ['bidder_msg', 'bid_amount']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['bid_amount'].widget.attrs.update(
            {'placeholder': 'Enter your bid', 'name': 'bid_amount', 'id': 'bid_amount'})
        self.fields['bidder_msg'].widget.attrs.update(
            {'placeholder': 'Message', 'name': 'bidder_msg', 'id': 'bidder_msg'})
