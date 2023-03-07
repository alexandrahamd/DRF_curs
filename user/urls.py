from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from user.apps import UserConfig
from user.views import UserViewSet

app_name = UserConfig.name
router = DefaultRouter()
router.register(r'', UserViewSet, basename='user')

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
              ] + router.urls