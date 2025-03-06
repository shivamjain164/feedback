from django import forms

class Uploadform(forms.Form):
    user_file = forms.FileField()