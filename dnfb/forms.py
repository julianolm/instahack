from django import forms

class UserNameForm(forms.Form):
    username = forms.CharField(label='Instagram username', max_length=20,
                               widget=forms.TextInput(attrs={'placeholder':'neymarjr'}))