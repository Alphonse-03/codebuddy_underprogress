from django.db import models




class Java(models.Model):
    que=models.CharField(max_length=300)
    option1=models.CharField(max_length=100)
    option2=models.CharField(max_length=100)
    option3=models.CharField(max_length=100)
    option4=models.CharField(max_length=100)
    option_correct=models.CharField(max_length=100)









class Cpp(models.Model):
    que=models.CharField(max_length=300)
    option1=models.CharField(max_length=100)
    option2=models.CharField(max_length=100)
    option3=models.CharField(max_length=100)
    option4=models.CharField(max_length=100)
    option_correct=models.CharField(max_length=100)
class Python(models.Model):
    que=models.CharField(max_length=300)
    option1=models.CharField(max_length=100)
    option2=models.CharField(max_length=100)
    option3=models.CharField(max_length=100)
    option4=models.CharField(max_length=100)
    option_correct=models.CharField(max_length=100)

class Javascript(models.Model):
    que=models.CharField(max_length=300)
    option1=models.CharField(max_length=100)
    option2=models.CharField(max_length=100)
    option3=models.CharField(max_length=100)
    option4=models.CharField(max_length=100)
    option_correct=models.CharField(max_length=100)

class Django(models.Model):
    que=models.CharField(max_length=300)
    option1=models.CharField(max_length=100)
    option2=models.CharField(max_length=100)
    option3=models.CharField(max_length=100)
    option4=models.CharField(max_length=100)
    option_correct=models.CharField(max_length=100)

class C(models.Model):
    que=models.CharField(max_length=300)
    option1=models.CharField(max_length=100)
    option2=models.CharField(max_length=100)
    option3=models.CharField(max_length=100)
    option4=models.CharField(max_length=100)
    option_correct=models.CharField(max_length=100)