from rest_framework import serializers
from .models import Book
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model=Book
        # fields = ['id','name','Auther','Number_of_pages']
        fields = '__all__'