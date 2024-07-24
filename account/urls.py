from django.urls import path
from .views import VerifyTokenView, AdminLoginView

urlpatterns = [
    path('verify-token/', VerifyTokenView.as_view(), name='verify-token'),
    path('admin/login/', AdminLoginView.as_view(), name='admin-login'),
]