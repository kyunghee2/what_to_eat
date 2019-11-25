from django import forms
from .models import Restaurant, Comment


class CommentForm(forms.ModelForm):
   
    # content = forms.CharField(
    #     label='댓글',
    #     widget=forms.Textarea(
    #         attrs={
    #             'class':'content',
    #             'placeholder':'댓글입력해',
    #             'rows':1,
    #             'cols':30,
    #         }
    #     )
    # )
    class Meta:
        model = Comment
        fields = ('score','content',)      #원하는것만 필드에 나타나게 할 수 있다 ( 'title','content',)

