from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Advocate
from .serializers import AdvocateSerializer

# Create your views here.

@api_view(['GET'])
def endpoints(request):
    data = ['/advocates', 'advocates/:username']
    return JsonResponse(data, safe=False)

@api_view(['GET'])
def advocate_list(request):
    query = request.GET.get('query')
    
    
    if query == None:
        query = ''
    
    advocates = Advocate.objects.filter(username__icontains=query)
    serializer = AdvocateSerializer(advocates, many=True)
    return Response(serializer.data)  # Use serializer.data here

@api_view(['GET'])
def advocate_detail(request, username):
    advocate = Advocate.objects.get(username=username)  # Adjust to match your model's fields
    serializer = AdvocateSerializer(advocate, many=False)
    return Response(serializer.data)
    

