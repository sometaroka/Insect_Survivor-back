# from django.urls import path, include
# from rest_framework import routers
# from . import views

# router = routers.DefaultRouter()
# router.register('testdata', views.TestDataViewSet)

# urlpatterns = [
#     path('', include(router.urls))
# ]
from django.urls import path
from .views import WordListCreate

urlpatterns = [
    path('words/', WordListCreate.as_view(), name='word-list-create'),
]
