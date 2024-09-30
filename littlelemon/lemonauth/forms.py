from django import forms
from .models import CustomUser


class SignupForm(forms.ModelForm):
    password1 = forms.CharField(label='enter password' , widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label='confirm password' , widget=forms.PasswordInput(attrs={'class':'form-control'}))

    class Meta:
        model= CustomUser
        fields = ('first_name' , 'last_name' , 'user_name' , 'email')

    def password_match(self):
        password1= self.cleaned_data.get('password1')
        password2= self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('passwords not matchingg')
        
        return password2
    
    def saveto_db (self , commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit :
            user.save()
        return user



