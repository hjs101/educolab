# Generated by Django 3.2.12 on 2022-07-27 02:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_userinfo_grade'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='school',
            field=models.ForeignKey(db_column='school', on_delete=django.db.models.deletion.CASCADE, related_name='school', to='accounts.schoolinfo'),
        ),
    ]