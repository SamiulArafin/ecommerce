from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()


class ContactForm(forms.Form):
    full_name = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control",
        "placeholder": "Full Name"
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        "class": "form-control",
        "placeholder": "Email"
    }))
    message = forms.CharField(widget=forms.Textarea(attrs={
        "class": "form-control",
        "placeholder": "Your message"
    }))

    def clean_email(self):
        email_passed = self.cleaned_data.get("email")
        if not "gmail.com" in email_passed:
            raise forms.ValidationError("You have forgotten about gmail mail format")
        return email_passed

    def clean_full_name(self):
        data = self.cleaned_data.get("full_name")
        if "samiul" not in data:
            raise forms.ValidationError("Full name must be samiul")
        return data


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class RegisterForm(forms.Form):
    username = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(label="Confirm Password", widget=forms.PasswordInput)

    def clean_username(self):
        username = self.cleaned_data.get("username")
        query = User.objects.filter(username=username)
        if query.exists:
            raise forms.ValidationError("User already taken")
        return username

    def clean_email(self):
        email = self.cleaned_data.get("email")
        query = User.objects.filter(email=email)
        if query.exists:
            raise forms.ValidationError("Email already taken")
        return email

    def clean(self):
        data = self.cleaned_data
        password = self.cleaned_data.get("password")
        confirm_password = self.cleaned_data.get("confirm_password")
        if password != confirm_password:
            raise forms.ValidationError("Password Not matched")
        return data
