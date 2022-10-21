from django.shortcuts import render

from .models import DongSanPham, LoaiSanPham, SanPham

# Create your views here.

def index(request):

	CacDongSanPham = DongSanPham.objects.all()

	context = {}

	context['data'] = {}
	for dong in CacDongSanPham:
		cacloai = SanPham.objects.filter(Loai__Dong=dong)
		context['data'][dong.Ten_Tieng_Viet] = cacloai

	return render(request, "index.html" , context)

def ProductLine(request , productLine):

    CacLoaiSanPham = LoaiSanPham.objects.filter(Dong__Ten=productLine)
    context = {}
    context['data'] = {}
    for loai in CacLoaiSanPham:
        cacsanpham = SanPham.objects.filter(Loai=loai)
        context['data'][loai.Ten_Tieng_Viet] = cacsanpham
    return render(request , "DongSanPham.html" , context)

def ProductType(request , productLine , productType):

    CacSanPham = SanPham.objects.filter(Loai__Ten=productType)
    context = {}
    return render(request , "LoaiSanPham.html" , context)
def OneProduct(request , productLine , productType , productCode):
    product = SanPham.objects.filter(id=productCode)
    context = {'product' : product}
    return render(request , "SanPham.html" , context)
