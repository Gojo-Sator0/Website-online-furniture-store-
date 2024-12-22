from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm

from users.models import User


class UserLoginForm(AuthenticationForm):

    class Meta:
        model = User
        fields = ['username','password']

    username = forms.CharField()
    password = forms.CharField()


class UserRegisterForm(UserCreationForm):

    class Meta:
        model = User
        fields = (
            'username',
            'password1',
            'password2',
            'email',
            'first_name',
            'last_name'
        )

    username = forms.CharField()
    password1 = forms.CharField()
    password2 = forms.CharField()
    email = forms.EmailField()
    first_name = forms.CharField()
    last_name = forms.CharField()

class UserProfileForm(UserChangeForm):
        class Meta:
            model = User
            fields = (
                'image',
                'first_name',
                'last_name',
                'email',
                'username',
            )

        image = forms.ImageField(required=False)
        first_name = forms.CharField()
        last_name = forms.CharField()
        email = forms.EmailField()
        username = forms.CharField()



        # image = forms.ImageField(
        #      widget=forms.FileInput(attrs={
        #           "class":"form-control mt-3", 
        #           }), required=False
        # )
        
        # first_name = forms.CharField(
        #      widget=forms.TextInput(attrs={
        #           "class":"form-control mt-3", 
        #           "placeholder":"Введите ваше имя"
        #           }), required=False
        # )

        # last_name = forms.CharField(
        #     widget=forms.TextInput(attrs={
        #          "class":"form-control mt-3", 
        #          "placeholder":"Введите вашу фамилию"
        #          }), required=False
        # )

        # email = forms.EmailField(
        #     widget=forms.EmailInput(attrs={
        #          "class":"form-control mt-3", 
        #          "placeholder":"Введите вашу почту"
        #          }), required=False
        # )

        # username = forms.CharField(
        #     widget=forms.TextInput(attrs={
        #          "class":"form-control mt-3", 
        #          "placeholder":"Введите ваше имя пользователя"
        #          }), required=False
        # )

        


    # username = forms.CharField(
    #     label='Имя',
    #     widget=forms.TextInput(attrs={
    #         "autofocus":True,
    #         'class':'form-control',
    #         'placeholder':'Введите ваше имя пользователя'
    #         }))
    
    # password = forms.CharField(
    #     label='Пароль',
    #     widget=forms.PasswordInput(attrs={
    #         "autocomplete":"current-password",
    #         'class':'form-control',
    #         'placeholder':'Введите ваш пароль'
    #         }))


