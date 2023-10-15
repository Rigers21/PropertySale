from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(label='Your Name')
    email = forms.EmailField(label='Your email')
    message = forms.CharField(label='Your message', widget=forms.Textarea)
