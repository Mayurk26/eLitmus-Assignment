from django.shortcuts import render , redirect
from .models import User

# Create your views here.
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request,'quiz/index.html')

def js(request):
    return render(request,'quiz/quizjs.html')

def web(request):
    return render(request,'quiz/web.html')

def login(request):
    if request.method == "POST":
        loginemail = request.POST.get('loginemail','')
        loginpassword = request.POST.get('loginpassword', '')

        newemail = request.POST.get('email','')
        name = request.POST.get('name','')
        password = request.POST.get('password','')


        #print('pwd:', password,  'name:', name, 'email:', newemail, 'loginemail:', loginemail,'loginpwd:',loginpassword)
        if loginemail != '' or loginpassword != '':
            print('loginemail:', loginemail, 'pwd:', loginpassword)
            try:
                user = User.objects.filter(useremail=loginemail,password=loginpassword)
                if (len(user)>0):
                    return redirect('Quizindex')
                else:
                    print('Your email or passwords dont match')
            except Exception as e:
                pass
        elif newemail !='' and password != '' and name != '':
            user1 = User.objects.filter(useremail=newemail)
            if (len(user1) == 0):
                user = User(useremail=newemail, name=name, password=password)
                user.save()
                print("Account created successfully")
            else:
                print('Account already exists')
            print('pwd:', password, 'name:', name, 'email:', newemail)


        else:
            print("Fill up all the fields")
            print('pwd:', password, 'name:', name, 'email:', newemail)

        #    print('pwd:',password,'name:',name,'email:',newemail)


    return render(request,'quiz/login.html')