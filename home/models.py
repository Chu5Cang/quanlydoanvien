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

class Chucvu(models.Model):
    maCV = models.CharField(max_length=20, primary_key=True)
    tenCV = models.CharField(max_length=100)

    def __str__(self):
        return self.tenCV
    class Meta:
            db_table = 'chucvu'
            verbose_name = 'Chức Vụ'
            verbose_name_plural = 'Các Chức VỤ'

class Doanvien(models.Model):
    maDV = models.CharField(max_length=20, primary_key=True)  # Mã Đoàn Viên
    tenDV = models.CharField(max_length=100)  # Tên Đoàn Viên
    maCD = models.ForeignKey(Chidoan, on_delete=models.CASCADE)  # Liên kết đến Chi Đoàn
    GIOI_TINH_CHOICES = [
        (0, 'Nam'),
        (1, 'Nữ'),
    ]
    gioi_tinh = models.PositiveSmallIntegerField(choices=GIOI_TINH_CHOICES, default=0)
    ngay_sinh = models.DateField()  # Ngày Sinh
    que_quan = models.CharField(max_length=100)  # Quê Quán
    sdt = models.CharField(max_length=15, default='N/A')  # Cung cấp giá trị mặc định
    ngay_vao_doan = models.DateField()  # Ngày Vào Đoàn
    maCV = models.ForeignKey(Chucvu, on_delete=models.CASCADE)  # Liên kết đến Chức Vụ

    def __str__(self):
        return self.tenDV
    class Meta:
        db_table = 'doanvien'
        verbose_name = 'Đoàn Viên'
        verbose_name_plural = 'Các Đoàn Viên' 

