from django.http import JsonResponse

response = JsonResponse({'foo': 'bar'})
response.content