from django import forms

class PostForm(forms.Form): # django Form 클래스를 상속
    # label : 폼에서 텍스트로 보여지는 것을 설정
    title = forms.CharField(label="제목", max_length=200)
    content = forms.CharField(label="내용", widget=forms.Textarea)