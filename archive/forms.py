from django import forms

from .models import Comment


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['article', 'message', 'name', 'email']
        exclude = ['article']

    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        self.fields['message'].widget.attrs.update({
            'class': 'form-control w-100',
            'name': 'comment',
            'id': 'comment',
            'cols': 30,
            'rows': 9,
            'placeholder': 'Write Comment'
        })
        self.fields['name'].widget.attrs.update({
            'class': 'form-control',
            'name': 'name',
            'id': 'name',
            'type': 'text',
            'placeholder': 'Name'
        })
        self.fields['email'].widget.attrs.update({
            'class': 'form-control',
            'name': 'email',
            'id': 'email',
            'type': 'email',
            'placeholder': 'Email'
        })
