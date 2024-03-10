"""
URL configuration for OnlinePlatform project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from . import Home
from . import UsrAuth
from . import SendNotify

urlpatterns = [
    path("admin/", admin.site.urls),
    path("home/", Home.homePage,name="home/"),
    path("sin/", Home.SignIn,name="sin/"),
    path("sup/", Home.SignUp,name="sup/"),
    path("tProfile/", Home.showTeacherProfile,name="tProfile/"),
    path('api/data/', Home.get_data, name='api/data/'),
    path('wow/', Home.your_view, name='wow/'),
    path('wow2/', Home.retrive, name='wow2/'),
    path('notf/', Home.mailPage, name='notf/'),
    path('pays/', Home.showPaymentPage, name='pays/'),
    path("authStu/", UsrAuth.studentAuth,name="authStu/"),
    path("authTea/", UsrAuth.teacherAuth,name="authTea/"),
    path("ims/", UsrAuth.idMatchStudent,name="ims/"),
    path("imt/", UsrAuth.idMatchTeacher,name="imt/"),
    path("filter/", UsrAuth.filterAll,name="filter/"),
    path("mail/", SendNotify.sendMail,name="mail/"),
]

