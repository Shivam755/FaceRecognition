import string
from django.db import models


# Create your models here.
class StudentModel(models.Model):
    name = models.CharField(max_length=100)
    rollNum = models.IntegerField(primary_key=True)

    def __str__(self) -> str:
        string = f"{self.name}({self.rollNum})"
        return string


class AttendanceModel(models.Model):
    student = models.ForeignKey(to=StudentModel, on_delete=models.CASCADE)
    datetime = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        string = f"{self.student.rollNum}({self.datetime})"
        return string
