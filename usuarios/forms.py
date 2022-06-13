from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
User = get_user_model()

# Formulario para registro de usuarios
class RegistrarUsuario(UserCreationForm):
    first_name = forms.CharField(label='Nombre', max_length=100, widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(label='Apellido', max_length=100, widget=forms.TextInput(attrs={'class':'form-control'}))
    username = forms.CharField(label='Nombre de usuario', min_length=5, max_length=150, widget=forms.TextInput(attrs={'class':'form-control'})) 
    email = forms.EmailField(label='E-mail', widget=forms.EmailInput(attrs={'class':'form-control'}))  
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput(attrs={'class': 'form-control'}))  
    password2 = forms.CharField(label='Confirma contraseña', widget=forms.PasswordInput(attrs={'class': 'form-control'}))  

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')

    def save(self, commit=True):
        user = super(RegistrarUsuario, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']

        if commit:
            user.save()
        return user