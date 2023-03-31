from django.contrib import admin
from StudentApp.models import StudentMainModel,StudentMarksModel,StudentMarksMainModel

# Register your models here.

class StudentMainModel_Admin(admin.ModelAdmin):
    list1 = ['Name','date_of_birth','Age','Rollno']


admin.site.register(StudentMainModel,StudentMainModel_Admin)

class StudentMarksModel_Admin(admin.ModelAdmin):
    list2 = ['student','Marks','Semester']

admin.site.register(StudentMarksModel,StudentMarksModel_Admin)

class StudentMarksMain_ModelAdmin(admin.ModelAdmin):
    list3 = ['student','Branch','FinalMarks']

admin.site.register(StudentMarksMainModel,StudentMarksMain_ModelAdmin)