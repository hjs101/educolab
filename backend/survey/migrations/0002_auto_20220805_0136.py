# Generated by Django 3.2.12 on 2022-08-04 16:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('survey', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='surveyquestionsanswer',
            name='question',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='question_answers', to='survey.surveyquestions'),
        ),
        migrations.AlterField(
            model_name='surveylist',
            name='class_field',
            field=models.IntegerField(),
        ),
        migrations.RemoveField(
            model_name='surveylist',
            name='done_target',
        ),
        migrations.AddField(
            model_name='surveylist',
            name='done_target',
            field=models.ManyToManyField(related_name='done_target', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='surveylist',
            name='grade',
            field=models.IntegerField(),
        ),
    ]