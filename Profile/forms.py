from django import forms
from .models import Contact_model_form
class contact_form(forms.ModelForm):
    class Meta:
        model=Contact_model_form
        fields=["full_name","email","subject","message"]
        labels=[("full_name,FullName"),("email","Email"),("subject","Subject"),("message","Message")]



