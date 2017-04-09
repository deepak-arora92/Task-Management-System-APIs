from django import forms

class LoginForm(forms.Form):
    name = forms.CharField(max_length=255, min_length=4, required=True)
    is_completed = forms.BooleanField(required=False)
    notes = forms.CharField(required=False)
    due_date = forms.DateTimeField(required=True)