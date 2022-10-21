from django.contrib import admin
from .models import DongSanPham, LoaiSanPham, SanPham
# Register your models here.

admin.site.register(DongSanPham)
admin.site.register(LoaiSanPham)
admin.site.register(SanPham)