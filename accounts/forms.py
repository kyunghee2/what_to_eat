from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserChangeForm,UserCreationForm

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        # User클래스를 바로 가져와서 사용하는 것이 아니라
        # get_user_model()을 사용해서 User 클래스를 참조
        model = get_user_model()
        # UserChangeForm -> User 클래스 -> AbstractUser 클래스
        fields = ('email','last_name','first_name')

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ('username','password1','password2','email',)
