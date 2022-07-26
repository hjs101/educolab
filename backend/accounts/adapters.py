from allauth.account.adapter import DefaultAccountAdapter

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
        if school:
            user.school = school
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
        homeroom_teacher_flag = data.get("homeroom_teacher_flag")
        if homeroom_teacher_flag:
            user.homeroom_teacher_flag = homeroom_teacher_flag
        plus_point = data.get("plus_point")
        if plus_point:
            user.plus_point = plus_point
        minus_point = data.get("minus_point")
        if minus_point:
            user.minus_point = minus_point
        
        user.save()
        return user