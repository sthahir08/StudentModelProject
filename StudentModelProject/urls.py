"""StudentModelProject URL Configuration

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
from django.urls import path,include
from StudentApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('studentmainlist/',views.Student_Marks_Main_List_View.as_view()),
    path('studentmainlist/<int:pk>',views.StudentMarksMainDetailView.as_view()),
    path("studentview/",views.Student_Main_List_View.as_view()),
    path('studentview/<int:pk>/',views.studentDetailView.as_view()),
    path('studentmarks/',views.StudentMarksListView.as_view()),
    path('studentMarks/<int:pk>/',views.StudentMarksDetailView.as_view()),
    path('createstudent/<int:Rollno>/', views.studentDetailView.as_view(),name = 'create'),
    path('studentdetail/<int:pk>/',views.Student_detail_view.as_view(),name='detail'),
]
