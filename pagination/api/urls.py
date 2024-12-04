from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BukuViewSet, KategoriViewSet, PenulisViewSet

router = DefaultRouter()
router.register(r'buku', BukuViewSet)
router.register(r'kategori', KategoriViewSet)
router.register(r'penulis', PenulisViewSet)

urlpatterns = [
    path('api/', include(router.urls))
]
