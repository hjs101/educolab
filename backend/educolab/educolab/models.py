# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Homework(models.Model):
    homework_pk = models.IntegerField(primary_key=True)
    teacher = models.ForeignKey('TeacherInfo', models.DO_NOTHING)
    title = models.CharField(max_length=45)
    subject = models.CharField(max_length=45)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    atch_data_slp = models.CharField(db_column='ATCH_DATA_SLP', max_length=500, blank=True, null=True)  # Field name made lowercase.
    atch_orgn_file_name = models.CharField(db_column='ATCH_ORGN_FILE_NAME', max_length=300, blank=True, null=True)  # Field name made lowercase.
    atch_file_size = models.IntegerField(db_column='ATCH_FILE_SIZE', blank=True, null=True)  # Field name made lowercase.
    deadline = models.DateTimeField()
    grade = models.IntegerField()
    class_field = models.IntegerField(db_column='class')  # Field renamed because it was a Python reserved word.

    class Meta:
        managed = False
        db_table = 'homework'
        unique_together = (('homework_pk', 'teacher'),)


class Notice(models.Model):
    notice_pk = models.IntegerField(primary_key=True)
    teacher = models.ForeignKey('TeacherInfo', models.DO_NOTHING)
    classification = models.CharField(max_length=45)
    title = models.CharField(max_length=45)
    created_at = models.DateTimeField()
    content = models.CharField(max_length=10000, blank=True, null=True)
    atch_data_slp = models.CharField(db_column='ATCH_DATA_SLP', max_length=500, blank=True, null=True)  # Field name made lowercase.
    atch_file_name = models.CharField(db_column='ATCH_FILE_NAME', max_length=300, blank=True, null=True)  # Field name made lowercase.
    atch_file_size = models.IntegerField(db_column='ATCH_FILE_SIZE', blank=True, null=True)  # Field name made lowercase.
    updated_flag = models.IntegerField()
    views = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'notice'
        unique_together = (('notice_pk', 'teacher'),)


class QuizList(models.Model):
    quiz_pk = models.IntegerField(primary_key=True)
    teacher = models.ForeignKey('TeacherInfo', models.DO_NOTHING)
    title = models.CharField(max_length=45)
    created_at = models.DateTimeField()
    grade = models.IntegerField()
    updated_flag = models.IntegerField()
    class_field = models.IntegerField(db_column='class')  # Field renamed because it was a Python reserved word.

    class Meta:
        managed = False
        db_table = 'quiz_list'
        unique_together = (('quiz_pk', 'teacher'),)


class QuizQuestion(models.Model):
    quiz_question_pk = models.IntegerField(primary_key=True)
    quiz_pk = models.ForeignKey(QuizList, models.DO_NOTHING, db_column='quiz_pk')
    question_number = models.IntegerField()
    question = models.CharField(max_length=500)
    multiple = models.CharField(max_length=500, blank=True, null=True)
    answer = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'quiz_question'
        unique_together = (('quiz_question_pk', 'quiz_pk'),)


class StudentHomework(models.Model):
    student_homework_pk = models.IntegerField(primary_key=True)
    student = models.ForeignKey('StudentInfo', models.DO_NOTHING)
    title = models.CharField(max_length=45)
    subject = models.CharField(max_length=45)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    atch_data_slp = models.CharField(db_column='ATCH_DATA_SLP', max_length=500, blank=True, null=True)  # Field name made lowercase.
    atch_orgn_file_name = models.CharField(db_column='ATCH_ORGN_FILE_NAME', max_length=300, blank=True, null=True)  # Field name made lowercase.
    atch_file_size = models.IntegerField(db_column='ATCH_FILE_SIZE', blank=True, null=True)  # Field name made lowercase.
    deadline = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'student_homework'
        unique_together = (('student_homework_pk', 'student'),)


class StudentInfo(models.Model):
    student_id = models.CharField(primary_key=True, max_length=45)
    name = models.CharField(max_length=30)
    birthday = models.IntegerField()
    school = models.CharField(max_length=45)
    grade = models.IntegerField()
    class_field = models.IntegerField(db_column='class')  # Field renamed because it was a Python reserved word.
    student_number = models.IntegerField()
    password = models.CharField(max_length=45)
    phone_number = models.IntegerField()
    email = models.CharField(max_length=45)
    plus_point = models.IntegerField()
    minus_point = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'student_info'


class SubmitHomework(models.Model):
    submit_homework_pk = models.IntegerField(primary_key=True)
    student = models.ForeignKey(StudentInfo, models.DO_NOTHING)
    homework_pk = models.ForeignKey(Homework, models.DO_NOTHING, db_column='homework_pk')
    student_homework_pk = models.ForeignKey(StudentHomework, models.DO_NOTHING, db_column='student_homework_pk')
    title = models.CharField(max_length=45)
    comment = models.CharField(max_length=10000, blank=True, null=True)
    subject = models.CharField(max_length=45)
    submit_at = models.DateTimeField()
    submit_flag = models.IntegerField()
    updated_at = models.DateTimeField()
    atch_data_slp = models.CharField(db_column='ATCH_DATA_SLP', max_length=500, blank=True, null=True)  # Field name made lowercase.
    atch_file_name = models.CharField(db_column='ATCH_FILE_NAME', max_length=300, blank=True, null=True)  # Field name made lowercase.
    atch_file_size = models.IntegerField(db_column='ATCH_FILE_SIZE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'submit_homework'
        unique_together = (('submit_homework_pk', 'student', 'homework_pk', 'student_homework_pk'),)


class SurveyList(models.Model):
    survey_pk = models.IntegerField(primary_key=True)
    teacher = models.ForeignKey('TeacherInfo', models.DO_NOTHING)
    title = models.CharField(max_length=45)
    created_at = models.DateTimeField()
    grade = models.IntegerField()
    updated_flag = models.IntegerField()
    class_field = models.IntegerField(db_column='class')  # Field renamed because it was a Python reserved word.

    class Meta:
        managed = False
        db_table = 'survey_list'
        unique_together = (('survey_pk', 'teacher'),)


class SurveyQuestions(models.Model):
    survey_pk = models.IntegerField(primary_key=True)
    survey_question_pk = models.ForeignKey(SurveyList, models.DO_NOTHING, db_column='survey_question_pk')
    question_number = models.IntegerField()
    survey_question = models.CharField(max_length=500)
    answer = models.CharField(max_length=100, blank=True, null=True)
    multiple_bogi = models.CharField(max_length=500, blank=True, null=True)
    num1 = models.IntegerField(blank=True, null=True)
    num2 = models.IntegerField(blank=True, null=True)
    num3 = models.IntegerField(blank=True, null=True)
    num4 = models.IntegerField(blank=True, null=True)
    num5 = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'survey_questions'
        unique_together = (('survey_pk', 'survey_question_pk'),)


class TeacherInfo(models.Model):
    teacher_id = models.CharField(primary_key=True, max_length=45)
    name = models.CharField(max_length=30)
    birthday = models.IntegerField()
    school = models.CharField(max_length=45)
    subject = models.CharField(max_length=45)
    homeroom_teacher_flag = models.IntegerField()
    homeroom_teacher_grade = models.IntegerField(blank=True, null=True)
    homeroom_teacher_class = models.IntegerField(blank=True, null=True)
    password = models.CharField(max_length=45)
    phone_number = models.IntegerField()
    email = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'teacher_info'