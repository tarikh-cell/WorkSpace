import json
from .models import User
from django.shortcuts import get_object_or_404
from django.http import JsonResponse

def user_api(request):
    user = get_object_or_404(User, id=request.user.id)
    return JsonResponse({'user':{
        "username":user.username,
        "password":user.password,
    }})