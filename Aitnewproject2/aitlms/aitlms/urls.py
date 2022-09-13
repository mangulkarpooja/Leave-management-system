"""aitlms URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from leaveapp.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index,name='index'),
    path('Registration',registration,name='Registration'),
    path('login',Login,name='login'),
    path('emp_dashbord',emp_dashbord,name='emp_dashbord'),
    path('empbase',empbase,name='empbase'),
    path('Eprofile',Eprofile,name='Eprofile'),
    path('logout',Logout,name='logout'),
    path('Leavetype', Leavetype, name='Leavetype'),
    path('Leaveappliction', Leaveapplication, name='Leaveapplication'),
    path('Changepassword',Changepassword,name='Changepassword'),
    path('Adminbase',Adminbase,name='Adminbase'),
    path('Admindashbord', Admindashbord, name='Admindashbord'),
    path('Allemployee', Allemployee , name='Allemployee'),
    path('Department', Department, name='Department'),
    path('Adminleave', Adminleave, name='Adminleave'),
    path('Adminchangep', Adminchangep, name='Adminchangep'),
    path('Adminleavemanage', Adminleavemanage, name='Adminleavemanage'),
    # path('api/change-password/', ChangePasswordView.as_view(), name='change-password'),

]

