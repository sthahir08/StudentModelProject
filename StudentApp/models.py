from django.db import models
from django.db.models.signals import post_save

from django.urls import reverse


Branch_Choices =(("1","CSE"),("2","ECE"), ("3","Mech"),("4","IT"))
Sem_Choices =(("1","I"),('2',"II"),("3","III"),("4","IV"),("5","V"),("6","VI"),("7","VII"),("8","VIII"))
Gender_Choices =(("1","male"),('2',"female"),("3","others"),)

class StudentMainModel(models.Model):
    Name  = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    Gender=models.CharField(max_length=10,choices=Gender_Choices)
    Image=models.ImageField()
    Rollno = models.CharField(max_length=100)

    def _str_(self):
        return self.Name


class StudentMarksModel(models.Model):
    student = models.ForeignKey(StudentMainModel,null=True,on_delete=models.CASCADE)
    Marks = models.IntegerField()
    Semester = models.CharField(max_length=20, choices=Sem_Choices)


class StudentMarksMainModel(models.Model):
    student = models.OneToOneField(StudentMainModel, null=True,on_delete=models.CASCADE)
    Marks = models.ManyToManyField(StudentMarksModel)
    Branch = models.CharField(max_length=50, choices=Branch_Choices, null=True)
    FinalMarks = models.IntegerField(blank=True,null=True)

def StudentFinalMarks(sender,created,instance,*args,**kwargs):

    if created:
        print("created")
        student_main=StudentMainModel.objects.get(id=instance.student.id)
        print(student_main)


post_save.connect(StudentFinalMarks,sender=StudentMarksModel)