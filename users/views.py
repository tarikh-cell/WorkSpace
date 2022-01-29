import json
from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import RegisterUserSerializer
from rest_framework.permissions import AllowAny
#from django.contrib.auth import authenticate, login, logout
#from django.views.decorators.csrf import csrf_exempt
from rest_framework_simplejwt.tokens import RefreshToken

class CustomUserCreate(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        reg_serializer = RegisterUserSerializer(data=request.data)
        if reg_serializer.is_valid():
            newuser = reg_serializer.save()
            if newuser:
                return Response(status=status.HTTP_201_CREATED)
        return Response(reg_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BlacklistTokenView(APIView):
    permission_classes = [AllowAny]
    authentication_classes = ()

    def post(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)

#@csrf_exempt
#def login_view(request):
#    if request.method == "POST":
#        json_body = json.loads(request.body)
#        user = authenticate(
#            request,
#            username=json_body.get('user_name'),
#            password=json_body.get('password'),
#        )
#        if user is not None:
#            login(request, user)
#            return JsonResponse(data={}, status=status.HTTP_200_OK)
#        else:
#            return JsonResponse(data={}, status=status.HTTP_404_NOT_FOUND)