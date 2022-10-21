from django.db import models

# Create your models here.

class DongSanPham(models.Model):
    Ten_choices = [
        ( 'Mypham' , 'Mỹ phẩm') ,
        ( 'Tuixach', 'Túi xách') ,
        ( 'Quanao' , 'Quần áo') ,
    ]

    Ten = models.CharField(choices=Ten_choices , max_length=50)
    Ten_Tieng_Viet = models.CharField(max_length=50)

    def __str__(self):
        return self.Ten_Tieng_Viet

class LoaiSanPham(models.Model):

    Ten_choices = [
        ('Balo'     ,'Ba lô' ),
        ('Kem'      , 'Kem' ),
        ('Son'      , 'Son' ),
        ('Nuochoa'  , 'Nước hoa'),
        ('Quan'     , 'Quần'),
        ('Ao'       , 'Áo'),
        ('PhanTrangDiem' , 'Phấn trang điểm'),
    ]

    Ten = models.CharField(choices=Ten_choices , max_length=50)
    Ten_Tieng_Viet = models.CharField(max_length=50)

    Dong = models.ForeignKey(
        "DongSanPham" ,
        on_delete=models.CASCADE
    )
    def __str__(self):
        return self.Ten_Tieng_Viet

class SanPham(models.Model):

    Ten = models.CharField(max_length=50)
    Gia_ban_dau = models.IntegerField(default = 200000)
    Gia_giam = models.IntegerField(default=1000000)
    Mo_ta_san_pham = models.TextField(default = "Kem tri nam")
    Anh_san_pham = models.ImageField(upload_to='pictures/')

    Loai = models.ForeignKey(
        "LoaiSanPham" ,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.Ten
