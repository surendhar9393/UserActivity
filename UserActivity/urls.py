from django.contrib import admin
from django.conf.urls import url

# local imports
from UserActivity.user import views

urlpatterns = [
    url('admin/', admin.site.urls),
    url('login/', views.UserLogin.as_view(), name='user-login'),
    url('user/detail', views.UserDetail.as_view(), name='user-detail')
]
