from django.db import models

# Create your models here.
class Doankhoa(models.Model):
    maDK = models.CharField(max_length= 10, primary_key= True)
    tenDK = models.CharField(max_length=255, null=False)
    def __str__(self):
        return f'{self.maDK}'
    
    class Meta:
        db_table = 'doankhoa'
        verbose_name = 'Đoàn Khoa'
        verbose_name_plural = 'Các Đoàn Khoa'
        
class Chidoan(models.Model):
    maCD = models.CharField(max_length=50, primary_key=True)
    tenCD = models.CharField(max_length=255, null=False)
    maDK = models.ForeignKey(Doankhoa, on_delete=models.CASCADE)

    def __str__(self):
        return self.tenCD

    class Meta:
        db_table = 'chidoan'
        verbose_name = 'Chi Đoàn'
        verbose_name_plural = 'Các Chi Đoàn'

class Doanvien(models.Model):
    maDV = models.CharField(max_length=50, primary_key=True)
    tenDV = models.CharField(max_length=255, null=False)
    maCD = models.ForeignKey(Chidoan, on_delete=models.CASCADE)
    ngay_sinh = models.DateField(null=False)
    GIOI_TINH_CHOICES = [
        (0, 'Nam'),
        (1, 'Nữ'),
    ]
    gioi_tinh = models.PositiveSmallIntegerField(choices=GIOI_TINH_CHOICES, default=0)
    que_quan = models.CharField(max_length=225, null=False)  
    sdt = models.CharField(max_length=15, null=True, blank=True) 
    ngay_vao_doan = models.DateField(null=False)  
    def __str__(self):
        return self.tenDV
    class Meta:
        db_table = 'doanvien'
        verbose_name = 'Đoàn Viên'
        verbose_name_plural = 'Đoàn Viên'