from django.urls import path

from .views import EditPost, PostList, PostDetail, CreatePost, EditPost, DeletePost

app_name = 'documents_api'

urlpatterns = [
    path('<int:pk>/', PostDetail.as_view(), name="detailcreate"),
    path('', PostList.as_view(), name='listcreate'),
    path('create/', CreatePost.as_view(), name='createpost'),
    path('edit/<int:pk>/', EditPost.as_view(), name='editpost'),
    path('delete/<int:pk>', DeletePost.as_view(), name='deletepost'),
]