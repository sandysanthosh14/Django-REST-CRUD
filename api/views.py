from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import TaskSerializer
from .models import Item

# Create your views here.
@api_view(['GET'])
def tasklist(request):
    task=Item.objects.all()
    serializer=TaskSerializer(task,many=True)
    return Response(serializer.data)
@api_view(['GET'])
def taskDetails(request,id):
    task=Item.objects.get(id=id)
    serializer=TaskSerializer(task,many=False)
    return Response(serializer.data)
@api_view(['POST'])
def taskCreate(request):
    serializer=TaskSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)
@api_view(['POST'])
def taskUpdate(request,id):
    task=Item.objects.get(id=id)
    serializer=TaskSerializer(instance=task,data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)
@api_view(['DELETE'])
def taskDelete(request,id):
    task=Item.objects.get(id=id)
    task.delete()

    return Response(serializer.data)


