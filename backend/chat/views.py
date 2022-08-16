# chat/views.py
from django.shortcuts import render
from django.core.mail import send_mail
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import status
from django.shortcuts import render
from django.utils.safestring import mark_safe
from accounts.models import UserInfo
from quiz.models import QuizQuestions
from .serializers import QuizAnswerSerializer
from .models import QuizRoom, QuizUser, QuizAnswer
from django.db.models import Count
import json

def index(request):
    return render(request, 'chat/index.html', {})

def room(request, room_name):
    return render(request, 'chat/room.html', {
        'room_name_json': mark_safe(json.dumps(room_name))
    })
    
class AnswerSubmitView(APIView):
    def post(self, req):
        answer = int(req.data['answer'])
        quiz_num = req.data['quiz_question_id']
        room_num = req.data['room_num']
        question = QuizQuestions.objects.get(id=quiz_num)
        answerflag = False
        if question.answer == answer:
            print("kkk")
            answerflag = True
            quiz_answer_serializer = QuizAnswerSerializer(data = {"answerflag":answerflag})
            room = QuizRoom.objects.get(roomnum=room_num)
            quizuser = QuizUser.objects.get(room_id=room_num,student=req.user)
            if quiz_answer_serializer.is_valid(raise_exception=True):
                quiz_answer_serializer.save(question=question, room=room, student=req.user,quizuser=quizuser)

        return Response({"answerflag" : answerflag})

class ScoreAddView(APIView):
    def get(self, req):
        qestion_num = req.GET['quiz_question_id']
        room_num = req.GET['room_num']
        quiz_answer_user = QuizAnswer.objects.filter(room=room_num,question=qestion_num).order_by('id')
        count = 0
        ans_cnt = 0
        for user in quiz_answer_user:
            ans_cnt +=1
            user.quizuser.score += (100 - count*10)
            user.quizuser.save()
            if count < 5:
                count +=1
        return Response({"success":True, "ans_cnt":ans_cnt})
class RankScoreView(APIView):
    def get(self, req):
        room_num = req.GET['room_num']
        room = QuizRoom.objects.get(roomnum=room_num)
        students = room.getuser_byroom.order_by('-score')
        data = []
        cnt = 1;
        score_log = students[0].score
        acc = 0;
        for student in students:
            if score_log == student.score and student != students[0]:
                acc +=1
            elif  student == students[0]:
                cnt=1
            else :
                cnt +=1
                cnt += acc
                acc = 0
            data.append({
                "rank" : cnt,
                "title" : "" if student.student.wear_title is None else student.student.wear_title.title ,
                "name" : student.student.name,
                "score" : student.score,
            })

            if cnt > 5:
                break
        return Response({
            "ranks" : data,
        })

class StudentResultView(APIView):
    def get(self, req):
        room_num = req.GET['room_num']
        user = QuizUser.objects.get(room_id=room_num, student=req.user)
        answers = user.quiz_user.all()
        cnt = len(user.room.quiz.question_quiz.all())
        data = []
        for answer in answers:
            data.append(answer.question.question_number)
        print(answers)
        room = QuizRoom.objects.get(roomnum=room_num)
        students = room.getuser_byroom.order_by('-score')
        rank = 1
        print(students)
        for student in students:
            print("lll")
            if student.student == req.user:
                print("kkk")
                break;
            rank+=1
        print(rank)
        
        return Response({
            "question_cnt" : cnt,
            "rank" : rank,
            "answers" : data,
        })