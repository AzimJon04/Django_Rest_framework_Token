from django.urls import path

from .views import Postdetail, PostList

urlpatterns = [
    path('<int:pk>/', Postdetail.as_view(), name="post_detail"),
    path('', PostList.as_view(), name="post_list"),
]
