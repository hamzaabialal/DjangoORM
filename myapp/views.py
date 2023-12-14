from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView
from .models import Student, Departements
from .serializers import StudentSerializer, DepartementSerializer
# Create your views here.


class StudentData(ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)   

class StudentFilterData(ListCreateAPIView):
    queryset= Student.objects.filter(departement_name__name='Data Science')
    serializer_class = StudentSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


