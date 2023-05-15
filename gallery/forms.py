from django.forms import forms


class GelleryUploadForm(forms.Form):
    image = forms.FileField()
