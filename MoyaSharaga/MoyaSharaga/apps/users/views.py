from django.shortcuts import render, redirect
from django.contrib import messages # django messages for certain actions
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required # decorator for auth

from panel.models import University, Student, Group, Timetable, UserStudent

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
        return render(request, 'profile.html', {'student': student})
    else:
        return render(request, 'profile.html',)
