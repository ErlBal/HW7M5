import random
from rest_framework.decorators import api_view, permission_classes
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from rest_framework.response import Response
from users.serializers import UserLoginSerializer, UserRegisterSerializer, ConfirmSerializer
from users.models import VerificationCode
from django.shortcuts import get_object_or_404
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView

class RegisterAPIView(APIView):
    serializer_class = UserRegisterSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = User.objects.create_user(is_active=False, **serializer.validated_data)
        verifycation = VerificationCode.objects.create(user=user, code=random.randint(100000, 999999))

        return Response({
            'status': 201,
            'code': verifycation.code,
            'data': serializer.data
        })

class ConfirmAPIView(APIView):
    serializer_class = ConfirmSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        code = serializer.validated_data.get('code')
        confirm = get_object_or_404(VerificationCode, code=code)
        user = confirm.user
        user.is_active = True
        user.save()
        confirm.delete()

        return Response(
            {
                'status': 200,
                'status': 'user activated'
            },
        )

class LoginAPIView(APIView):
    serializer_class = UserLoginSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = authenticate(**serializer.validated_data)
        if user:
            token, created = Token.objects.get_or_create(user=user)
            user.save()
            return Response({'token': token.key})
        return Response({'error': 'Invalid credentials'}, status=400)





