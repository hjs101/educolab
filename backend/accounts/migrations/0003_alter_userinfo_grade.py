# Generated by Django 3.2.12 on 2022-07-27 00:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_schoolinfo_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='grade',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
