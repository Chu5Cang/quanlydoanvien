from django import forms
from .models import Doankhoa
from .models import Chidoan
from .models import Doanvien 
import datetime
class DoankhoaForm(forms.ModelForm):
    class Meta:
        model = Doankhoa
        fields = ['maDK', 'tenDK']
        widgets = {
            'maDK': forms.TextInput(attrs={'placeholder': 'Mã Đoàn Khoa'}),
            'tenDK': forms.TextInput(attrs={'placeholder': 'Tên Đoàn Khoa'}),
        }
        labels = {
            'maDK': 'Mã Đoàn Khoa',
            'tenDK': 'Tên Đoàn Khoa',
        }
    def __init__(self, *args, **kwargs):
        super(DoankhoaForm, self).__init__(*args, **kwargs)
        if self.instance.pk:  # Kiểm tra xem đây có phải là trường hợp sửa không
            self.fields['maDK'].widget.attrs['readonly'] = True
    

class ChidoanForm(forms.ModelForm):
    class Meta:
        model = Chidoan
        # Liệt kê các trường cần có trong form, ví dụ: mã chi đoàn, tên chi đoàn, đoàn khoa, v.v.
        fields = ['maCD', 'tenCD', 'maDK']  # Chỉnh sửa danh sách này theo yêu cầu của bạn
        
        # Tùy chọn thêm cấu hình widgets cho các trường (nếu cần thiết)
        widgets = {
            'maCD': forms.TextInput(attrs={'placeholder': 'Nhập mã chi đoàn'}),
            'tenCD': forms.TextInput(attrs={'placeholder': 'Nhập tên chi đoàn'}),
            'maDK': forms.Select(attrs={'class': 'form-control'}),
        }
        
        # Tùy chọn thêm cấu hình tiêu đề dễ đọc cho các trường
        labels = {
            'maCD': 'Mã Chi Đoàn',
            'tenCD': 'Tên Chi Đoàn',
            'maDK': 'Đoàn Khoa',
        }

    def __init__(self, *args, **kwargs):
        super(ChidoanForm, self).__init__(*args, **kwargs)
        if self.instance.pk:  # Kiểm tra xem đây có phải là trường hợp sửa không
            self.fields['maCD'].widget.attrs['readonly'] = True  # Chỉ đọc nếu đang sửa
            
# Tao form uploadfile
class ImportExcelForm(forms.Form):
    file = forms.FileField(label="Chọn file Excel")

class DoanvienForm(forms.ModelForm):
    class Meta:
        model = Doanvien
        fields = ['maDV', 'tenDV', 'maCD', 'gioi_tinh', 'ngay_sinh', 'que_quan', 'sdt', 'ngay_vao_doan']
        widgets = {
            'maDV': forms.TextInput(attrs={'placeholder': 'Mã Đoàn Viên'}),
            'tenDV': forms.TextInput(attrs={'placeholder': 'Tên Đoàn Viên'}),
            'maCD': forms.TextInput(attrs={'placeholder': 'Mã Chi Đoàn'}),
            'gioi_tinh': forms.Select(attrs={'class': 'form-control'}),
            'ngay_sinh': forms.DateInput(attrs={'placeholder': 'Ngày Sinh', 'type': 'date'}),  # Đặt type là date
            'que_quan': forms.TextInput(attrs={'placeholder': 'Quê Quán'}),
            'sdt': forms.TextInput(attrs={'placeholder': 'SĐT'}),
            'ngay_vao_doan': forms.DateInput(attrs={'placeholder': 'Ngày Vào Đoàn', 'type': 'date'}),  # Đặt type là date
        }
        labels = {
            'maDV': 'Mã Đoàn Viên',
            'tenDV': 'Tên Đoàn Viên',
            'maCD': 'Mã Chi Đoàn',
            'gioi_tinh': 'Giới Tính',
            'ngay_sinh': 'Ngày Sinh',
            'que_quan': 'Quê Quán',
            'sdt': 'SĐT',
            'ngay_vao_doan': 'Ngày Vào Đoàn',
        }

    def __init__(self, *args, **kwargs):
        super(DoanvienForm, self).__init__(*args, **kwargs)
        if self.instance.pk:  # Kiểm tra xem đây có phải là trường hợp sửa không
            self.fields['maCD'].widget.attrs['readonly'] = True  # Chỉ đọc nếu đang sửa