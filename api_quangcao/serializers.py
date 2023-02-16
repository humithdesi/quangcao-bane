from rest_framework import serializers
from .models import Category,Post
class CategorySet(serializers.ModelSerializer):# tạo serializer Author để gắn vào ProductSerializers
    class Meta:
        model=Category
        fields=['category','slug']    

class PostSerializer(serializers.ModelSerializer):# tạo serializer Author để gắn vào ProductSerializers
    category=CategorySet(many=True)
    class Meta:
        model=Post
        fields=['titte','image','content','category','slug','day_create','view'] 

class CategorySerializer(serializers.ModelSerializer):# tạo serializer Author để gắn vào ProductSerializers
    posts=PostSerializer(many=True)
    class Meta:
        model=Category
        fields=['category','slug','posts']               