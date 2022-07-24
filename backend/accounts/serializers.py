from rest_framework import serializers
from . import models
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

class UserinfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.UserInfo
        fields = '__all__'

# jwt token 결과 커스텀 
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

    # response 커스텀
    default_error_messages = {
        'no_active_account': {'message':'username or password is incorrect!',
                            'success': False,
                            'status' : 401}
    }
    # 유효성 검사
    def validate(self, attrs):
        data = super().validate(attrs)

        refresh = self.get_token(self.user)

        # response에 추가할 key값
        data['username'] = self.user.username
        data['userFlag'] = self.user.userFlag
        print(data)
        return data


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer