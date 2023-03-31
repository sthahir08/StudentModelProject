from rest_framework import serializers
from StudentApp.models import StudentMainModel, StudentMarksModel,StudentMarksMainModel

class Student_serializer(serializers.ModelSerializer):
    Branch = serializers.CharField(max_length=50,required=True)


    def validate(self, data):
        student_id = data.get('Rollno')
        student = StudentMainModel.objects.filter(Rollno=student_id).last()
        if student:
            raise serializers.ValidationError({"message":"student already exists with this number"})
        else:
            pass
        return data

    class Meta:
        model = StudentMainModel
        fields = '_all_'

class Student_Marks_Serializer(serializers.ModelSerializer):

    rank = serializers.SerializerMethodField(read_only=True)

    def get_rank(self,obj):
        if obj.Marks >25:
            return {'message':"Good Marks"}
        else:
            return {'message':"poor need to improve"}

    def validation(self, data):
        print(data)
        # print(self)
        student_id = data.get('student')
        semester = data.get('Semester')
        marks = data.get('Marks')
        existing_students = StudentMarksModel.objects.filter(student_id =student_id,Semester=semester)
        print(existing_students)
        if existing_students.exists():
            raise serializers.ValidationError({"message" : "Student Marks Already Exist with same Semester"} )
        return data

    class Meta:
        model = StudentMarksModel
        fields = ('student','Marks','Semester')


class Student_Main_Marks_Serializer(serializers.ModelSerializer):
    student = Student_serializer()
    student_Marks_details=serializers.SerializerMethodField(read_only=True)
    Passed = serializers.SerializerMethodField(read_only=True)


    def get_Passed(self,obj):
        total_marks = 500
        if ((obj.FinalMarks / total_marks) * 100) >=70:
            return "Distantion"
        if ((obj.FinalMarks / total_marks) * 100) >=60:
            return "1st Class"
        else:
            return "2nd Class"

    class Meta:
        model = StudentMarksMainModel
        fields = ('student','student_Marks_details','FinalMarks','Passed')