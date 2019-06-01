from django.conf.urls import url
from django.conf.urls import include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('helloviewset',views.HelloViewset,base_name='helloviewset')
router.register('profile',views.userProfileViewSet)
router.register('login',views.LoginViewSet,base_name='login')
router.register('feed',views.ProfileFeedViewSet)

urlpatterns = [
    url(r'^home/',views.HelloApi.as_view()),
    url(r'',include(router.urls)),
]
