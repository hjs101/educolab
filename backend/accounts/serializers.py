from rest_framework import serializers
from . import models


class TeacherSerializer(serializers.Serializer):
    class Meta():
        Model = models.TeacherInfo
        fields = ('teacher_id','name','birthday','school','subject','homeroom_teacher_flag',
        'homeroom_teacher_grade','homeroom_teacher_class','phone_number','email')
    
class StudentSerializer(serializers.Serializer):
    class Meta():
        Model = models.StudentInfo
        fields = ('student_id','name','birthday','school','grade','class_field','student_number',
        'phone_number','email','plus_point','minus_point')
