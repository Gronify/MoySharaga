from django.shortcuts import render, redirect
from django.contrib import messages # django messages for certain actions
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required # decorator for auth

from panel.models import University, Student, Group, Timetable, UserStudent, UserTeacher, ConnectionTSG, Teacher

#view for registration
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created successfuly')
            return redirect('users:login')
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})

# view for profile
@login_required
def profile(request):
    if UserStudent.objects.filter(user = request.user):
        studentid = UserStudent.objects.filter(user = request.user).values_list('student_id').first()
        student = Student.objects.get(id = studentid[0])
        groupid = Student.objects.filter(id = studentid[0]).values_list('group_id').first()
        timetableForMonday = Timetable.objects.filter(group_id = groupid, day = "M")
        timetableForTuesday = Timetable.objects.filter(group_id = groupid, day = "T")
        timetableForWendsday = Timetable.objects.filter(group_id = groupid, day = "W")
        timetableForThursday = Timetable.objects.filter(group_id = groupid, day = "TH")
        timetableForFriday = Timetable.objects.filter(group_id = groupid, day = "F")
        timetableForSaturday= Timetable.objects.filter(group_id = groupid, day = "S")
        return render(request, 'profile.html', {'student': student,'timetableForMonday': timetableForMonday, 'timetableForTuesday': timetableForTuesday, 'timetableForWendsday': timetableForWendsday, 'timetableForThursday': timetableForThursday, 'timetableForFriday': timetableForFriday, 'timetableForSaturday': timetableForSaturday},   )
    elif UserTeacher.objects.filter(user = request.user):
        teacherid = UserTeacher.objects.filter(user = request.user).values_list('teacher_id').first()
        teacher = Teacher.objects.get(id = teacherid[0])
        connectionTSG = ConnectionTSG.objects.filter(teacher_id = teacherid[0])
        student = ''

        return render(request, 'profile.html', {'teacher': teacher, 'connectionTSG':connectionTSG, 'student': student} )
    else:
        return render(request, 'profile.html',)
