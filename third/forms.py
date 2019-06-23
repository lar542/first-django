from django.forms import ModelForm
from . models import Restaurant
from django.utils.translation import gettext_lazy as _

class RestaurantForm(ModelForm):
    class Meta:
        model = Restaurant
        fields = ['name', 'address']
        labels = {
            'name': _('이름'),
            'address': _('주소'),
        }
        help_texts = {
            'name': _('이름을 입력해주세요.'),
            'address': _('주소를 입력해주세요.'),
        }
        error_messages = {
            'name': {
                'mex_length': _('이름은 30자 이하로 정해주세요.')
            }
        }