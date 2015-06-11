

from django import forms
from models import *




class edit_profile_first_and_last_name_form(forms.Form):
    first_name = forms.CharField(max_length=50, required=True)
    last_name = forms.CharField(max_length=50, required=True)
    email = forms.CharField(max_length=50, required=True)
    points = forms.IntegerField(max_value=250)
    twitter = forms.CharField(max_length=250, required=True)
    facebook = forms.CharField(max_length=250, required=True)
    linkedn = forms.CharField(max_length=250, required=True)
    googleplus = forms.CharField(max_length=250, required=True)
    hakkinda = forms.CharField(max_length=1000)
    bolum = forms.CharField(max_length=50)
    sinif = forms.IntegerField(max_value=4)

class edit_member_password_form(forms.Form):
    old_password = forms.CharField(max_length=50, widget=forms.PasswordInput())
    new_password = forms.CharField(max_length=50, widget=forms.PasswordInput())
    confirm_password = forms.CharField(max_length=50, widget=forms.PasswordInput())

class edit_member_profile_form(forms.Form):
    profile_photo = forms.ImageField()


class DocumentForm(forms.Form):
    docfile = forms.FileField(
        label='Select a file'
    )