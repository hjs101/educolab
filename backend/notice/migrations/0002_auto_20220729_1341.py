# Generated by Django 3.2.12 on 2022-07-29 04:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('notice', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='files',
            name='notice',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notice_file', to='notice.notice'),
        ),
        migrations.AlterField(
            model_name='notice',
            name='views',
            field=models.IntegerField(default=0),
        ),
    ]
