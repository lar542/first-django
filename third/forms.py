from django.forms import ModelForm
from django import forms
from . models import Restaurant, Review
from django.utils.translation import gettext_lazy as _

# 평점의 선택지
REVIEW_POINT_CHOICES = (
    ('1', 1),
    ('2', 2),
    ('3', 3),
    ('4', 4),
    ('5', 5),
)


class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['point', 'comment', 'restaurant']
        labels = {
            'point': _('평점'),
            'comment': _('코멘트'),
        }
        widgets = {
            'restaurant': forms.HiddenInput(),  # 리뷰를 달 식당 정보는 사용자에게 보여지지 않도록 한다
            'point': forms.Select(choices=REVIEW_POINT_CHOICES)  # 선택지를 인자로 전달
        }
        help_texts = {
            'point': _('평점을 입력해주세요.'),
            'comment': _('코멘트를 입력해주세요.'),
        }


class RestaurantForm(ModelForm):
    class Meta:
        model = Restaurant
        fields = ['name', 'address', 'image', 'password']
        labels = {
            'name': _('이름'),
            'address': _('주소'),
            'image': _('이미지 url'),
            'password': _('게시물 비밀번호'),
        }
        help_texts = {
            'name': _('이름을 입력해주세요.'),
            'address': _('주소를 입력해주세요.'),
            'image': _('이미지 url을 입력해주세요.'),
            'password': _('비밀번호를 입력해주세요.'),
        }
        widgets = {
            'password': forms.PasswordInput()
        }
        error_messages = {
            'name': {
                'mex_length': _('이름은 30자 이하로 정해주세요.')
            },
            'image': {
                'max_length': _('이미지 주소의 길이가 너무 깁니다. 500자 이하로 정해주세요.')
            },
            'password': {
                'max_length': _('비밀번호가 너무 깁니다. 20자 이하로 정해주세요.')
            }
        }


# 수정하거나 삭제할 때는 게시물의 비밀번호를 update를 하면 안 되고
# 기존에 저장되어있는 비밀번호가 맞는지 검증만 하기 위해
# update할 때 비밀번호가 제외하고 나머지 필드만 update시킨다.
class UpdateRestaurantForm(RestaurantForm):
    class Meta:
        model = Restaurant
        exclude = ['password']