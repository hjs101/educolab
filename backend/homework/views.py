<<<<<<< HEAD
from re import sub
=======
>>>>>>> 1d03a62 (Backend file 삽입)
from django.shortcuts import render
from rest_framework.views import APIView 
from rest_framework.response import Response

<<<<<<< HEAD
from accounts.serializers import UserinfoSerializer

from .models import StudentHomework, TeacherHomework, Files, SubmitHomework
from accounts.models import  UserInfo, PointLog
from .serializers import StudentHomeworkDetailSerializer, StudentHomeworkMainSerializer, SubmitHomeworkSerializer, SubmitHomeworksubmitSerializer, TeacherHomeworkCreateSerializer, StudentHomeworkCreateSerializer, TeacherHomeworkDetailSerializer, TeacherHomeworkMainSerializer
=======
from .models import StudentHomework, TeacherHomework, Files, SubmitHomework
from accounts.models import SchoolInfo, UserInfo
<<<<<<< HEAD
from .serializers import StudentHomeworkDetailSerializer, StudentHomeworkMainSerializer, TeacherHomeworkCreateSerializer, StudentHomeworkCreateSerializer, TeacherHomeworkDetailSerializer, TeacherHomeworkMainSerializer
>>>>>>> 1d03a62 (Backend file 삽입)
=======
from .serializers import StudentHomeworkDetailSerializer, StudentHomeworkMainSerializer, SubmitHomeworksubmitSerializer, TeacherHomeworkCreateSerializer, StudentHomeworkCreateSerializer, TeacherHomeworkDetailSerializer, TeacherHomeworkMainSerializer
>>>>>>> ffe7e28 (백 프론트 파일 복사했어유)

from datetime import datetime
# Create your views here.
class HomeworkMainView(APIView):
    
    def get(self, request):
<<<<<<< HEAD
<<<<<<< HEAD
        if request.user.userflag:
=======
        today = datetime.now().date()
        if request.user.userflag == True:
>>>>>>> 7affbf9 (feat : 과제 메인 기능 구현)
=======
        today = datetime.now().date()
        if request.user.userflag == True:
>>>>>>> 1d03a62 (Backend file 삽입)
            teacher = UserInfo.objects.get(username=request.user.username)
            homeworks = teacher.T_homework.all()
            notdone_homework = []
            done_notcheck_homework = []
            all_done_homework = []
            for homework in homeworks:
<<<<<<< HEAD
<<<<<<< HEAD
=======
                print(homework.deadline, today)
>>>>>>> 1d03a62 (Backend file 삽입)
=======
>>>>>>> fc9ea5f (머지)
                if homework.deadline >= today:
                    notdone_homework.append(homework)
                elif homework.check_flag == False:
                    done_notcheck_homework.append(homework)
                else:
                    all_done_homework.append(homework)
        
            
            student_homeworks = teacher.homeroom_T.filter(submit_flag=True,agreement=False)

<<<<<<< HEAD
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
=======
>>>>>>> fc9ea5f (머지)
            notdone_homework_serializer = TeacherHomeworkMainSerializer(notdone_homework, many=True)
            not_done = sorted(notdone_homework_serializer.data, key=lambda x:x['deadline'])
            done_notcheck_homework_serializer = TeacherHomeworkMainSerializer(done_notcheck_homework, many=True)
            all_done_homework_serializer = TeacherHomeworkMainSerializer(all_done_homework, many=True)
            all_done = sorted(all_done_homework_serializer.data, key=lambda x:x['id'], reverse=True)
            student_homeworks_serizlizer = StudentHomeworkMainSerializer(student_homeworks, many=True)
            
            context = {
                "not_done" : not_done,
                "done_notcheck" : done_notcheck_homework_serializer.data,
                "all_done" : all_done,
<<<<<<< HEAD
                "students" : student_homeworks_serizlizer.data
            }
            return Response(context)
>>>>>>> e59250a (feat: 과제 메인페이지 기능 어느정도 구현 완료 나머지는 상의필요)
        
        elif request.user.userflag:
=======
            
            student_homeworks = teacher.homeroom_T.filter(submit_flag=True,agreement=False)

            notdone_homework_serializer = TeacherHomeworkMainSerializer(notdone_homework, many=True)
            done_notcheck_homework_serializer = TeacherHomeworkMainSerializer(done_notcheck_homework, many=True)
            all_done_homework_serializer = TeacherHomeworkMainSerializer(all_done_homework, many=True)
            student_homeworks_serizlizer = StudentHomeworkMainSerializer(student_homeworks, many=True)
            
            context = {
                "not_done" : notdone_homework_serializer.data,
                "done_notcheck" : done_notcheck_homework_serializer.data,
                "all_done" : all_done_homework_serializer.data,
=======
>>>>>>> fc9ea5f (머지)
                "students" : student_homeworks_serizlizer.data
            }
            return Response(context)
        
        elif request.user.userflag == False:
>>>>>>> 1d03a62 (Backend file 삽입)
            student = UserInfo.objects.get(username=request.user.username)
            homeworks = student.teacher_homework.all()

            notdone_homework = []
            done_homework = []

            for homework in homeworks:
                if homework.deadline >= today:
                    notdone_homework.append(homework)
                else:
                    done_homework.append(homework)
            
<<<<<<< HEAD
<<<<<<< HEAD
            my_submit_homework = student.S_homework.filter(submit_flag=True).order_by('-id')
=======
            my_submit_homework = student.S_homework.filter(submit_flag=True).order_by('-pk')
>>>>>>> fc9ea5f (머지)
            my_homework = student.S_homework.filter(submit_flag=False).order_by('deadline')

            notdone_homework_serializer = TeacherHomeworkMainSerializer(notdone_homework, many=True)
            not_done = sorted(notdone_homework_serializer.data, key=lambda x:x['deadline'])
            done_homework_serialzier = TeacherHomeworkMainSerializer(done_homework, many=True)
            done = sorted(done_homework_serialzier.data,key=lambda x:x['id'], reverse=True)

            my_submit_homework_serializer = StudentHomeworkMainSerializer(my_submit_homework, many=True)
            my_homework_serializer = StudentHomeworkMainSerializer(my_homework, many=True)
            context = {
                "notdone" : not_done,
                "done" : done,
                "my_submit_homework" : my_submit_homework_serializer.data,
<<<<<<< HEAD
                "my_homework" : my_homework_serializer.data
            }
            return Response(context)

            
=======
            my_homework = student.S_homework.all()

            notdone_homework_serializer = TeacherHomeworkMainSerializer(notdone_homework, many=True)
            done_homework_serialzier = TeacherHomeworkMainSerializer(done_homework, many=True)
            my_homework_serializer = StudentHomeworkMainSerializer(my_homework, many=True)
            context = {
                "notdone" : notdone_homework_serializer.data,
                "done" : done_homework_serialzier.data,
=======
>>>>>>> fc9ea5f (머지)
                "my_homework" : my_homework_serializer.data
            }
            return Response(context)
            
            


>>>>>>> 1d03a62 (Backend file 삽입)
class HomeworkCreateView(APIView):
    
    def post(self, request):
        if request.user.userflag == 0:
<<<<<<< HEAD
<<<<<<< HEAD
            print(0)
            print(request.data)
=======
>>>>>>> 9e9bfd9 (style : print 모두 제거)
            homework_serializer = StudentHomeworkCreateSerializer(data=request.data)
            
            if homework_serializer.is_valid(raise_exception=True):
<<<<<<< HEAD
                print('valid')
                teacher = UserInfo.objects.get(school=request.user.school,class_field=request.user.class_field,grade=request.user.grade,userflag=True)
=======
                teacher = UserInfo.objects.get(school=request.user.school,class_field=request.user.class_field,grade=request.user.grade,userflag=True,homeroom_teacher_flag=True)
>>>>>>> 3ed528e (fix : 학생 담임선생님에게 요청하도록 fix)
                homework = homework_serializer.save(student=request.user,teacher=teacher)
<<<<<<< HEAD
<<<<<<< HEAD
=======
            homework_serializer = StudentHomeworkCreateSerializer(data=request.data)
            
            if homework_serializer.is_valid(raise_exception=True):
                teacher = UserInfo.objects.get(class_field=request.user.class_field,grade=request.user.grade,userflag=True)
                homework = homework_serializer.save(student=request.user,teacher=teacher)

>>>>>>> 1d03a62 (Backend file 삽입)
=======
                print('homework')
>>>>>>> 1771885 (Fix : 과제 스타일 및 수정, 생성 시 오류 해결)
=======
>>>>>>> 9e9bfd9 (style : print 모두 제거)
                files = request.FILES.getlist("files")
                for file in files:
                    fp = Files.objects.create(student_homework=homework,atch_file=file,atch_file_name=file)
                    fp.save()
                
                submit = SubmitHomework.objects.create(student_homework=homework,student=request.user)
                submit.save()

        elif request.user.userflag == 1:
<<<<<<< HEAD
<<<<<<< HEAD
            print(1)
            print(request.data)
=======
>>>>>>> 9e9bfd9 (style : print 모두 제거)
            homework_serializer = TeacherHomeworkCreateSerializer(data=request.data)
            if homework_serializer.is_valid(raise_exception=True):
                school = request.user.school
                school_student= school.school_student.all()
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
                print(school_student)
                students = school_student.filter(grade=homework_serializer.validated_data['grade'],class_field=homework_serializer.validated_data['class_field'])
                print(students)
=======
                students = school_student.filter(grade=homework_serializer.validated_data['grade'],class_field=homework_serializer.validated_data['class_field'],userflag=False)
>>>>>>> 6f71aa8 (과제요청사항 수정)
=======
                students = school_student.filter(grade=homework_serializer.validated_data['grade'],class_field=homework_serializer.validated_data['class_field'],userflag=False)
>>>>>>> 373b6d1 (feat: 과제 생성 기능 수정, 상세정보 기능 수정, 제출 수정)
=======
                print(school_student)
                students = school_student.filter(grade=homework_serializer.validated_data['grade'],class_field=homework_serializer.validated_data['class_field'],userflag=False)
                print(students)
>>>>>>> d6318b5 (Feat : 과제 제출 기능 구현 및 상세 페이지 오류 수정)
=======
                students = school_student.filter(grade=homework_serializer.validated_data['grade'],class_field=homework_serializer.validated_data['class_field'],userflag=False)
>>>>>>> 9e9bfd9 (style : print 모두 제거)
                homework = homework_serializer.save(teacher=request.user,target=students)
                files = request.FILES.getlist("files")
                for file in files:
                    fp = Files.objects.create(teacher_homework=homework,atch_file=file,atch_file_name=file)
                    fp.save()
                for student in students:
                    submit = SubmitHomework.objects.create(student=student,teacher_homework=homework)
<<<<<<< HEAD
                    print(submit)
=======
            homework_serializer = TeacherHomeworkCreateSerializer(data=request.data)
            if homework_serializer.is_valid(raise_exception=True):
                school = request.user.school
                school_student= school.school_student.all()
                students = school_student.filter(grade=homework_serializer.validated_data['grade'],class_field=homework_serializer.validated_data['class_field'])
                homework = homework_serializer.save(teacher=request.user,target=students)
                
                files = request.FILES.getlist("files")
                for file in files:
                    fp = Files.objects.create(teacher_homework=homework,atch_file=file,atch_file_name=file)
                    fp.save()
                
                for student in students:
                    submit = SubmitHomework.objects.create(student=student,teacher_homework=homework)
>>>>>>> 1d03a62 (Backend file 삽입)
=======
>>>>>>> 9e9bfd9 (style : print 모두 제거)
                    submit.save()

        context = {
            "success" : True,
            "pk" : homework.pk
        }
        return Response(context)

class HomeworkDetailView(APIView):
    def get(self, request):
        homework_pk = request.GET.get('pk')
<<<<<<< HEAD
        teacher_flag = request.GET.get('teacher_flag')
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
        if teacher_flag == '1':
            print('teacher')
=======
        print(homework_pk, teacher_flag)
        if teacher_flag:
>>>>>>> 6f71aa8 (과제요청사항 수정)
            homework = TeacherHomework.objects.get(id=homework_pk)
            homework_serializer = TeacherHomeworkDetailSerializer(homework)
=======
        print(homework_pk, teacher_flag)
=======
>>>>>>> 9e9bfd9 (style : print 모두 제거)
        if teacher_flag == '1':
            if request.user.userflag == True:
                homework = TeacherHomework.objects.get(id=homework_pk)
                homework_serializer = TeacherHomeworkDetailSerializer(homework)
                student_submit = homework.student_submit.all()
                student_submit_serializer = SubmitHomeworkSerializer(student_submit, many=True)
                context = {
                    "homework" : homework_serializer.data,
                    "student_submit" : student_submit_serializer.data
                }
            
            else:
                homework = TeacherHomework.objects.get(id=homework_pk)
                student_submit = homework.student_submit.filter(student=request.user)
                homework_serializer = TeacherHomeworkDetailSerializer(homework)
                student_submit_serializer = SubmitHomeworkSerializer(student_submit, many=True)
>>>>>>> 373b6d1 (feat: 과제 생성 기능 수정, 상세정보 기능 수정, 제출 수정)

                context = {
                    "homework" : homework_serializer.data,
                    "student_submit" : student_submit_serializer.data
                }

            return Response(context)
                
        else:
            homework = StudentHomework.objects.get(id=homework_pk)
            homework_serializer = StudentHomeworkDetailSerializer(homework)
<<<<<<< HEAD
        
=======

            return Response(homework_serializer.data)

>>>>>>> 373b6d1 (feat: 과제 생성 기능 수정, 상세정보 기능 수정, 제출 수정)
        # serializer를 통해서 어디까지 보여줄지 정해야함.
        # 각각 따로 만들어야함
=======
        teacher_flag = request.GET.get('teacher')
        print(homework_pk, teacher_flag)
        if teacher_flag:
            homework = TeacherHomework.objects.get(id=homework_pk)
            homework_serializer = TeacherHomeworkDetailSerializer(homework)

        else:
<<<<<<< HEAD
            print(2)
=======
>>>>>>> fc9ea5f (머지)
            homework = StudentHomework.objects.get(id=homework_pk)
            homework_serializer = StudentHomeworkDetailSerializer(homework)
        

        # serializer를 통해서 어디까지 보여줄지 정해야함.
        # 각각 따로 만들어야함
        return Response(homework_serializer.data)
<<<<<<< HEAD
>>>>>>> 1d03a62 (Backend file 삽입)
    
=======

>>>>>>> ffe7e28 (백 프론트 파일 복사했어유)
    def put(self, request):
        homework_pk = request.data.get('pk')
        if request.user.userflag:
            homework = TeacherHomework.objects.get(pk=homework_pk)
            homework_serializer = TeacherHomeworkCreateSerializer(instance = homework,data=request.data)
            if homework_serializer.is_valid(raise_exception=True):
                students = request.user.school.school_student.filter(grade=homework_serializer.validated_data['grade'],class_field=homework_serializer.validated_data['class_field'],userflag=False)
                homework_serializer.save(target = students)
                
                student_submit = homework.student_submit.all()
                student_submit.delete()

                for student in students:
                    submit = SubmitHomework.objects.create(student=student,teacher_homework=homework)
                    submit.save()


                d_files = homework.teacher_file.all()
                d_files.delete()
<<<<<<< HEAD
<<<<<<< HEAD
                files = request.FILES.getlist("files")
=======

                files = request.FILES.getlist('files')
>>>>>>> 1d03a62 (Backend file 삽입)
=======
                files = request.FILES.getlist("files")
>>>>>>> ffe7e28 (백 프론트 파일 복사했어유)
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
            "message" : homework_serializer.data
        }
        return Response(context)

    def delete(self, request):
        homework_pk = request.data.get('pk')
<<<<<<< HEAD
<<<<<<< HEAD
        teacher_flag = request.data.get('teacher')
        print(homework_pk)
=======
        teacher_flag = request.data.get('teacher_flag')
<<<<<<< HEAD
>>>>>>> 373b6d1 (feat: 과제 생성 기능 수정, 상세정보 기능 수정, 제출 수정)
=======
        teacher_flag = request.data.get('teacher')
>>>>>>> 1d03a62 (Backend file 삽입)
        print(teacher_flag)
=======
>>>>>>> 9e9bfd9 (style : print 모두 제거)
        if teacher_flag == True:
            homework = TeacherHomework.objects.get(pk=homework_pk)
        
        elif teacher_flag == False:
            homework = StudentHomework.objects.get(pk=homework_pk)
        
        homework.delete()
        context = {
            "success" : True,
            "message" : "삭제되었습니다"
        }
<<<<<<< HEAD
<<<<<<< HEAD
        return Response(context) 

class HomeworkCheckView(APIView): # 채점
    def post(self, request):
        if request.user.userflag == True:
            submit = SubmitHomework.objects.get(id=request.data.get('pk'))
            if submit.check_flag == True:
                return Response({"success" : False, "message" : "이미 채점된 제출입니다"})
            username = request.data.get('username')
            point = request.data.get('point')
            student = UserInfo.objects.get(username=username)
            if point > 0:
                student.plus_point += point
                student.acc_point += point
            else:
                student.minus_point += point
            submit.check_flag=True
            submit.save()
            point = PointLog.objects.create(teacher=request.user,student=student,school=request.user.school,content="과제 점수",point=point,acc_minus=student.minus_point,acc_point=student.plus_point)
            student.save()
<<<<<<< HEAD
            # students = UserinfoSerializer(student)
            return Response({"username" : username, "success" : True,"message" : "적용되었습니다"})
=======
            return Response({"success": True, "message" : "채점이 완료되었습니다"})
>>>>>>> cda8e1a (feat : 채점 여부 플래그)

class HomeworkCheckDoneView(APIView):
    def post(self, request):
        if request.user.userflag == True:
            if request.data.get('teacher_flag') == '1':
                homework = TeacherHomework.objects.get(id=request.data.get('pk'))
                homework.check_flag = True
                homework.save()
            else:
                homework = StudentHomework.objects.get(id=request.data.get('pk'))
                homework.agreement = True
                homework.save()
            
            return Response({"success" : True,"message" : "완료되었습니다"})

        
class HomeworkSubmitView(APIView): # 제출
    def post(self, request):
        submit_pk = request.data.get('submit_pk') # 제출번호

        if request.data.get('teacher_flag') == '1':
=======
        return Response(context)

class HomeworkCheckView(APIView): # 채점
    def post(self, request):
        if request.user.userflag == True:
            pass
        
class HomeworkSubmitView(APIView): # 제출
    def post(self, request):
        submit_pk = request.data.get('submit_pk') # 제출번호

        if request.data.get('teacher') == '1':
>>>>>>> ffe7e28 (백 프론트 파일 복사했어유)
            submit = SubmitHomework.objects.get(id=submit_pk)
            submit_serializer = SubmitHomeworksubmitSerializer(submit,data=request.data)

            if submit_serializer.is_valid(raise_exception=True):
                file = request.FILES.get('files')
<<<<<<< HEAD
                submit_serializer.save(atch_file=file,atch_file_name=file, submit_flag=True)
=======
                submit_serializer.save(atch_file=file,atch_file_name=file)
>>>>>>> ffe7e28 (백 프론트 파일 복사했어유)
                context = {
                    "success" : True,
                    "message" : "제출되었습니다"
                }
                return Response(context)
        else:
            submit = SubmitHomework.objects.get(id=submit_pk)
            submit_serializer = SubmitHomeworksubmitSerializer(submit,data=request.data)
<<<<<<< HEAD
            if submit_serializer.is_valid(raise_exception=True):
                file = request.FILES.get('files')
<<<<<<< HEAD
                submit_serializer.save(atch_file=file,atch_file_name=file, submit_flag=True)
=======
                submit_serializer.save(atch_file=file,atch_file_name=file,submit_flag=True)
>>>>>>> 4910d64 (feat : 상점 기능 구현, 마이페이지 칭호 변경 구현)
=======

            if submit_serializer.is_valid(raise_exception=True):
                file = request.FILES.get('files')
                submit_serializer.save(atch_file=file,atch_file_name=file)
                print(submit.student_homework)
>>>>>>> ffe7e28 (백 프론트 파일 복사했어유)
                homework = StudentHomework.objects.get(id=submit.student_homework.id)
                homework.submit_flag = True
                homework.save()
                context = {
                    "success" : True,
                    "message" : "제출되었습니다"
                }
                return Response(context)


<<<<<<< HEAD
=======
        return Response(context)
>>>>>>> 1d03a62 (Backend file 삽입)
=======
>>>>>>> ffe7e28 (백 프론트 파일 복사했어유)
