from nturl2path import url2pathname
from django.urls import path
from .views import CustomUserCreate, BlacklistTokenView, GetUser
from . import views

app_name = 'users'

urlpatterns = [
    path('register/', CustomUserCreate.as_view(), name="create_user"),
    path('logout/blacklist/', BlacklistTokenView.as_view(), name='blacklist'),
    path('use/', GetUser.as_view(), name='user'),
    #path('login/', views.login_view, name="login_user"),
]