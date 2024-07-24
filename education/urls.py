from django.urls import path, include # type: ignore
from rest_framework.routers import DefaultRouter # type: ignore
from .views import CourseViewSet, DepartmentViewSet, SemesterViewSet, SubjectViewSet, SilabusViewSet

router = DefaultRouter()
router.register(r'courses', CourseViewSet)
router.register(r'departments', DepartmentViewSet)
router.register(r'semesters', SemesterViewSet)
router.register(r'subjects', SubjectViewSet)
router.register(r'silabuses', SilabusViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
