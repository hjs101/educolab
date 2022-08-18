from urllib import response
from requests import request
from rest_framework.decorators import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from accounts.serializers import UserNameSerializer
from accounts.models import SchoolInfo,UserInfo
<<<<<<< HEAD
<<<<<<< HEAD
from .serializers import QuizMainSerializer, QuizSerializer, QuestionSerializer,QuestionDetailSerializer
=======
from .serializers import QuizMainSerializer, QuizSerializer, QuestionSerializer,QuestionDetailSerializer, QuestionUpdateSerializer
>>>>>>> b125449 (Refactor : 백엔드 Question update 수정)
from .models import QuizList
=======
from survey.serializers import SurveySerializer,QuestionStatDetailSerializer, QuestionSerializer, SurveyMainSerializer,QuestionDetailSerializer,QuestionStatSerializer, QuestionsAnswerSerializer
from .models import SurveyList, SurveyQuestions
>>>>>>> f25ab0c (Fix : AWS 파일 옮기기)
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
import os, io


<<<<<<< HEAD
class QuizMainView(APIView) :
=======
class SurveyTeacherMainView(APIView) :
>>>>>>> f25ab0c (Fix : AWS 파일 옮기기)
    ## 권한 설정 부분(View단위)
    # permission_classes = (IsAuthenticated,)

    def get(self,req):
        if not req.user.userflag:
            return Response({"message" :"선생님만 접근 가능합니다."})
        
        ## 2. 쿼리로 작성자가 user인 설문조사 목록을 가져온다.
        teacher = UserInfo.objects.get(username=req.user.username)
<<<<<<< HEAD
<<<<<<< HEAD
        quiz = teacher.quiz_teacher.all()
=======
        quiz = teacher.quiz_teacher.all().order_by('-updated_at')
>>>>>>> 7d09758 (Feat : 내림차순 정렬, 포인트 로그 관련 정보 수정)
        print(quiz)
        # notices = Notice.objects.select_related('school').filter(school_id=schoolCode)
        
        ## 3. 시리얼라이저 변환
        quiz_serializer = QuizMainSerializer(quiz, many=True)
        ## 4. 가져온 목록 반환
        return Response(quiz_serializer.data)
    
class QuizCreateView(APIView):
=======
        survey = teacher.survey_teacher.all()

        print(survey)
        # notices = Notice.objects.select_related('school').filter(school_id=schoolCode)
        
        ## 3. 시리얼라이저 변환
        survey_serializer = SurveyMainSerializer(survey, many=True)
        ## 4. 가져온 목록 반환
        return Response(survey_serializer.data)
    
class SurveyCreateView(APIView):
>>>>>>> f25ab0c (Fix : AWS 파일 옮기기)
    def post(self, req):

        if not req.user.userflag:
            return Response({"message" :"선생님만 접근 가능합니다."})
        

        
        # survey_serializer
        # 설문조사 등록하기 start
<<<<<<< HEAD
        quiz_serializer = QuizSerializer(data=req.data['quiz'])
        if quiz_serializer.is_valid(raise_exception=True):
            quiz = quiz_serializer.save(teacher = req.user)
=======
        survey_serializer = SurveySerializer(data=req.data['survey'])
        if req.data['survey']['grade'] == 0:
            students = UserInfo.objects.filter(school=req.user.school, userflag=False)
        elif req.data['survey']['class_field'] == 0:
            students = UserInfo.objects.filter(grade = req.data['survey']['grade'],school=req.user.school, userflag=False)
        else:
            students = UserInfo.objects.filter(grade = req.data['survey']['grade'], class_field=req.data['survey']['class_field'], school=req.user.school, userflag=False);
        print(students)
        if survey_serializer.is_valid(raise_exception=True):
            survey = survey_serializer.save(target=students, teacher = req.user)
>>>>>>> f25ab0c (Fix : AWS 파일 옮기기)
        # 설문조사 등록하기 end

        # 설문조사 문항 등록하기 start
        for question in req.data['question']:
            question_serializer = QuestionSerializer(data=question)
            if question_serializer.is_valid(raise_exception=True):
<<<<<<< HEAD
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
=======
                question_serializer.save(survey=survey)
        # 설문조사 문항 등록하기 end


        return Response({"success":True})
class SurveyDetailView(APIView):
    def get(self, req):
        ## 설문조사 번호 가져오기
        survey_id = req.GET['survey_num']

        ## 설문조사 번호로 설문조사 인스턴스 가져오기
        survey = SurveyList.objects.get(pk=survey_id)
        questions = survey.question_survey.all()
        ## 설문조사 시리얼라이저 생성
        question_serializer = QuestionDetailSerializer(questions, many=True)
        survey_name = [{"survey_name" : survey.title}]
        print(question_serializer.data)
        return Response(survey_name+question_serializer.data)

    def delete(self, req):
        survey_id = req.GET['survey_num']

        ## 설문조사 번호로 설문조사 인스턴스 가져오기
        survey = SurveyList.objects.get(pk=survey_id)
>>>>>>> f25ab0c (Fix : AWS 파일 옮기기)

        survey.delete()
        return Response({"success":True})

<<<<<<< HEAD

    def put(self, req):
        quiz_id = req.data['quiz_num']
        quiz = QuizList.objects.get(pk=quiz_id)
        quiz_serializer = QuizSerializer(quiz, data=req.data['quiz'])
        print(quiz_serializer)
        if quiz_serializer.is_valid(raise_exception=True):
            quiz = quiz_serializer.save(teacher = req.user)

        quiz_questions = quiz.question_quiz.all()

        quiz_questions.delete()
<<<<<<< HEAD
<<<<<<< HEAD
=======
class SurveyUpdateView(APIView):
    def get(self, req):
        ## 설문조사 번호 가져오기
        survey_id = req.GET['survey_num']

        ## 설문조사 번호로 설문조사 인스턴스 가져오기
        survey = SurveyList.objects.get(pk=survey_id)
        questions = survey.question_survey.all()
        ## 설문조사 시리얼라이저 생성
        question_serializer = QuestionDetailSerializer(questions, many=True)

        return Response(question_serializer.data)

    def put(self, req):
        survey_id = req.data['survey_num']
        survey = SurveyList.objects.get(pk=survey_id)

        survey_serializer = SurveySerializer(survey, data=req.data['survey'])

        if req.data['survey']['grade'] == 0:
            students = UserInfo.objects.filter(school=req.user.school, userflag=False)
        elif req.data['survey']['class_field'] == 0:
            students = UserInfo.objects.filter(grade = req.data['survey']['grade'],school=req.user.school, userflag=False)
        else:
            students = UserInfo.objects.filter(grade = req.data['survey']['grade'], class_field=req.data['survey']['class_field'], school=req.user.school, userflag=False);

        if survey_serializer.is_valid(raise_exception=True):
            survey = survey_serializer.save(target=students,teacher = req.user)

        survey_questions = survey.question_survey.all()

        survey_questions.delete()
>>>>>>> f25ab0c (Fix : AWS 파일 옮기기)

=======
        print(req.data)
>>>>>>> 1a24399 (Test : 퀴즈 테스느)
=======
>>>>>>> e2eb7b4 (Fix : 퀴즈 수정 부분 오류 수정)
        for question in req.data['question']:
            question_serializer = QuestionUpdateSerializer(data=question)
            if question_serializer.is_valid(raise_exception=True):
<<<<<<< HEAD
                question_serializer.save(quiz=quiz)
=======
                question_serializer.save(survey=survey)
>>>>>>> f25ab0c (Fix : AWS 파일 옮기기)

        res = Response()
        res.data = {
            'message' : "success",
        }
<<<<<<< HEAD
        return Response({"success" : True})
=======
        return Response({"success" : True})
>>>>>>> f25ab0c (Fix : AWS 파일 옮기기)
