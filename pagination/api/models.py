from django.db import models

# Create your models here.

class Penulis(models.Model):
    nama = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.nama
    
class Kategori(models.Model):
    nama = models.CharField(max_length=50)
    deskripsi = models.TextField(blank=True)

    def __str__(self):
        return self.nama
    
class Buku(models.Model):
    judul = models.CharField(max_length=200)
    penulis = models.ForeignKey(Penulis, on_delete=models.CASCADE)
    kategori = models.ForeignKey(Kategori, on_delete=models.CASCADE)
    harga = models.DecimalField(max_digits=10, decimal_places=2)
    stok = models.IntegerField(default=0)
    terbit = models.DateField()

    def __str__(self):
        return self.judul
