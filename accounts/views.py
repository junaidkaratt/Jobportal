from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import userregister,LoginSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken


class RegisterUserView(APIView):
    def post(self,request):
        serializer = userregister(data=request.data)
        if serializer.is_valid():
            user=serializer.save()
            return Response({"message":"user created successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class loginUserView(APIView):
   def post(self,request):
       serializer= LoginSerializer(data=request.data)
       if serializer.is_valid():
           user= serializer.validated_data['user']
           refresh= RefreshToken.for_user(user)
           return Response({
               'access': str(refresh.access_token),
               'refresh': str(refresh)
           },status=status.HTTP_200_OK)
       return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        
class ProtectedUserView(APIView):
    permission_classes= [IsAuthenticated]

    def get(self,request):
        return Response({"successfully authorised"})

