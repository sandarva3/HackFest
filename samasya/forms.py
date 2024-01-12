from django import forms
from .models import Customer
from django.contrib.auth.forms import UserCreationForm, User

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(max_length= 35,required=True)
    phone = forms.CharField(max_length= 10, required=True)
    class Meta:
        model = User
        fields = ("username", "email", "phone", "password1", "password2")

    def clean_email(self):
        email = self.cleaned_data["email"]
        if Customer.objects.filter(email = email).exists():
            raise forms.ValidationError("That Email already Exists, Please provide different Email")
        return email
    
    def clean_phone(self):
        phone = self.cleaned_data["phone"]
        if Customer.objects.filter(phone = phone).exists():
            raise forms.ValidationError("That Phone number already Exists, Please provide different Email address")
        return phone
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        user.phone = self.cleaned_data["phone"]
        if commit:
            user.save()
            customer = Customer.objects.create(user=user, phone=self.cleaned_data["email"])
        return user