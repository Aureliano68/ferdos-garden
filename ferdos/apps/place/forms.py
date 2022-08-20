from tkinter import Widget
from django import forms

# ---------------------------------------------------------------------------------------------------------------

class form_message(forms.Form):
    full_name=forms.CharField(label='نام و نام خانوادگی',required=True)
    email=forms.EmailField(label=" ایمیل",required=False)
    subject=forms.CharField(label=" عنوان پیام")
    message=forms.CharField(label='متن پیام',widget=forms.Textarea)
    
    