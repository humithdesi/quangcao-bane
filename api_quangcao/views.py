from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .models import Post,Category
from .serializers import CategorySerializer, PostSerializer

# Create your views here.
class PostList(APIView):
    def get(self, request, format=None):
        posts= Post.objects.all()
        serializer =PostSerializer(posts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
class PostDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, slug):
        try:
            return Post.objects.get(slug=slug)
        except Post.DoesNotExist:
            raise Http404

    def get(self, request, slug, format=None):
        post = self.get_object(slug)
        serializer = PostSerializer(post)
        return Response(serializer.data)
class CategoryList(APIView):
    def get(self, request, format=None):
        categorys =Category.objects.all()
        serializer =CategorySerializer(categorys, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class CategoryDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, slug):
        try:
            return Category.objects.get(slug=slug)
        except Category.DoesNotExist:
            raise Http404

    def get(self, request, slug, format=None):
        category = self.get_object(slug)
        serializer = CategorySerializer(category)
        return Response(serializer.data)        

from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

class ExampleView(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        content = {
            'user': str(request.user),  # `django.contrib.auth.User` instance.
            'auth': str(request.auth),  # None
        }
        return Response(content)