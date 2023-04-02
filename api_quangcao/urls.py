from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import PostList,PostDetail,CategoryList,CategoryDetail,ExampleView

urlpatterns = [
     path('post', PostList.as_view(),name='Post_list'),
     path('post/<slug:slug>',PostDetail.as_view(),name='Post_detail'),
     path('category', CategoryList.as_view(),name='Category_list'),
     path('category/<slug:slug>', CategoryDetail.as_view(),name='Category_detail'),
     path('auth',ExampleView.as_view() )
]
urlpatterns=format_suffix_patterns(urlpatterns)
