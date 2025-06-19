from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import userregister,LoginSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken, TokenError
from rest_framework_simplejwt.token_blacklist.models import BlacklistedToken, OutstandingToken 


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

class logoutUserView(APIView):
    permission_classes= [IsAuthenticated]

    def post(self, request):
        try:
            refresh= request.data["refresh"]
            token= RefreshToken(refresh)
            token.blacklist()
        
            return Response({"message": "Successfully logged out"}, status=status.HTTP_205_RESET_CONTENT)
        except KeyError:
            return Response({"error": "Refresh token required"}, status=status.HTTP_400_BAD_REQUEST)
        except TokenError as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

