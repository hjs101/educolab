from rest_framework.decorators import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated 
class NoticeMainView(APIView) :
    
    # permission_classes = (IsAuthenticated,)

    def post(self,req):
    

        # email = req.data['email']
        # password = req.data['password']

        ## 0. 로그인한 사용자인지 인증(자동?)

        ## 1. request로부터 학교 코드를 받는다.

        ## 2. 쿼리로 학교 코드가 req에서 받은 학교 코드인 사람이 작성자인 공지사항 목록을 가져온다.

        ## 3. 가져온 목록 반환

        res = Response()



        return res