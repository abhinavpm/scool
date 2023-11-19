from rest_framework import serializers
from teacher.models import Student, Teacher


class StudentRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields='__all__'
