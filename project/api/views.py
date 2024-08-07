from django.shortcuts import render
from rest_framework.response import Response
from .serializers import MovieSerializer
from .models import MovieModel
from rest_framework import status
from rest_framework import viewsets

# Create your views here.
class MovieViewSet(viewsets.ViewSet):
    
    def list(self, request):
        stu = MovieModel.objects.all()
        serializer = MovieSerializer(stu, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        id = pk
        if id is not None:
            stu = MovieModel.objects.get(id=id)
            serializer = MovieSerializer(stu)
            return Response(serializer.data)

    def create(self, request):
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Created'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self,request, pk):
        id = pk
        stu = MovieModel.objects.get(pk=id)
        serializer = MovieSerializer(stu, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Complete Data Updated'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self,request, pk):
        id = pk
        stu = MovieModel.objects.get(pk=id)
        serializer = MovieSerializer(stu, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Partial Data Updated'})
        return Response(serializer.errors)

    def destroy(self,request, pk):
        id = pk
        stu = MovieModel.objects.get(pk=id)
        stu.delete()
        return Response({'msg':'Data Deleted'})
    