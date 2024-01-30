from django.shortcuts import redirect, render
from django.contrib.auth.models import Group, User
from django.contrib.auth import authenticate, login
from .forms import AuthForm, RegForm
from .models import CustomUser
# Create your views here.
def main(request):
    authform = AuthForm()
    return render(request, 'main.html', {'form':authform})

def reg(request):
    regform = RegForm(request.POST)
    if request.method == 'POST':
        request.POST.get('username')
        if regform.is_valid():
            if regform.cleaned_data.get('is_teacher'):
                teacher = CustomUser.objects.create_user(
                    first_name=regform.cleaned_data.get('first_name'),
                    last_name=regform.cleaned_data.get('last_name'),
                    surname=regform.cleaned_data.get('surname'),
                    username=regform.cleaned_data.get('username'),
                    password=regform.cleaned_data.get('password'),
                    email=regform.cleaned_data.get('email'),
                )
                teacher_group = Group.objects.get(name='Учитель')
                teacher.groups.add(teacher_group)
                authenticate(username=regform.cleaned_data.get('username'), password=regform.cleaned_data.get('password'),)
            
                return redirect('/')
            else:
                student = CustomUser.objects.create_user(
                    first_name=regform.cleaned_data.get('first_name'),
                    last_name=regform.cleaned_data.get('last_name'),
                    surname=regform.cleaned_data.get('surname'),
                    username=regform.cleaned_data.get('username'),
                    password=regform.cleaned_data.get('password'),
                    email=regform.cleaned_data.get('email'),
                )
                student_group = Group.objects.get(name='Ученик')
                student.groups.add(student_group)
                authenticate(username=regform.cleaned_data.get('username'), password=regform.cleaned_data.get('password'),)
                
                return redirect('/')
        else:
            for error in regform.non_field_errors():
                print(error)
    return render(request, 'reg.html', {'form':regform})