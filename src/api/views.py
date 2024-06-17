# from rest_framework import viewsets
# from .models import TestData
# from .serializers import TestDataSerializer

# class TestDataViewSet(viewsets.ModelViewSet):
#     queryset = TestData.objects.all()
#     serializer_class = TestDataSerializer
from rest_framework import generics
from .models import Word
from .serializers import WordSerializer

class WordListCreate(generics.ListCreateAPIView):
    queryset = Word.objects.all().order_by('word')
    serializer_class = WordSerializer
