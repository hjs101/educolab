from django.shortcuts import render
from rest_framework.views import APIView 
from rest_framework.response import Response

from .models import StudentHomework, TeacherHomework, Files, SubmitHomework
from accounts.models import SchoolInfo, UserInfo
from .serializers import StudentHomeworkDetailSerializer, StudentHomeworkMainSerializer, SubmitHomeworksubmitSerializer, TeacherHomeworkCreateSerializer, StudentHomeworkCreateSerializer, TeacherHomeworkDetailSerializer, TeacherHomeworkMainSerializer

from datetime import datetime
# Create your views here.
class HomeworkMainView(APIView):
    
    def get(self, request):
<<<<<<< HEAD
        if request.user.userflag:
=======
        today = datetime.now().date()
        if request.user.userflag == True:
>>>>>>> 7affbf9 (feat : 과제 메인 기능 구현)
            teacher = UserInfo.objects.get(username=request.user.username)
            homeworks = teacher.T_homework.all()
            notdone_homework = []
            done_notcheck_homework = []
            all_done_homework = []
            for homework in homeworks:
                print(homework.deadline, today)
                if homework.deadline >= today:
                    notdone_homework.append(homework)
                elif homework.check_flag == False:
                    done_notcheck_homework.append(homework)
                else:
                    all_done_homework.append(homework)
            
            student_homeworks = teacher.homeroom_T.filter(submit_flag=True,agreement=False)

<<<<<<< HEAD
            print(notdone_homework)
            print(done_notcheck_homework)
            print(all_done_homework)
<<<<<<< HEAD

<<<<<<< HEAD
            print(homework)

            homework_serializer = TeacherHomeworkMainSerializer(homework, many=True)
            return Response(homework_serializer.data)
=======
=======
            print(student_homeworks)
>>>>>>> 7affbf9 (feat : 과제 메인 기능 구현)
=======
>>>>>>> 7306741 (feat : 과제 제출 기능 구현)
            notdone_homework_serializer = TeacherHomeworkMainSerializer(notdone_homework, many=True)
            done_notcheck_homework_serializer = TeacherHomeworkMainSerializer(done_notcheck_homework, many=True)
            all_done_homework_serializer = TeacherHomeworkMainSerializer(all_done_homework, many=True)
            student_homeworks_serizlizer = StudentHomeworkMainSerializer(student_homeworks, many=True)
            
            context = {
                "not_done" : notdone_homework_serializer.data,
                "done_notcheck" : done_notcheck_homework_serializer.data,
                "all_done" : all_done_homework_serializer.data,
                "students" : student_homeworks_serizlizer.data
            }
            return Response(context)
>>>>>>> e59250a (feat: 과제 메인페이지 기능 어느정도 구현 완료 나머지는 상의필요)
        
        elif request.user.userflag:
            student = UserInfo.objects.get(username=request.user.username)
            homeworks = student.teacher_homework.all()

            notdone_homework = []
            done_homework = []

            for homework in homeworks:
                if homework.deadline >= today:
                    notdone_homework.append(homework)
                else:
                    done_homework.append(homework)
            
            my_homework = student.S_homework.all()

            notdone_homework_serializer = TeacherHomeworkMainSerializer(notdone_homework, many=True)
            done_homework_serialzier = TeacherHomeworkMainSerializer(done_homework, many=True)
            my_homework_serializer = StudentHomeworkMainSerializer(my_homework, many=True)
            context = {
                "notdone" : notdone_homework_serializer.data,
                "done" : done_homework_serialzier.data,
                "my_homework" : my_homework_serializer.data
            }
            return Response(context)
            
            


class HomeworkCreateView(APIView):
    
    def post(self, request):
        if request.user.userflag == 0:
            print(0)
            print(request.data)
            homework_serializer = StudentHomeworkCreateSerializer(data=request.data)
            
            if homework_serializer.is_valid(raise_exception=True):
                teacher = UserInfo.objects.get(class_field=request.user.class_field,grade=request.user.grade,userflag=True)
                homework = homework_serializer.save(student=request.user,teacher=teacher)

                files = request.FILES.getlist("files")
                for file in files:
                    fp = Files.objects.create(student_homework=homework,atch_file=file,atch_file_name=file)
                    fp.save()
                
                submit = SubmitHomework.objects.create(student_homework=homework,student=request.user)
                submit.save()

        elif request.user.userflag == 1:
            print(1)
            print(request.data)
            homework_serializer = TeacherHomeworkCreateSerializer(data=request.data)
            if homework_serializer.is_valid(raise_exception=True):
                print('valid')
                school = request.user.school
                print(school)
                school_student= school.school_student.all()
                print(school_student)
                students = school_student.filter(grade=homework_serializer.validated_data['grade'],class_field=homework_serializer.validated_data['class_field'])
                print(students)
                homework = homework_serializer.save(teacher=request.user,target=students)
                print(homework)
                files = request.FILES.getlist("files")
                print(files)
                for file in files:
                    print(file)
                    fp = Files.objects.create(teacher_homework=homework,atch_file=file,atch_file_name=file)
                    fp.save()
                
                for student in students:
                    print(student)
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
        teacher_flag = request.GET.get('teacher_flag')
        print(homework_pk, teacher_flag)
        if teacher_flag:
            homework = TeacherHomework.objects.get(id=homework_pk)
            homework_serializer = TeacherHomeworkDetailSerializer(homework)

        else:
            homework = StudentHomework.objects.get(id=homework_pk)
            homework_serializer = StudentHomeworkDetailSerializer(homework)
        

        # serializer를 통해서 어디까지 보여줄지 정해야함.
        # 각각 따로 만들어야함
        return Response(homework_serializer.data)

    def put(self, request):
        homework_pk = request.data.get('pk')
        print(homework_pk)
        print(request.user.userflag)
        if request.user.userflag:
            homework = TeacherHomework.objects.get(pk=homework_pk)
            homework_serializer = TeacherHomeworkCreateSerializer(instance = homework,data=request.data)
            if homework_serializer.is_valid(raise_exception=True):
                homework_serializer.save()

                d_files = homework.teacher_file.all()
                d_files.delete()
                files = request.FILES.getlist("files")
                for file in files:
                    fp = Files.objects.create(teacher_homework=homework,atch_file=file,atch_file_name=file)
                    fp.save()

        else:
            homework = StudentHomework.objects.get(pk=homework_pk)
            homework_serializer = StudentHomeworkCreateSerializer(instance = homework,data=request.data)
            if homework_serializer.is_valid(raise_exception=True):
                homework_serializer.save()

                d_files = homework.student_file.all()
                d_files.delete()

                files = request.FILES.getlist('files')
                for file in files:
                    fp = Files.objects.create(teacher_homework=homework,atch_file=file,atch_file_name=file)
                    fp.save()
        
        context = {
            "success" : True,
            "message" : "수정이 성공적으로 완성되었습니다"
        }
        return Response(context)

    def delete(self, request):
        homework_pk = request.data.get('pk')
        teacher_flag = request.data.get('teacher')
        print(homework_pk)
        print(teacher_flag)
        if teacher_flag == True:
            homework = TeacherHomework.objects.get(pk=homework_pk)
        
        elif teacher_flag == False:
            homework = StudentHomework.objects.get(pk=homework_pk)
        
        homework.delete()
        context = {
            "success" : True,
            "message" : "삭제되었습니다"
        }
        return Response(context)

class HomeworkCheckView(APIView): # 채점
    def post(self, request):
        if request.user.userflag == True:
            pass
        
class HomeworkSubmitView(APIView): # 제출
    def post(self, request):
        submit_pk = request.data.get('submit_pk') # 제출번호

        if request.data.get('teacher') == '1':
            submit = SubmitHomework.objects.get(id=submit_pk)
            submit_serializer = SubmitHomeworksubmitSerializer(submit,data=request.data)

            if submit_serializer.is_valid(raise_exception=True):
                file = request.FILES.get('files')
                submit_serializer.save(atch_file=file,atch_file_name=file)
                context = {
                    "success" : True,
                    "message" : "제출되었습니다"
                }
                return Response(context)
        else:
            submit = SubmitHomework.objects.get(id=submit_pk)
            submit_serializer = SubmitHomeworksubmitSerializer(submit,data=request.data)

            if submit_serializer.is_valid(raise_exception=True):
                file = request.FILES.get('files')
                submit_serializer.save(atch_file=file,atch_file_name=file)
                print(submit.student_homework)
                homework = StudentHomework.objects.get(id=submit.student_homework.id)
                homework.submit_flag = True
                homework.save()
                context = {
                    "success" : True,
                    "message" : "제출되었습니다"
                }
                return Response(context)


