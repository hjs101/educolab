# Generated by Django 3.2.12 on 2022-08-07 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_alter_userinfo_profil'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='profil',
            field=models.ImageField(blank=True, default='test01.jpg', upload_to='accounts/profils'),
        ),
    ]