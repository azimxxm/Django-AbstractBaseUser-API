from django.contrib import admin
from django.urls import path, include
from users.views import *

urlpatterns = [
    # Admin panel
    path('admin/', admin.site.urls),

    # Users all
    path('', MyUserView.as_view()),
    # Users detail
    path('<int:pk>/', MyUserViewDetail.as_view()),

    # Login and register urls
    path('login/', MyUserLogin.as_view()),
    path('register/', MyUserRegister.as_view()),

    # Rest Framework API Authentication
    path('rest-auth/', include('rest_framework.urls')),
]
