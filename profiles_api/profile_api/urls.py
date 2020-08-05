from django.urls import path,include
from rest_framework.routers import DefaultRouter

from profile_api import views

router = DefaultRouter()

router.register('hello-viewset',views.HelloViewSet,basename="hello-viewset")
router.register('user-profile', views.UserProfileViewSet)
router.register('feed', views.UserProfileFeedViewSet)

urlpatterns = [
    path('hello-view/', views.HelloAPIView.as_view()),
    path("", include(router.urls)),
    path("login/",views.UserApiLoginView.as_view())
]