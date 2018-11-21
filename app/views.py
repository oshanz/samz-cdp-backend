from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.


def webhooks(request):
    response_data = {
        'id': 4,
        'name': 'Test Response',
        'roles': ['Admin', 'User']
    }

    return JsonResponse(response_data)
