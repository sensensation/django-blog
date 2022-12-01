# from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Bb
from .serializers import PostSerializer
from .permissions import IsAuthorOrReadOnly, IsAdminOrReadOnly
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly



#only serializers views

class PostAPIList(generics.ListCreateAPIView):
   queryset = Bb.objects.all()
   serializer_class = PostSerializer
   permission_classes = (IsAuthenticatedOrReadOnly, )


class PostAPIUpdate(generics.RetrieveUpdateAPIView):
   queryset = Bb.objects.all()
   serializer_class = PostSerializer
   permission_classes = (IsAuthorOrReadOnly,)


class PostAPIDestroy(generics.RetrieveDestroyAPIView):
   queryset = Bb.objects.all()
   serializer_class = PostSerializer
   permission_classes = (IsAdminOrReadOnly,)