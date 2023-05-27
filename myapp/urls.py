from django.urls import path
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('users',BotUserApiView)
router.register('product',ProductApiView)
router.register('category',CategoryApiView)


urlpatterns = [
    # path('users',BotUserApiView.as_view(), name='bot-users'),
    # path('product',ProductApiView.as_view(), name='product'),
    # path('category',CategoryApiView.as_view(), name='category'),
    path('language',ChangeLanguage.as_view(), name='change'),
    path('user', BotUserInfo.as_view())
]