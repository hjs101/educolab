from allauth.account.adapter import DefaultAccountAdapter
from .serializers import SchoolInfoSerializer
from .models import SchoolInfo
class CustomAccountAdapter(DefaultAccountAdapter):
    def save_user(self, request, user, form, commit=True):
        data = form.cleaned_data
        user = super().save_user(request, user, form, commit)
        name = data.get("name")
        if name:
            user.name = name
        birthday = data.get("birthday")
        if birthday:
            user.birthday = birthday
        school = data.get("school")
        school = SchoolInfo.objects.get(code=school)
        if school:
            user.school = school
        userflag = data.get("userflag")
        if userflag:
            user.userflag = userflag
        phone_number = data.get("phone_number")
        if phone_number:
            user.phone_number = phone_number
        grade = data.get("grade")
        if grade:
            user.grade = grade
        class_field = data.get("class_field")
        if class_field:
            user.class_field = class_field
        subject = data.get("subject")
        if subject:
            user.subject = subject
        
        user.save()
        return user