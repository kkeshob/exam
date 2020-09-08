from django.db import models
from django.conf import settings
class Course(models.Model):
    course=models.CharField(max_length=150,unique=True)
    
    def __str__(self):
        return self.course
class Paper(models.Model):
    paper=models.CharField(max_length=150)

    def __str__(self):
        return self.paper

class Questions(models.Model):
    qs_no=models.IntegerField()
    course=models.ForeignKey(Course,on_delete=models.CASCADE)
    paper=models.ForeignKey(Paper,on_delete=models.CASCADE)
    questions=models.TextField()
    
    answers=models.CharField(max_length=20)
    option_a=models.TextField()
    option_b=models.TextField()
    option_c=models.TextField()
    option_d=models.TextField()
    def __str__(self):
        return str(self.qs_no)+self.questions

class Answer(models.Model):
    student=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    question=models.ForeignKey(Questions,on_delete=models.CASCADE)
    answer=models.CharField(max_length=20)
    date=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.answer
