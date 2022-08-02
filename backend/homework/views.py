from django.shortcuts import render
from rest_framework.views import APIView 
from rest_framework.response import Response

from .models import StudentHomework, TeacherHomework, Files, SubmitHomework
from accounts.models import SchoolInfo, UserInfo
from .serializers import StudentHomeworkMainSerializer, TeacherHomeworkCreateSerializer, StudentHomeworkCreateSerializer, TeacherHomeworkMainSerializer

# Create your views here.
class HomeworkMainView(APIView):
    
    def get(self, request):
        if request.user.userflag:
            teacher = UserInfo.objects.get(username=request.user.username)
            homework = teacher.T_homework.all()

            print(homework)

            homework_serializer = TeacherHomeworkMainSerializer(homework, many=True)
            return Response(homework_serializer.data)
        
        elif request.user.userflag:
            student = UserInfo.objects.get(username=request.user.username)
            homework = student.S_homework.all()

            homework_serializer = StudentHomeworkMainSerializer(homework, many=True)
            return Response(homework_serializer.data)
            
            


class HomeworkCreateView(APIView):
    
    def post(self, request):
        if request.user.userflag == 0:
            homework_serializer = StudentHomeworkCreateSerializer(data=request.data)
            if homework_serializer.is_valid(raise_exception=True):
                homework_serializer.save(student=request.user)

                files = request.FILES.getlist("files")
                for file in files:
                    fp = Files.objects.create(student_homework=homework,atch_file=file,atch_file_name=file)
                    fp.save()
                
                submit = SubmitHomework.objects.create(student_homework=homework,student=student)
                submit.save()

        elif request.user.userflag == 1:
            homework_serializer = TeacherHomeworkCreateSerializer(data=request.data)
            if homework_serializer.is_valid(raise_exception=True):
                school_student= SchoolInfo.objects.get(code=request.user.school)
                students = school_student.filter(grade=homework_serializer.validated_data['grade'],class_field=homework_serializer.validated_data['class_field'])
                homework = homework_serializer.save(teacher=request.user,target=students)
                
                files = request.FILES.getlist("files")
                for file in files:
                    fp = Files.objects.create(teacher_homework=homework,atch_file=file,atch_file_name=file)
                    fp.save()
                
                for student in students:
                    submit = SubmitHomework.objects.create(student=student,teacher_homework=homework)
                    submit.save()

        context = {
            "success" : True,
            "pk" : homework.pk
        }
        return Response(context)

class HomeworkDetailView(APIView):
    def get(self, request):
        homework_pk = request.GET.get('pk')
        teacher_flag = request.GET.get('teacher')
        if teacher_flag:
            homework = TeacherHomework.objects.get(pk=homework_pk)
        
        elif teacher_flag == None:
            homework = StudentHomework.objects.get(pk=homework_pk)
        # serializer를 통해서 어디까지 보여줄지 정해야함.
        # 각각 따로 만들어야함
        return Response(homework)
    
    def put(self, request):
        homework_pk = request.GET.get('pk')
        teacher_flag = request.GET.get('teacher')
        if request.user.userflag:
            homework = TeacherHomework.objects.get(pk=homework_pk)
            homework_serializer = TeacherHomeworkCreateSerializer(instance = homework,data=request.data)
        
        else:
            homework = StudentHomework.objects.get(pk=homework_pk)
            homework_serializer = StudentHomeworkCreateSerializer(instance = homework,data=request.data)
        
    def delete(self, request):
        homework_pk = request.GET.get('pk')
        teacher_flag = request.GET.get('teacher')
        if teacher_flag:
            homework = TeacherHomework.objects.get(pk=homework_pk)
        
        elif teacher_flag == None:
            homework = StudentHomework.objects.get(pk=homework_pk)
        
        homework.delete()
        context = {
            "success" : True,
            "message" : "삭제되었습니다"
        }
        return Response(context)