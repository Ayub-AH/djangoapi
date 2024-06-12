from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from .models import Hadith
from .serializers import HadithSerializer
# Create your views here.
class HadithListCreate(generics.ListCreateAPIView):
    queryset= Hadith.objects.all()
    serializer_class = HadithSerializer
    def delete(self, request, *args, **kwargs):
        Hadith.objects.all().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
class HadithRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset= Hadith.objects.all()
    serializer_class = HadithSerializer
    lookup_field = "pk"
