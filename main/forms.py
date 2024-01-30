from django import forms


class AuthForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'type':'username', 'placeholder':'Имя пользователя'}))
    password = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'type':'password', 'placeholder':'Пароль'}))

class RegForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'username', 'type': 'username', 'placeholder': 'Придумай имя пользователя'})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'name': 'password', 'type': 'password', 'placeholder': 'Введи свой пароль'})
    )
    email = forms.EmailField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'email', 'name': 'email', 'placeholder': 'Электронная почта'})
    )
    is_teacher = forms.BooleanField(
        label='Вы учитель?', required=False, widget=forms.CheckboxInput(attrs={'class': 'form-check-input'})
    )
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'first_name', 'type': 'input', 'placeholder': 'Имя'})
    )
    last_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'last_name', 'type': 'input', 'placeholder': 'Фамилия'})
    )
    surname = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'surname', 'type': 'input', 'placeholder': 'Отчество'})
    )