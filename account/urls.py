from django.urls import path
from .views import VerifyTokenView, AdminLoginView, CollegeRegisterView, CollegeView

urlpatterns = [
    path('verify-token/', VerifyTokenView.as_view(), name='verify-token'),
    path('admin/login/', AdminLoginView.as_view(), name='admin-login'),
    path('register/college/', CollegeRegisterView.as_view(), name='college-register'),
    path('colleges/', CollegeView.as_view(), name='college'),
]