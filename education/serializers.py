from rest_framework import serializers # type: ignore
from .models import Course, Department, Semester, Subject, Silabus

class CourseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Course
        fields = ['url', 'id', 'name', 'icon', 'description', 'qualification', 'duration', 'is_active']

class DepartmentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Department
        fields = ['url', 'id', 'name', 'description', 'course', 'is_active']

class SemesterSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Semester
        fields = ['url', 'id', 'name', 'course', 'department']

class SubjectSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Subject
        fields = ['url', 'id', 'name', 'author']

class SilabusSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Silabus
        fields = ['url', 'id', 'semester', 'department', 'course', 'subject', 'silabus']
