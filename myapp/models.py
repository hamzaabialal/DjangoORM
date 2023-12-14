from django.db import models

# Create your models here.


class Departements(models.Model):
    name = models.CharField(max_length = 1230)
    faculty = models.CharField(max_length= 1200)

    def __str__(self):
        return self.name


class Student(models.Model):
    name = models.CharField(max_length = 1000)
    departement_name = models.ForeignKey(Departements, on_delete=models.CASCADE, related_name='Departements_names', null=True, blank=True)
    roll_no = models.IntegerField()
    father_name = models.CharField(max_length=1000)