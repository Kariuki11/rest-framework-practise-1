from django.shortcuts import render, redirect
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db.models import Q

from .models import Advocate
from .serializers import AdvocateSerializer

# Create your views here.

# GET  /advocates
# POST /avocates

@api_view(['GET'])
def endpoints(request):
    data = ['/advocates', 'advocates/:username']
    return JsonResponse(data, safe=False)

@api_view(['GET' "POST"])
def advocate_list(request):
    #Handles Get requests
    if request.method == 'GET':
        query = request.GET.get('query')
    
    
    if query == None:
        query = ''
    
    advocates = Advocate.objects.filter(Q(username__icontains=query) | Q(bio_icontains=query))
    serializer = AdvocateSerializer(advocates, many=True)
    return Response(serializer.data)  # Use serializer.data here

    if request.method == 'POST':
        
        advocate = Advocate.objects.create(
            username = request.data['username'],
            bio=request.data['bio']
            )
        
        serializer = AdvocateSerializer(advocate, many=False)
        
        return Response(serializer.data)

    
    


@api_view(['GET' "PUT", "DELETE"])
def advocate_detail(request, username):
    advocate = Advocate.objects.get(username=username)  # Adjust to match your model's fields
    serializer = AdvocateSerializer(advocate, many=False)
    return Response(serializer.data)
    
    
    1hr: 17 minutes

