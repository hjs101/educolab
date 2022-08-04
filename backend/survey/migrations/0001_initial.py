<<<<<<< HEAD
# Generated by Django 3.2.12 on 2022-08-03 07:25
=======
# Generated by Django 3.2.12 on 2022-08-02 14:53
>>>>>>> 1d03a62 (Backend file 삽입)

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='SurveyList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=45)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
<<<<<<< HEAD
                ('grade', models.IntegerField()),
                ('class_field', models.IntegerField()),
                ('done_target', models.ManyToManyField(related_name='done_target', to=settings.AUTH_USER_MODEL)),
=======
                ('grade', models.CharField(max_length=45)),
                ('class_field', models.CharField(max_length=45)),
                ('done_target', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='target_done', to=settings.AUTH_USER_MODEL)),
>>>>>>> 1d03a62 (Backend file 삽입)
                ('target', models.ManyToManyField(related_name='target', to=settings.AUTH_USER_MODEL)),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='survey_teacher', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SurveyQuestions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_number', models.IntegerField()),
                ('survey_question', models.CharField(max_length=500)),
                ('multiple_bogi', models.CharField(blank=True, max_length=500, null=True)),
                ('num1', models.IntegerField(default=0)),
                ('num2', models.IntegerField(default=0)),
                ('num3', models.IntegerField(default=0)),
                ('num4', models.IntegerField(default=0)),
                ('num5', models.IntegerField(default=0)),
                ('survey', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='question_survey', to='survey.surveylist')),
            ],
        ),
        migrations.CreateModel(
            name='SurveyQuestionsAnswer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
<<<<<<< HEAD
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='question_answers', to='survey.surveyquestions')),
=======
                ('survey_question_pk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='survey.surveyquestions')),
>>>>>>> 1d03a62 (Backend file 삽입)
            ],
        ),
        migrations.CreateModel(
            name='SueveyTemplate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.CharField(max_length=450)),
                ('teacher_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
