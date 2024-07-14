from django import forms

from .models import Item

class NewItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ["name", "description", "price", "category", "image"]
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control",
                                           "placeholder": "Enter item name"}),
            "description": forms.Textarea(attrs={"class": "form-control",
                                                "placeholder": "Enter item description"}),
            "price": forms.NumberInput(attrs={"class": "form-control",
                                             "placeholder": "Enter item price"}),
            "category": forms.Select(attrs={"class": "form-control"}),
            "image": forms.FileInput(attrs={"class": "form-control"}),
        }

class EditItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ["name", "description", "price", "category", "image", "is_sold"]
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control",
                                           "placeholder": "Enter item name"}),
            "description": forms.Textarea(attrs={"class": "form-control",
                                                "placeholder": "Enter item description"}),
            "price": forms.NumberInput(attrs={"class": "form-control",
                                             "placeholder": "Enter item price"}),
            "category": forms.Select(attrs={"class": "form-control"}),
            "image": forms.FileInput(attrs={"class": "form-control"}),
            "is_sold": forms.CheckboxInput(attrs={"class": "form-check-input"}),
        }