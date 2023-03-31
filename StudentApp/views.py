from django.shortcuts import render
from rest_framework import status,generics
from StudentApp.Serializers import Student_serializer,Student_Marks_Serializer,Student_Main_Marks_Serializer
from rest_framework.response import Response
from rest_framework.views import APIView
from StudentApp.models import StudentMainModel,StudentMarksModel,StudentMarksMainModel
# Create your views here.

class Student_detail_view(APIView):
    def get_data(self,request,pk):
        student =StudentMainModel.objects.get(id=pk)
        student_Marks =StudentMarksMainModel.objects.get(student=student)
        serializer =Student_Main_Marks_Serializer(student_Marks)
        return Response(serializer.data)

class Student_Main_List_View(APIView):
    def get_data(self,request):
        student  = StudentMainModel.objects.all()
        serializer =Student_serializer(student,many = True)
        return Response(serializer.data)

    def post_data(self,request):
        serializer = Student_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

class StudentMainDetailView(APIView):

    def get_data(self,request,pk):
        try:
            student = StudentMainModel.objects.get(pk=pk)
        except:
            return Response({'message':'Student DoesNot Exists'})
        serializer =Student_serializer(student)
        return Response(serializer.data)

    def put_data(self,request,pk):
        try:
            student = StudentMainModel.objects.get(pk=pk)
        except:
            return Response({'message':'Student DoesNot Exists'})
        serializer = Student_serializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)


    def delete_data(self,request,pk):
        try:
            student = StudentMainModel.objects.get(pk=pk)
        except:
            return Response({'message':'Student DoesNot Exists'})
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class StudentMarksListView(APIView):

    def get_data(self,request):
        student = StudentMarksModel.objects.all()
        serializer = Student_Marks_Serializer(student,many=True)
        return Response(serializer.data)

    def post_data(self,request):
        serializer = Student_Marks_Serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()


class StudentMarksDetailView(APIView):

    def get_data(self, request, pk):
        try:
            student = StudentMarksModel.objects.get(pk=pk)
        except:
            return Response({'message':'Student Marks DoesNot Exists'})
        serializer = Student_Marks_Serializer(student)
        return Response(serializer.data)

    def put_data(self,request,pk):

        try:
            student = StudentMarksModel.objects.get(pk=pk)
        except:
            return Response({'message':'Student DoesNot Exists'})
        serializer = Student_Marks_Serializer(student,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)


    def delete_data(self,request,pk):
        try:
            student = StudentMarksModel.objects.get(pk=pk)
        except:
            return Response({'message':'Student Marks DoesNot Exists'})
        student.delete()


class Student_Marks_Main_List_View(APIView):
    def get_data(self, request):
        student = StudentMarksMainModel.objects.all()
        serializer =Student_Main_Marks_Serializer(student, many=True)
        return Response(serializer.data)

    def post_data(self, request):
        serializer = Student_Main_Marks_Serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()


class StudentMarksMainDetailView(APIView):

    def get_data(self, request, pk):
        try:
            student = StudentMarksMainModel.objects.get(pk=pk)
        except:
            return Response({'message':'Student Final Marks DoesNot Exists'})
        serializer = Student_Main_Marks_Serializer(student)
        return Response(serializer.data)

    def put_data(self, request, pk):

        try:
            student = StudentMarksMainModel.objects.get(pk=pk)
        except:
            return Response({'message':'Student Final Marks DoesNot Exists'})

        serializer = Student_Main_Marks_Serializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)


    def delete_data(self, request, pk):
        try:
            student = StudentMarksMainModel.objects.get(pk=pk)
        except:
            return Response({'message':'Student Final Marks DoesNot Exists'})
        student.delete()


class studentDetailView(generics.RetrieveUpdateAPIView):
    queryset = StudentMainModel.objects.all()
    serializer_class = Student_serializer, Student_Marks_Serializer
    lookupfield = 'Rollno'


    def get_queryset(self):
        queryset = StudentMainModel.objects.all()
        return queryset