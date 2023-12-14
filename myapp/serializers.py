from rest_framework import serializers
from .models import Student, Departements


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'


class DepartementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departements
        fields = '__all__'