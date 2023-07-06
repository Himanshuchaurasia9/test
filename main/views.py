from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect, HttpResponse





# Create your views here.
def home(request):
    return render(request,'base.html')




def login_page(request):
    if request.user.is_authenticated:
        if request.user.user_role == 1:
            return HttpResponse("Admin")
        elif request.user.user_role == 2:
            return HttpResponse('Staff')
        else:
            return HttpResponse('student')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,user_id=username,password=password)
        print(user)
        if user != None:
            login(request, user)
            user_role = user.user_role
            if user_role == 1:
                return HttpResponse('Admin')
            elif user_role == 2:
                return HttpResponse('Staff')
            elif user_role == 3:
                return HttpResponse('Student')
            else:
                # messages.add_message(request, messages.SUCCESS, f"Hi, Wellcome, {username}.!!!")
                return redirect('login')
        else:
            # messages.add_message(request, messages.WARNING, "Wrong Credentials.!!!.")
            return redirect('login')
    return render(request,'login.html')

