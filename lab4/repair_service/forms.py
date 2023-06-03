from django import forms
from .models import Service, ServiceTag


class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = "__all__"
        #
        # attrs = {'class': 'form-control'}
        # widgets = {
        #     'name': forms.TextInput(attrs=attrs),
        #     'price': forms.NumberInput(attrs=attrs),
        #     'about': forms.TextInput(attrs=attrs),
        #     # 'service_tags': forms.SelectMultiple(attrs=attrs),
        #     'image': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
        # }
