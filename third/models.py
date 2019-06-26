from django.db import models

# Create your models here.
class Restaurant(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=200)

    # 속성을 추가할 때 default 속성을 지정하면 기존에 이미 저장되어 있는 레코드들의 컬럼 값들은
    # default에서 지정된 값으로 채워진다.
    image = models.CharField(max_length=500, default=None, null=True)
    password = models.CharField(max_length=20, default=None, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)


class Review(models.Model):
    point = models.IntegerField()
    comment = models.CharField(max_length=500)

    # Restaurant 모델의 ForeignKey로 선언
    # on_delete에 CASCADE로 지정하면 식당이 삭제되면 같이 삭제된다.
    # SET_NULL은 Restaurant가 삭제될 때 이 모델에 의존한 Review는 NULL 처리함을 의미
    # SET_DEFAULT는 Restaurant가 삭제될 때 이 모델에 의존한 Review는 디폴트 값으로 자동으로 업데이트 처리
    # DO_NOTHING는 아무 조치도 안 함
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
