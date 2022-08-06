from urllib import response
from requests import request
from rest_framework.decorators import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from accounts.serializers import UserNameSerializer
from accounts.models import SchoolInfo,UserInfo
from survey.serializers import SurveySerializer,QuestionStatDetailSerializer, QuestionSerializer, SurveyMainSerializer,QuestionDetailSerializer,QuestionStatSerializer, QuestionsAnswerSerializer
from .models import SurveyList, SurveyQuestions
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
        if req.data['survey']['grade'] == 0:
            students = UserInfo.objects.filter(school=req.user.school, userflag=False)
        elif req.data['survey']['class_field'] == 0:
            students = UserInfo.objects.filter(grade = req.data['survey']['grade'],school=req.user.school, userflag=False)
        else:
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
        survey_name = [{"survey_name" : survey.title}]
        print(question_serializer.data)
        return Response(survey_name+question_serializer.data)

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

        for question in req.data['question']:
            question_serializer = QuestionSerializer(data=question)
            if question_serializer.is_valid(raise_exception=True):
                question_serializer.save(survey=survey)

        res = Response()
        res.data = {
            'message' : "success",
        }
        return Response({"success" : True})
class SurveyStatView(APIView):
    def get(self, req):
        survey_id = req.GET['survey_num']
        survey = SurveyList.objects.get(pk=survey_id)

        survey_questions = survey.question_survey.all()
        print(survey_questions)
        question_serializer = QuestionStatSerializer(survey_questions,many=True)
        res = Response({
            "survey_title" : survey.title,
            "questions" : question_serializer.data
        })
        return res

class SurveyStatDetailView(APIView):
    def get(self, req):
        question_id = req.GET['question_num']
        question = SurveyQuestions.objects.get(pk=question_id)

        answers = question.question_answers.all()
        answer_serializer = QuestionStatDetailSerializer(answers,many=True)
        res = Response(answer_serializer.data)
        return res
        ##survey.title

## 설문 제출 누적시키기
class SurveySubmitView(APIView):
    def post(self, req):

        answers = req.data['answers']
        survey = SurveyList.objects.get(id=req.data['survey_num'])
        
        userauth = survey.target.filter(username=req.user.username).exists()
        if not userauth:
            return Response({"message" : "설문 제출 자격이 없습니다."})

        done =  survey.done_target.filter(username=req.user.username).exists()
        print(done)
        if done:
            return Response({"message" : "이미 제출하셨습니다."})
        for answer in answers:
            print(answer)
            question = SurveyQuestions.objects.get(id=answer['id'])
            

            
            if question.multiple_bogi is not None:
                if answer['answer'] == 1:
                    question.num1 +=1
                elif answer['answer'] == 2:
                    question.num2 +=1
                elif answer['answer'] == 3:
                    question.num3 +=1
                elif answer['answer'] == 4:
                    question.num4 +=1
                elif answer['answer'] == 5:
                    question.num5 +=1
                else:
                    return Response({"message" : "정상적인 값을 입력해주세요"})
            else:
                content = {'content' : answer['answer']}
                answer_serializer = QuestionsAnswerSerializer(data=content)
                if answer_serializer.is_valid(raise_exception=True):
                    answer_serializer.save(question=question)
            
            question.save()
            survey.done_target.add(req.user)

        return Response({"success":True})