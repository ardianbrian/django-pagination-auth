from rest_framework import serializers
from .models import Buku, Penulis, Kategori

class BukuSerializer(serializers.ModelSerializer):
    penulis_nama = serializers.CharField(source='penulis.nama', read_only=True)
    kategori_nama = serializers.CharField(source='kategori.nama', read_only=True)

    class Meta:
        model = Buku
        fields = '__all__'

class PenulisSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Penulis
        fields = '__all__'
    
class KategoriSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kategori
        fields = '__all__'
