from django import forms

class Login(forms.Form):
    your_phone = forms.CharField(max_length=10,required=True,widget=forms.TextInput(attrs={'placeholder': 'Мобильный телефон','value':'+7(***)*******'}),label='' ,initial='+7'  )  
    your_password=forms.CharField(max_length=25, required=True,widget=forms.TextInput(attrs={'placeholder': 'Пароль','type':'password'}),label='')
