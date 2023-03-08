from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()
router.register(r'tables', BookingViewSet, basename='tables')

urlpatterns = [
    path('api-token-auth/', obtain_auth_token),
    path('booking/', include(router.urls)),
    path('menu/', MenuItemsView.as_view()),
    path('menu/<int:pk>/', SingleMenuItemView.as_view()),
]
