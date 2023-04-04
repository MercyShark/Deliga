from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken

from django.contrib.auth import authenticate


from .serializers import  (UserRegistrationSerializer ,
                            UserLoginSerializer,
                            UserChangePasswordSerializer,
                            UserInfoSerializer,
                            UserCheckEmailAvailabilitySerializer,
                            UserCheckUsernameAvailabilitySerializer)

from .renderes import UserRenderer

def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }


class UserRegistrationView(APIView):
    renderer_classes = [UserRenderer]
    def post(self,request,format=None):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message' : 'Registration Successfull! '},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_406_NOT_ACCEPTABLE)

class UserLoginView(APIView):
    renderer_classes = [UserRenderer]
    def post(self,request,format=None):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data.get('email')
            password = serializer.validated_data.get('password')
            user = authenticate(email = email , password = password)
            if user is not None:
                token = get_tokens_for_user(user)
                return Response({'token':token},status=status.HTTP_200_OK)
            else:
                return Response({'errors' : 'Invalid username or password!'})
        return Response(serializer.errors)

class UserInfoView(APIView):
    permission_classes = [IsAuthenticated]
    renderer_classes = [UserRenderer]

    def get(self,request,format=None):
        print('helo')
        print(request.user)
        serializer = UserInfoSerializer(request.user)
        print(serializer.data)
        return Response(serializer.data)
    
class UserChangePasswordView(APIView):
    permission_classes = [IsAuthenticated]
    renderer_classes = [UserRenderer]
    def post(self,request,format=None):
        serializer = UserChangePasswordSerializer(data=request.data,context={
            "user" : request.user
        })
        if serializer.is_valid():
            return Response({'message': 'Password Change Successfully!!'},status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class UserCheckEmailAvailabilityView(APIView):
    permission_classes = [IsAuthenticated]
    renderer_classes = [UserRenderer]

    def post(self,request,format=None):
        serializer = UserCheckEmailAvailabilitySerializer(data=request.data)
        if serializer.is_valid():
            return Response({'success' : 'Email does not exists!'},status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)
    
class UserCheckUsernameAvailabilityView(APIView):
    permission_classes = [IsAuthenticated]
    renderer_classes = [UserRenderer]

    def post(self,request,format=None):
        serializer = UserCheckUsernameAvailabilitySerializer(data=request.data)
        if serializer.is_valid():
            return Response({'success' : 'Username does not exists!'},status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)

