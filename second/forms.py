from django import forms
from django.forms import ModelForm
from second.models import Post
from django.utils.translation import gettext_lazy as _

# class PostForm(forms.Form): # django Form 클래스를 상속
#     # label : 폼에서 텍스트로 보여지는 것을 설정
#     title = forms.CharField(label="제목", max_length=200)
#     content = forms.CharField(label="내용", widget=forms.Textarea)

class PostForm(ModelForm): # ModelForm을 상속
    class Meta:
        model = Post # 사용할 클래스
        fields = ['title', 'content'] # 압력받을 필드
        labels = {
            'title': _("제목"), # gettext_lazy는 "제목"이라는 텍스트를 가져오는 메소드
            "content": _("내용"),
        }
        help_texts = {
            'title': _("제목을 입력해주세요."),
            "content": _("내용을 입력해주세요."),
        }
        error_message = {
            "name": {
                "max_length": _("제목이 너무 깁니다. 30자 이하로 작성해주세요.")
            }
        }