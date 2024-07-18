from django.db import models
from django.contrib.auth.models import User
from education.models import Semester, Course, Department

class College(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile = models.ImageField(upload_to='profiles/')
    place = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    district = models.CharField(max_length=100)
    panchayath = models.CharField(max_length=100)
    latitude = models.FloatField()
    longitude = models.FloatField()
    description = models.TextField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.user.username

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile = models.ImageField(upload_to='profiles/')
    college = models.ForeignKey(College, on_delete=models.SET_NULL, null=True)
    phone = models.CharField(max_length=15, null=True, blank=True)
    parent_name = models.CharField(max_length=100)
    relation = models.CharField(max_length=50)
    address = models.TextField()
    adhere_number = models.CharField(max_length=15, unique=True)
    parent_phone_number = models.CharField(max_length=15)
    place = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    panchayath = models.CharField(max_length=100)
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True)
    batch = models.PositiveIntegerField()
    current_class = models.CharField(max_length=50)
    STATUS_CHOICES = [
        ('studying', 'Studying'),
        ('stopped', 'Stopped'),
        ('removed', 'Removed'),
    ]
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='studying')
    action_discription = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.user.username

class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile = models.ImageField(upload_to='profiles/')
    college = models.ForeignKey(College, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15)
    degree = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    focus = models.IntegerField( blank=True, null=True ) 
    exam_invigilator = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_principal = models.BooleanField(default=False)
    # add adhar number
    
    def __str__(self):
        return self.user.username


