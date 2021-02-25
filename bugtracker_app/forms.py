from django import forms 

class LoginForm(forms.Form):
    username = forms.CharField(max_length=40)
    password = forms.CharField(widget=forms.PasswordInput)

STATUS_CHOICES = (
    ('New', 'NEW'),
    ('In Progress','INPROGRESS'),
    ('Done','DONE'),
    ('Invalid', 'INVALID')
    )

class AddTicketForm(forms.Form):
    title = forms.CharField(max_length=50)
    description = forms.CharField(widget=forms.Textarea)
    