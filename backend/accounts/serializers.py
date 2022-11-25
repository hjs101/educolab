from rest_framework import serializers
from . import models


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.TeacherInfo
        fields = ('username','name','birthday','school','subject','homeroom_teacher_flag',
        'homeroom_teacher_grade','homeroom_teacher_class','phone_number','email')

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.StudentInfo
        fields = ('username','name','birthday','school','grade','class_field','student_number',
        'phone_number','email','plus_point','minus_point')
