from django import forms
from .models import Customer, Post
from django.contrib.auth.forms import UserCreationForm, User

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(max_length=35, required=True)
    phone = forms.CharField(max_length=10, required=True)
    province = forms.CharField(max_length=15, required=True)
    district = forms.CharField(max_length=35, required=True)
    city = forms.CharField(max_length=45, required=True)
    ward = forms.IntegerField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "phone", "password1", "password2")

    def clean_email(self):
        email = self.cleaned_data["email"]
        if Customer.objects.filter(email = email).exists():
            raise forms.ValidationError("That Email already Exists, Please provide different Email")
        return email
    
    def clean_province(self):
        province = self.cleaned_data["province"]
        return province
    
    def clean_district(self):
        district = self.cleaned_data["district"]
        return district
    
    def clean_city(self):
        city = self.cleaned_data["city"]
        return city

    def clean_ward(self):
        ward = self.cleaned_data["ward"]
        return ward

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
            Customer.objects.create(
                user=user,
                phone=self.cleaned_data["phone"],
                province=self.cleaned_data["province"],
                district=self.cleaned_data["district"],
                city=self.cleaned_data["city"],
                ward=self.cleaned_data["ward"]
            )
        return user


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['text', 'level', 'category']
        widgets = {
            'text': forms.Textarea(attrs={'placeholder': 'Write down Problem', 'class':'post-content', 'spellcheck':'false'}),
            'level': forms.Select(attrs={'class': 'level'}),
            'category': forms.Select(attrs={'class':'category'}),
        }