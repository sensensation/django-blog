# from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Bb
from .serializers import PostSerializer
from django.forms import model_to_dict
from rest_framework.permissions import IsAuthenticatedOrReadOnly



#only serializers views

class PostAPIView(APIView):
   permission_classes = (IsAuthenticatedOrReadOnly, )
   def get(self, request):
      lst = Bb.objects.all().values()
      return Response({'All posts':list(lst)})

   def post(self, request):
      serializer = PostSerializer(data=request.data)
      serializer.is_valid(raise_exception=True)
      serializer.save()
      return Response({'post': serializer.data})

   def put(self, request, *args, **kwargs):
      pk = kwargs.get("pk", None)
      if not pk:
         return Response({"Erorr":"method PUT not allowed"})
      
      try:
         instance = Bb.objects.get(pk=pk)
      except:
         return Response({"Erorr":"object does not exists"})
      
      serializer = PostSerializer(data=request.data, instance=instance)
      serializer.is_valid(raise_exception=True)
      serializer.save()
      return Response({"post": serializer.data})
   
   def delete(self, request, *args, **kwargs):
      pk = kwargs.get("pk", None)
      post = Bb.objects.get(pk=pk)
      post.delete()
      return Response('Object deleted')
      