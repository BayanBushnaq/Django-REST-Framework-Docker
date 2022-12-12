from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView,RetrieveAPIView , RetrieveUpdateAPIView , RetrieveUpdateDestroyAPIView
from .serializers import BookSerializer
# Create your views here.
from .models import Book
class BookListView(ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer