from django import forms


class UserForm(forms.Form):
    username = forms.CharField(label='Nazwa użytkownika', max_length=128, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': "Username", 'autofocus': ''}))
    password = forms.CharField(label='Hasło', max_length=256,
                               widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': "Password"}))


class RegisterForm(forms.Form):
    gender = (
        ('Meżczyzna', "♂"),
        ('Kobieta', "♀"),
    )

    username = forms.CharField(label="Nazwa użytkownika", max_length=128, widget=forms.TextInput(attrs={'class': 'form-control', }))
    password1 = forms.CharField(label="Hasło", max_length=256, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label="Powtórz haslo", max_length=256,
                                widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label="Email", widget=forms.EmailInput(attrs={'class': 'form-control'}))
    sex = forms.ChoiceField(label="Płeć", choices=gender)
