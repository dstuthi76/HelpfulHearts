from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UsernameField,PasswordChangeForm, PasswordResetForm,SetPasswordForm
from django.contrib.auth.models import User
from django.utils.translation import gettext,gettext_lazy as _
from django.contrib.auth import password_validation
from .models import Profile
from .models import contactus,BuyNow,SLOT1

class CustomerRegistrationForm(UserCreationForm):
    username = forms.CharField(label='Username', widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.CharField(required=True, widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Confirm Password (again)',widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class Meta:
    model = User
    labels = {'email': 'Email'}
    fields = ['username','email','password1','password2']
    widgets = {'username'}


class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'autofocus': True,'class': 'form-control'}))
    password = forms.CharField(label=_("Password"),strip=False,widget=forms.PasswordInput(attrs={'autocomplete':'current-password','class': 'form-control'}))


class MyPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(label=("Old Password"),strip=False,widget=forms.PasswordInput(attrs={'autocomplete': 'current-password','autofocus':True,'class':'form-control'}))
    new_password1 = forms.CharField(label=("New Password"),strip=False,widget=forms.PasswordInput(attrs={'autocomplete': 'new-password','class':'form-control'}),
    help_text=password_validation.password_validators_help_text_html())
    new_password2 = forms.CharField(label=("Confirm New Password"),strip=False,widget=forms.PasswordInput(attrs={'autocomplete': 'new-password','class':'form-control'}))


class MyPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(label=('Email'),max_length=254,widget=forms.EmailInput(attrs={'autocomplete':'email','class':'form-control'}))


class MySetPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(label=("New Password"), strip=False, widget=forms.PasswordInput(
        attrs={'autocomplete': 'new-password', 'class': 'form-control'}),
                                    help_text=password_validation.password_validators_help_text_html())
    new_password2 = forms.CharField(label=("Confirm New Password"), strip=False, widget=forms.PasswordInput(
        attrs={'autocomplete': 'new-password', 'class': 'form-control'}))

class CustomerProfileForm(forms.ModelForm):
    class Meta:

      model = Profile
      fields =['name','Goal','units','gender','height_feet','height_inch','weight','Age','Bodyfat','Activity_level','Primary_Diet']
      widgets= {'name':forms.TextInput(attrs={'class':'form-control'}),'Goal':forms.Select(attrs={'class':'form-control'}),'units':forms.Select(attrs={'class':'form-control'}),'gender':forms.Select(attrs={'class':'form-control'}),
              'height_feet':forms.NumberInput(attrs={'class':'form-control'}),'height_inch':forms.NumberInput(attrs={'class':'form-control'}),
              'weight':forms.NumberInput(attrs={'class':'form-control'}),'Age':forms.NumberInput(attrs={'class':'form-control'}),
              'Bodyfat':forms.Select(attrs={'class':'form-control'}),'Activity_level':forms.Select(attrs={'class':'form-control'}),'Primary_Diet':forms.Select(attrs={'class':'form-control'})}


class ContactForm(forms.ModelForm):
    class Meta:
        model = contactus
        fields = ['name','Answer','email']
        widgets={'name':forms.TextInput(attrs={'class':'form-control'}),'Answer':forms.TextInput(attrs={'class':'form-control'}),'email':forms.EmailInput(attrs={'class':'form-control'})}

class BuyNowBlock(forms.ModelForm):
    class Meta:
        model=BuyNow
        fields=['Full_Name','Email','Address','City','State','Zipcode','Name_on_Card','Card_Number','Exp_Month','Exp_Year','Cvv']
        widgets={'Full_Name':forms.TextInput(attrs={'class':'form-control'}),'Email':forms.EmailInput(attrs={'class':'form-control'}),
                 'Address':forms.TextInput(attrs={'class':'form-control'}),'City':forms.TextInput(attrs={'class':'form-control'}),
                 'State':forms.Select(attrs={'class':'form-control'}),'Zipcode':forms.NumberInput(attrs={'class':'form-control'}),
                 'Name_on_Card':forms.TextInput(attrs={'class':'form-control'}),'Card_Numder':forms.NumberInput(attrs={'class':'form-control'}),
                 'Exp_Month':forms.TextInput(attrs={'class':'form-control'},),'Exp_year':forms.NumberInput(attrs={'class':'form-control'}),
                 'Cvv':forms.NumberInput(attrs={'class':'form-control'})}

class SlotBlock(forms.ModelForm):
    class Meta:
        model = SLOT1
        fields = ['name','slot','date','phone','Doctor_specialization']
        widgets = {'name':forms.TextInput(attrs={'class':'form-control'}),'slot':forms.Select(attrs={'class':'form-control'}),
                   'date':forms.DateInput(attrs={'class':'form-control'}),'phone':forms.NumberInput(attrs={'class':'form-control'}),
                   'Doctor_specialization':forms.Select(attrs={'class':'form-control'})}