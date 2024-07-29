from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

from.models import Advocate
from .serializers import AdvocateSerializer

# Create your views here.


@api_view(['GET'])
def endpoints(request):
    data = ['/advocates', 'advocates/:username']
    return JsonResponse(data, safe=False)

@api_view(['GET'])
def advocate_list(request):
    #data = ['Dennis', 'Tadas', 'Max']
    advocates = Advocate.objects.all()
    serializer = AdvocateSerializer(advocates, many=True)
    return Response(advocates.data)

@api_view(['GET'])
def advocate_detail(request, username):
    data = username
    return JsonResponse(data, safe=False)

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
    advocates = Advocate.objects.all()
    serializer = AdvocateSerializer(advocates, many=True)
    return Response(serializer.data)  # Use serializer.data here

@api_view(['GET'])
def advocate_detail(request, username):
    try:
        advocate = Advocate.objects.get(username=username)  # Adjust to match your model's fields
        serializer = AdvocateSerializer(advocate)
        return Response(serializer.data)
    except Advocate.DoesNotExist:
        return Response({'error': 'Advocate not found'}, status=404)

