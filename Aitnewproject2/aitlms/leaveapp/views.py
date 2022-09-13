from django.shortcuts import render,redirect
from.models import *
from django.contrib.auth import login,logout,authenticate

def index(request):
    if not request.user.is_staff:
        return redirect('login')
    return render(request, 'index.html')

def registration(request):

    if request.method == "POST":
        fn = request.POST['firstname']
        ln = request.POST['lastname']
        em = request.POST['email']
        p = request.POST['Pwd']
        cn = request.POST['contact']
        ad = request.POST['Address']
        ut= request.POST['user_type']
        try:
            registration=Registration(firstname=fn,lastname=ln,email=em, password=p,contact=cn,address=ad,user_type=ut)
            registration.save()
            error="no"
        except:
            error="yes"
    return render(request,'Registration.html',locals())

def Login(request):

    if request.method == 'POST':
        em = request.POST['uname']
        pwd = request.POST['password']
        tpe= request.POST['user_type']
        printit=Registration.objects.filter(firstname=em,password=pwd,user_type=tpe).exists()
        if printit:
            error = "no"
        else:
            error = "yes"
    return render(request,'login.html',locals())

# def Login(request):
#     error = ""
#     if request.method == 'POST':
#         u = request.POST['uname']
#         p = request.POST['password']
#         user = authenticate(username=u, password=p)
#         UserDetail.objects.create()
#         UserDetail.objects.create()
#         try:
#             if user.is_staff:
#                 login(request, user)
#                 error = "no"
#             else:
#                 error = "yes"
#         except:
#             error = "yes"
#     d = {'error': error}
#     return render(request,'login.html', d)





def emp_dashbord(request):
    EmployeeName = Registration.objects.fetchAll(user_type="Employee",firstname="swati").exists()
    print(EmployeeName)
    return render(request,'emp_dashbord.html',{ EmployeeName:str(EmployeeName)})

def empbase(request):
    return render (request,'empbase.html')

def Logout(request):
    logout(request)
    return redirect('index')

def Eprofile(request):
    # if not request.User.is_authenticated:
    # return redirect('login')
    error = ""
       #  User = request.User
    # employee = UserDetail.objects.get(User=User)
    if request.method == request.POST:
        fn = request.post['Username']
        em = request.post['Email-Id']
        pwd = request.post['Password']
        pn = request.post['PhoneNumber']
        ad = request.post['Address']
        dp = request.post['Department']
        de = request.post['Designation']

        employee.User.Username = fn
        employee.User.Department = dp
        employee.User.PhoneNumber = pn
        employee.User.Designation = de
        employee.User.Address = ad
        try:
            employee.save
            employee.user.save
            User.objects.create_User(user_name=fn,email=em,password=pwd)
            UserDetail.objects.create(User=User,PhoneNumber =pn)
            UserDetail.objects.create(User=User,Address=ad)
            error="no"
        except:
            error="yes"
    return render(request,'Eprofile.html',locals())

def Leavetype(request):
    return render (request,'Leavetype.html',locals())

def Leaveapplication(request):
    return render (request,'Leaveapplication.html',locals())

def Changepassword(request):
      return render (request,'Changepassword.html',locals())

def Adminbase(request):
    return render (request,'Adminbase.html')

def Admindashbord(request):
    # if not request.User.is_authenticated:
    #     return redirect('login')
    return render(request,'Admindashbord.html')

def Allemployee(request):
    # EmployeeList=Registration.objects.filter(user_type="Employee").exists()
    return render (request,'Allemployee.html')

def Department(request):
    return render (request,'Department.html')

def Adminleave(request):
    return render (request,'Adminleave.html')

def Adminchangep(request):
    return render (request,'Adminchangep.html')


def Adminleavemanage(request):
    return render (request,'Adminleavemanage.html')


def Eprofile(request):

    if request.method == 'POST':
        em = request.POST['uname']
        pwd = request.POST['password']
        tpe= request.POST['user_type']
        pn = request.post['PhoneNumber']
        dp = request.post['Department']
        de = request.post['Designation']
        printt=Registration.objects.filter(firstname=request.printt.id)

        context = {
           "printt":printt
        }
    return render(request, 'Eprofile.html', locals())




