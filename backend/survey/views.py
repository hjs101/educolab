from urllib import response
from requests import request
from rest_framework.decorators import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from accounts.serializers import UserNameSerializer
from accounts.models import SchoolInfo,UserInfo
from survey.serializers import SurveySerializer, QuestionSerializer, SurveyMainSerializer,QuestionDetailSerializer
from .models import SurveyList
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
import os, io


class SurveyTeacherMainView(APIView) :
    ## 권한 설정 부분(View단위)
    # permission_classes = (IsAuthenticated,)

    def get(self,req):
        if not req.user.userflag:
            return Response({"message" :"선생님만 접근 가능합니다."})
        
        ## 2. 쿼리로 작성자가 user인 설문조사 목록을 가져온다.
        teacher = UserInfo.objects.get(username=req.user.username)
        survey = teacher.survey_teacher.all()

        print(survey)
        # notices = Notice.objects.select_related('school').filter(school_id=schoolCode)
        
        ## 3. 시리얼라이저 변환
        survey_serializer = SurveyMainSerializer(survey, many=True)
        ## 4. 가져온 목록 반환
        return Response(survey_serializer.data)

class SurveyCreateView(APIView):
    def post(self, req):
        
        if not req.user.userflag:
            return Response({"message" :"선생님만 접근 가능합니다."})
        
        # 설문조사 등록하기 start
        survey_serializer = SurveySerializer(data=req.data['survey'])
        students = UserInfo.objects.filter(grade = req.data['survey']['grade'], class_field=req.data['survey']['class_field'], school=req.user.school, userflag=False);
        print(students)
        if survey_serializer.is_valid(raise_exception=True):
            survey = survey_serializer.save(target=students, teacher = req.user)
        # 설문조사 등록하기 end

        # 설문조사 문항 등록하기 start
        for question in req.data['question']:
            question_serializer = QuestionSerializer(data=question)
            if question_serializer.is_valid(raise_exception=True):
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

        return Response(question_serializer.data)

    def delete(self, req):
        survey_id = req.GET['survey_num']

        ## 설문조사 번호로 설문조사 인스턴스 가져오기
        survey = SurveyList.objects.get(pk=survey_id)

        survey.delete()
        return Response({"success":True})

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
        survey = SurveyList.objects.get(pk=self.survey_id)

        survey_serializer = SurveySerializer(survey, data=req.data)
        if survey_serializer.is_valid(raise_exception=True):
            survey = survey_serializer.save()

        
        notice_files = notice.notice_file.all()


        for question in req.data['question']:
            question_serializer = QuestionSerializer(data=question)
            if question_serializer.is_valid(raise_exception=True):
                question_serializer.save(survey=survey)

        files = req.FILES.getlist("files")

        for file in files:
            fp = Files.objects.create(notice=notice, atch_file=file)
            fp.save()
        res = Response()
        res.data = {
            'message' : "success",
        }
