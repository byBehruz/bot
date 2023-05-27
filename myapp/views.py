from django.shortcuts import render
from urllib.parse import urlparse
from django.conf import settings
from django.http import HttpResponseRedirect
from django.urls.base import resolve, reverse
from django.urls.exceptions import Resolver404
from django.utils import translation
from .models import BotUser, Product, Category
from .serializers import BotUserSerializer, ProductSerializer, CategorySerializer
# from rest_framework.generics import ListCreateAPIView

from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import filters
from .models import *
from .serializers import *


def set_Language(request, language):
    for lang, _ in settings.LANGUAGES:
        translation.activate(lang)
        try:
            view = resolve(urlparse(request.Meta.get('HTTP_REFERER')).path)
        except Resolver404:
            view= None
        if view:
            break
    if view:
        translation.activate(language)
        next_url = reverse(view.url_name, args=view.args, kwargs=view.kwargs)
        response = HttpResponseRedirect(next_url)
        response.set_cookie(settings.LANGUAGE_COOKIE_NAME, language)
    else:
        response = HttpResponseRedirect('/')
        return response


class BotUserApiView(ModelViewSet):
    queryset = BotUser.objects.all()
    serializer_class = BotUserSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']

class ProductApiView(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class CategoryApiView(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

from rest_framework.views import APIView
class ChangeLanguage(APIView):
    def post(self,request):
        data=request.POST
        data=data.dict()
        telegram_id= data['telegram_id']
        user = BotUser.objects.get(telegram_id=telegram_id)
        user.language=data['language']
        user.save()
        return Response({'Language changed'})

class BotUserInfo(APIView):
    def post(self, request):
        data = request.data
        botuser = BotUser.objects.get(telegram_id = data['telegram_id'])
        serializer = BotUserSerializer(instance=botuser, partial=True)
        return Response(serializer.data)
       