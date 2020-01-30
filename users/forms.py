from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from .models import User


# User forms for different user groups
class StaffSignUpForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = User

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_staff = True
        if commit:
            user.save()
        return user


class CustomerSignUpForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_customer = True
        user.save()
        return user


# These choices will appear in user setup after first login
IF_SELLING = [
    ('i sell via a different system', 'I sell via a different system'),
    ('i do not sell yet', 'I do not sell yet'),
    ('i am just playing around', 'I am just playing around'),
    ('i sell offline', 'I sell offline'),
]

HOW_DO_YOU_WANNA_SELL = [
    ('online', 'Online'),
    ('in person', 'In person'),
    ('both online and in person', 'Both online and in person'),
]

WHERE_YOU_SELL = [
    ('in a shop', 'In a shop'),
    ('at pop-ups', 'At pop-ups'),
    ('fairs and markets', 'Fairs and markets'),
]

MOSTLY_USED_SYSTEM = [
    ('WooCommerce', 'WooCommerce'),
    ('Wix', 'Wix'),
    ('Tictail', 'Tictail'),
    ('Volusion', 'Volusion'),
    ('Shopify', 'Shopify'),
    ('Kickstarter', 'Kickstarter'),
    ('OpenCart', 'OpenCart'),
    ('Squarespace', 'Squarespace'),
    ('Clover', 'Clover'),
    ('Square', 'Square'),
    ('BigCommerce', 'BigCommerce'),
    ('IndieGogo', 'IndieGogo'),
    ('WordPress', 'WordPress'),
    ('PrestaShop', 'PrestaShop'),
    ('Etsy', 'Etsy'),
    ('Revel', 'Revel'),
    ('Big Cartel', 'Big Cartel'),
    ('ShopKeep', 'ShopKeep'),
    ('eBay', 'eBay'),
    ('GoDaddy', 'GoDaddy'),
    ('Magento 1', 'Magento 1'),
    ('Magento 2', 'Magento 2'),
    ('Vend', 'Vend'),
    ('Amazon', 'Amazon'),
    ('lightspeed', 'lightspeed'),
    ('Other', 'Other'),
]

CURRENT_REVENUE = [
    ('i sell via a different system', 'I sell via a different system'),
    ('i do not sell yet', 'I do not sell yet'),
    ('i am just playing around', 'I am just playing around'),
    ('i sell offline', 'I sell offline'),
]


# Forms
class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional')
    email = forms.EmailField(max_length=254, help_text='Enter a valid email address')

    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',
        ]


class CompleteSetupOne(forms.Form):
    if_selling = forms.CharField(max_length=200)
    how_do_you_wanna_sell = forms.CharField(max_length=200)
    mostly_used_system = forms.CharField(max_length=200)
    why_you_chose_us = forms.CharField(max_length=200)
    where_you_sell = forms.CharField(max_length=200)
    current_revenue = forms.CharField(max_length=200)
    i_am_a_developer = forms.BooleanField()

    class Meta:
        model = User
        fields = [
            'if_selling',
            'how_do_you_wanna_sell',
            'mostly_used_system',
            'why_you_chose_us',
            'where_you_sell',
            'current_revenue',
            'i_am_a_developer',
        ]


class CompleteSetupTwo(forms.Form):
    first_name = forms.CharField(max_length=200)
    last_name = forms.CharField(max_length=200)
    company_address = forms.CharField(max_length=200)
    address_extra = forms.CharField(max_length=200)
    city = forms.CharField(max_length=200)
    zip_code = forms.CharField(max_length=200)
    country = forms.CharField(max_length=200)
    phone = forms.CharField(max_length=200)
    website = forms.CharField(max_length=200)

    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'address',
            'address_extra',
            'city',
            'zip_code',
            'country',
            'phone',
            'website',
        ]
