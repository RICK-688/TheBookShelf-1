# _*_ coding: utf-8 _*_

__author__ = 'Tim'
__date__ = '04/07/2021 23:03'

from django.urls import path, include
from django.views.decorators.csrf import csrf_exempt

from rest_framework.routers import DefaultRouter
from .views import BookcaseView, BookMarkView

router = DefaultRouter()

urlpatterns = [
    path('bookcase/add/', BookcaseView.as_view(), name='bookshelf'),
    path('bookmark/add/', BookMarkView.as_view(), name='bookmark')
]
