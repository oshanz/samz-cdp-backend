from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.


@csrf_exempt
def webhooks(request):
    # print(request.body)
    response_data = {
        # "speech": 'oshan awesome speech',
        # "displayText": 'oshan awesome display',
        "source": "Build conversational interface for your app in 10 minutes.",
        'fulfillmentText': "oshan awesome fulfilment"
    }

    return JsonResponse(response_data)
