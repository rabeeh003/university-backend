from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)
from rest_framework.routers import DefaultRouter
from education.views import CourseViewSet, DepartmentViewSet, SemesterViewSet, SubjectViewSet, SilabusViewSet

# Initialize the default router and register viewsets
router = DefaultRouter()
router.register(r'courses', CourseViewSet)
router.register(r'departments', DepartmentViewSet)
router.register(r'semesters', SemesterViewSet)
router.register(r'subjects', SubjectViewSet)
router.register(r'silabuses', SilabusViewSet)

# Project-level URL patterns
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('rest_framework.urls')),  # Browsable API login/logout views
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('education/', include(router.urls)),  # Include app-level URLs using the router
    path('account/', include('account.urls')), 
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)