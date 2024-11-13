from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import get_user_model

CustomUser = get_user_model()

class LoginForm(AuthenticationForm):
    username = forms.CharField(
        label="Nom d'utilisateur",
        widget=forms.TextInput(attrs={
            'class': 'w-full p-3 pl-10 border rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500',
            'placeholder': "Votre nom d'utilisateur"
        })
    )
    password = forms.CharField(
        label="Mot de passe",
        widget=forms.PasswordInput(attrs={
            'class': 'w-full p-3 pl-10 border rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500',
            'placeholder': "Votre mot de passe"
        })
    )

class SignupForm(UserCreationForm):
    username = forms.CharField(
        label="Nom d'utilisateur",
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'w-full p-3 pl-10 border rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500',
            'placeholder': "Votre nom d'utilisateur"
        })
    )
    email = forms.EmailField(
        label="Email",
        required=True,
        widget=forms.EmailInput(attrs={
            'class': 'w-full p-3 pl-10 border rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500',
            'placeholder': "Votre email"
        })
    )
    phone_number = forms.CharField(
        label="Numéro de téléphone",
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'w-full p-3 pl-10 border rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500',
            'placeholder': "Votre numéro de téléphone"
        })
    )
    password1 = forms.CharField(
        label="Mot de passe",
        widget=forms.PasswordInput(attrs={
            'class': 'w-full p-3 pl-10 border rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500',
            'placeholder': "Votre mot de passe"
        })
    )
    password2 = forms.CharField(
        label="Confirmer le mot de passe",
        widget=forms.PasswordInput(attrs={
            'class': 'w-full p-3 pl-10 border rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500',
            'placeholder': "Confirmer le mot de passe"
        })
    )

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'phone_number', 'password1', 'password2')

class CustomUserUpdateForm(forms.ModelForm):
    username = forms.CharField(
        label="Nom d'utilisateur",
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'w-full p-3 pl-10 border rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500',
            'placeholder': "Votre nom d'utilisateur"
        })
    )
    email = forms.EmailField(
        label="Email",
        required=True,
        widget=forms.EmailInput(attrs={
            'class': 'w-full p-3 pl-10 border rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500',
            'placeholder': "Votre email"
        })
    )
    phone_number = forms.CharField(
        label="Numéro de téléphone",
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'w-full p-3 pl-10 border rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500',
            'placeholder': "Votre numéro de téléphone"
        })
    )
    first_name = forms.CharField(
        label="Prénom",
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'w-full p-3 pl-10 border rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500',
            'placeholder': "Votre prénom"
        })
    )
    last_name = forms.CharField(
        label="Nom",
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'w-full p-3 pl-10 border rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500',
            'placeholder': "Votre nom"
        })
    )
    date_of_birth = forms.DateField(
        label="Date de naissance",
        required=False,
        widget=forms.DateInput(attrs={
            'type': 'date',
            'class': 'w-full p-3 pl-10 border rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500'
        })
    )

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'phone_number', 'first_name', 'last_name', 'date_of_birth']

    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')
        # Ajoute des validations spécifiques si nécessaire
        return phone_number