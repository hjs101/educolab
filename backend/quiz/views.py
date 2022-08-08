from urllib import response
from requests import request
from rest_framework.decorators import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from accounts.serializers import UserNameSerializer
from accounts.models import SchoolInfo,UserInfo
from .serializers import QuizMainSerializer, QuizSerializer, QuestionSerializer,QuestionDetailSerializer
from .models import QuizList
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
import os, io


class QuizMainView(APIView) :
    ## 권한 설정 부분(View단위)
    # permission_classes = (IsAuthenticated,)

    def get(self,req):
        if not req.user.userflag:
            return Response({"message" :"선생님만 접근 가능합니다."})
        
        ## 2. 쿼리로 작성자가 user인 설문조사 목록을 가져온다.
        teacher = UserInfo.objects.get(username=req.user.username)
        quiz = teacher.quiz_teacher.all()
        print(quiz)
        # notices = Notice.objects.select_related('school').filter(school_id=schoolCode)
        
        ## 3. 시리얼라이저 변환
        quiz_serializer = QuizMainSerializer(quiz, many=True)
        ## 4. 가져온 목록 반환
        return Response(quiz_serializer.data)
    
class QuizCreateView(APIView):
    def post(self, req):

        if not req.user.userflag:
            return Response({"message" :"선생님만 접근 가능합니다."})
        

        
        # survey_serializer
        # 설문조사 등록하기 start
        quiz_serializer = QuizSerializer(data=req.data['quiz'])
        if quiz_serializer.is_valid(raise_exception=True):
            quiz = quiz_serializer.save(teacher = req.user)
        # 설문조사 등록하기 end

        # 설문조사 문항 등록하기 start
        for question in req.data['question']:
            question_serializer = QuestionSerializer(data=question)
            if question_serializer.is_valid(raise_exception=True):
                question_serializer.save(quiz=quiz)
        # 설문조사 문항 등록하기 end

        return Response({"success":True})

class QuizDetailView(APIView):
    def get(self, req):
        ## 설문조사 번호 가져오기
        quiz_id = req.GET['quiz_num']

        ## 설문조사 번호로 설문조사 인스턴스 가져오기
        quiz = QuizList.objects.get(pk=quiz_id)
        questions = quiz.question_quiz.all()
        ## 설문조사 시리얼라이저 생성
        question_serializer = QuestionDetailSerializer(questions, many=True)
        quiz_name = [{"quiz_name" : quiz.title}]
        print(question_serializer.data)
        return Response(quiz_name+question_serializer.data)

    def delete(self, req):
        quiz_id = req.GET['quiz_num']

        ## 설문조사 번호로 설문조사 인스턴스 가져오기
        survey = QuizList.objects.get(pk=quiz_id)

        survey.delete()
        return Response({"success":True})


    def put(self, req):
        quiz_id = req.data['quiz_num']
        quiz = QuizList.objects.get(pk=quiz_id)

        quiz_serializer = QuizSerializer(quiz, data=req.data['quiz'])

        if quiz_serializer.is_valid(raise_exception=True):
            quiz = quiz_serializer.save(teacher = req.user)

        quiz_questions = quiz.question_survey.all()

        quiz_questions.delete()

        for question in req.data['question']:
            question_serializer = QuestionSerializer(data=question)
            if question_serializer.is_valid(raise_exception=True):
                question_serializer.save(quiz=quiz)

        res = Response()
        res.data = {
            'message' : "success",
        }
        return Response({"success" : True})
