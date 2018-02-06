from django import forms

from .models import ContactCreate


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactCreate
        fields = (
            'name',
            'mobile_phone',
            'phone',
            'email',
            'address'
            # 'image'
        )
        labels = {'text': ''}
