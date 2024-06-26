from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from project_management_app.views import UserViewSet, ProjectViewSet, TaskViewSet, CommentViewSet, register_user, login_user
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'projects', ProjectViewSet)
router.register(r'tasks', TaskViewSet)
router.register(r'comments', CommentViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/users/register/', register_user, name='register_user'),
    path('api/users/login/', login_user, name='login_user'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
