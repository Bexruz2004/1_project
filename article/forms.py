from django import forms
from .models import (
    Commentary,

)


class CommentaryForm(forms.ModelForm):
    class Meta:
        model = Commentary
        fields = ['name', 'image', 'message']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['message'].widget.attrs.update({
            'class': "form-control w-100",
            "cols": 30,
            "rows": 9,
            "name": "message",
            'placeholder': 'Write Comment',
        })

        self.fields['image'].widget.attrs.update({
            'class': "form-control",
            "name": "image",
        })

        self.fields['name'].widget.attrs.update({
            'class': "form-control",
            'placeholder': 'Name',
            "name": "name",
        })
