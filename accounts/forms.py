from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserChangeForm,UserCreationForm

class CustomUserChangeForm(UserChangeForm):
    comp_addr = forms.CharField(
        label='회사주소',
        widget=forms.Textarea(
            attrs={
                'class':'comp_addr',
                'placeholder':'주소',
                'rows':2,
                'cols':10,
            }
        )
    )

    class Meta:
        # User클래스를 바로 가져와서 사용하는 것이 아니라
        # get_user_model()을 사용해서 User 클래스를 참조
        model = get_user_model()
        # UserChangeForm -> User 클래스 -> AbstractUser 클래스
        fields = (
            'username','email', 'comp_addr', 
            'lunch_noti_enable', 'schedule_noti_enable',
            )

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ('username','email', 'password1', 'password2',)
