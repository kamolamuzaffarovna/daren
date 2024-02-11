from django import forms

from .models import Contact


class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = ['name', 'email', 'subject', 'message']

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({
            'class': 'form-control',
            'name': 'name',
            'id': 'name',
            'type': 'text',
            'onfocus': "this.placeholder = ''",
            'onblur': "this.placeholder = 'Enter Message'",
            'placeholder': 'Enter your name'
        })
        self.fields['email'].widget.attrs.update({
            'class': 'form-control',
            'name': "email",
            'id': 'email',
            'type': "email",
            'onfocus': "this.placeholder = ''",
            'onblur': "this.placeholder = 'Enter email address'",
            'placeholder': 'Enter email'
        })
        self.fields['subject'].widget.attrs.update({
            'class': 'form-control',
            'name': "subject",
            'id': 'subject',
            'type': "text",
            'onfocus': "this.placeholder = ''",
            'onblur': "this.placeholder = 'Enter Subject'",
            'placeholder': 'Enter your subject'
        })
        self.fields['message'].widget.attrs.update({
            'class': 'form-control w-100',
            'name': "message",
            'id': 'message',
            'cols': 30,
            'rows': 9,
            'onfocus': "this.placeholder = ''",
            'onblur': "this.placeholder = 'Enter your name'",
            'placeholder': 'Enter message'
        })