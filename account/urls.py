from django.urls import path # type: ignore
from .views import VerifyTokenView, AdminLoginView, CollegeRegisterView, CollegeView, LogoutView, CollegeLoginView, VerifyTokenCollegeView

urlpatterns = [
    path('verify-token/', VerifyTokenView.as_view(), name='verify-token'),
    path('admin/login/', AdminLoginView.as_view(), name='admin-login'),
    path('register/college/', CollegeRegisterView.as_view(), name='college-register'),
    path('login/college/', CollegeLoginView.as_view(), name='college-login'),
    path('colleges/', CollegeView.as_view(), name='college'),
    path('verify-college-token/', VerifyTokenCollegeView.as_view(), name='verify-college-token'),
    path('logout/', LogoutView.as_view(), name='logout'),
]