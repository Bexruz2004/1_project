from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'message', 'subject', 'id']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({
            "class": "form-control",
            "name": "name",
            "id": "name",
            "type": "text",
            "placeholder": "Enter Name"
        })

        self.fields["email"].widget.attrs.update({
            "class": "form-control",
            "name": "email",
            "id": "email",
            "type": "email",
            "placeholder": "Enter Email"
        })

        self.fields['message'].widget.attrs.update({
            "class": "form-control w-100",
            "id": "message",
            "cols": 30,
            'rows': 9,
            "placeholder": "Enter Message"

        })

        self.fields['subject'].widget.attrs.update({
            "class": "form-control",
            "name": "subject",
            "id": "subject",
            "type": "text",
            "placeholder": "Enter Subject"
        })
