from django import forms
from django.contrib.auth.models import User

from .models import Message

class MessageForm(forms.ModelForm):
    reciever = forms.CharField()
    
    class Meta:
        model = Message
        fields = ['reciever', 'subject', 'body']
        widgets = {
            'body': forms.Textarea(attrs={'rows': 5,
                                          'class': 'form-control',
                                          'placeholder': 'Message'}),
            'reciever': forms.TextInput(attrs={'class': 'form-control',
                                             'placeholder': 'Enter recipient username'}),
            'subject': forms.TextInput(attrs={'class': 'form-control',
                                              'placeholder': 'Subject'}),
        }