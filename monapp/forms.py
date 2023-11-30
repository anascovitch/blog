
from django import forms
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from .models import CustomUser
from .models import ImagePost

# Puis ajustez votre formulaire pour utiliser CustomUser
class CustomUserCreationForm(UserCreationForm):
    birth_date = forms.DateField(required=False, help_text='Optional.')   
   
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ('birth_date',)


    def save(self, commit=True):
        user = super().save(commit=False)
        user.birth_date = self.cleaned_data['birth_date']
        if commit:
            user.save()
           
        return user



class ImagePostForm(forms.ModelForm):
    class Meta:
        model = ImagePost
        fields = ['titre', 'description', 'image']


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ['username','email', 'first_name', 'last_name', 'birth_date']
        
