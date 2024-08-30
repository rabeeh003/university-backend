from rest_framework.views import APIView # type: ignore
from rest_framework import generics # type: ignore
from rest_framework.response import Response # type: ignore
from rest_framework.permissions import IsAuthenticated # type: ignore
from rest_framework_simplejwt.authentication import JWTAuthentication # type: ignore
from rest_framework_simplejwt.tokens import RefreshToken # type: ignore
from django.contrib.auth import authenticate # type: ignore
from django.contrib.auth.models import User # type: ignore
from rest_framework import status # type: ignore
from django.http import JsonResponse # type: ignore
from datetime import datetime, timedelta
from .serializers import UserSerializer, CollegeSerializer
from .models import College

# common view for all users

class LogoutView(APIView):
    def post(self, request, *args, **kwargs):
        user_type = request.data.get('user_type')
        
        if user_type not in ['admin', 'student', 'teacher', 'college']:
            return JsonResponse({'detail': 'Invalid user type'}, status=status.HTTP_400_BAD_REQUEST)
        
        cookie_name = user_type
        response = JsonResponse({'detail': 'Successfully logged out'}, status=status.HTTP_200_OK)
        response.delete_cookie(cookie_name)
        return response

# admin views

class VerifyTokenView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        if user.is_superuser:
            data = {
                'username': user.username,
                'first_name': user.first_name,
                'last_name': user.last_name,
                'email': user.email
            }
            return Response(data, status=status.HTTP_200_OK)
        else:
            return Response({'detail': 'Not a adminuser'}, status=status.HTTP_403_FORBIDDEN)


class AdminLoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        
        if user is not None and user.is_superuser:
            refresh = RefreshToken.for_user(user)
            data = {
                'refresh': str(refresh),
                'access': str(refresh.access_token),
                'user': user.id,
                'user_type': 'admin'
            }
            response = JsonResponse(data, status=status.HTTP_200_OK)
            expiration_time = datetime.utcnow() + timedelta(days=15)
            response.set_cookie(key='admin', value=data['access'], expires=expiration_time)
            return response
        return Response({'detail': 'Invalid credentials or not a superuser'}, status=status.HTTP_401_UNAUTHORIZED)


# start college views code.

class CollegeRegisterView(generics.CreateAPIView):
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        user_serializer = self.get_serializer(data=request.data)
        user_serializer.is_valid(raise_exception=True)
        user = user_serializer.save()

        college_data = {
            "user": user.id,  
            "place": request.data.get("place"),
            "phone": request.data.get("phone"),
            "district": request.data.get("district"),
            "panchayath": request.data.get("panchayath"),
        }

        college = College.objects.create(
            user=user,
            place=college_data.get("place"),
            phone=college_data.get("phone"),
            district=college_data.get("district"),
            panchayath=college_data.get("panchayath"),
        )

        college_serializer = CollegeSerializer(college)

        return Response({
            "user": user_serializer.data,
            "college": college_serializer.data
        }, status=status.HTTP_201_CREATED)
        
class CollegeView(generics.ListAPIView):
    queryset = College.objects.all()
    serializer_class = CollegeSerializer
    queryset = College.objects.all()
    
class CollegeLoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        
        if user is not None and not user.is_superuser and user.is_staff and user.is_active:
            refresh = RefreshToken.for_user(user)
            data = {
                'refresh': str(refresh),
                'access': str(refresh.access_token),
                'user': user.id,
                'user_type': 'college'
            }
            response = JsonResponse(data, status=status.HTTP_200_OK)
            expiration_time = datetime.utcnow() + timedelta(days=15)
            response.set_cookie(key='college', value=data['access'], expires=expiration_time)
            return response
        return Response({'detail': 'Invalid credentials or check inputs and login page.'}, status=status.HTTP_401_UNAUTHORIZED)
    
class VerifyTokenCollegeView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        if user.is_staff:
            data = {
                'username': user.username,
                'first_name': user.first_name,
                'last_name': user.last_name,
                'email': user.email
            }
            return Response(data, status=status.HTTP_200_OK)
        else:
            return Response({'detail': 'Not a college.'}, status=status.HTTP_403_FORBIDDEN)

