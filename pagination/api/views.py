from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from .models import Buku, Kategori, Penulis
from .serializers import BukuSerializer, KategoriSerializer, PenulisSerializer

# Create your views here.
class StandardPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

class BukuViewSet(viewsets.ModelViewSet):
    queryset = Buku.objects.all().order_by('-terbit')
    serializer_class = BukuSerializer
    permission_classes = [IsAuthenticated]

    pagination_class = StandardPagination

class KategoriViewSet(viewsets.ModelViewSet):
    queryset = Kategori.objects.all()
    serializer_class = KategoriSerializer
    permission_classes = [IsAuthenticated]

class PenulisViewSet(viewsets.ModelViewSet):
    queryset = Penulis.objects.all()
    serializer_class = PenulisSerializer
    permission_classes = [IsAuthenticated]