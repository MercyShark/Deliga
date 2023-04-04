from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from apps.account.renderes import UserRenderer

from .serializer import CreatePostSerializer , ShowPostSerializer
from .models import Post

class CreatePostView(APIView):
    renderer_classes = [UserRenderer]
    permission_classes = [IsAuthenticated]
    def post(self,request,format=None): 
        serializer = CreatePostSerializer(data=request.data ,context={
            'user' : request.user
        })
        if serializer.is_valid():
            serializer.save()
            print(serializer.validated_data)
            print(serializer.data)
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_401_UNAUTHORIZED)

class ShowPostView(ListAPIView):
    serializer_class = ShowPostSerializer
    def get_queryset(self):
        queryset = Post.objects.all()
        return queryset
    
    def list(self, request, *args, **kwargs):
        response_data = {}        
        user = request.user
        if user.is_authenticated: 
            posts = self.get_queryset().filter(user = user)
            total_post = posts.count()
            serializer = ShowPostSerializer(posts,many=True)

            response_data['total_post'] = total_post
            response_data['posts'] = serializer.data
            return Response(response_data)
        return super().list(request,*args,**kwargs)
        
 
