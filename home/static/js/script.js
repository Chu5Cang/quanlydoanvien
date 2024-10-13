// Khi người dùng nhấn bất cứ đâu ngoài modal, đóng modal
window.onclick = function(event) {
  if (event.target == modal) {
    modal.style.display = "none";
  }
}

// Thời gian ẩn bảng thông báo 
setTimeout(function() {
  var messages = document.querySelector('.messages');
  if (messages) {
      messages.style.display = 'none';
  }
}, 3000);  // Ẩn sau 3 giây


// Hàm hiển thị modal xác nhận xóa Đoàn Khoa
function confirmDeletedDoanKhoa(maDK) {
  var modal = document.getElementById("confirmDeleteModalDoanKhoa");
  var form = modal.querySelector("form");

  // Cập nhật action của form để gửi yêu cầu xóa đúng đối tượng
  form.action = "/doankhoa/" + maDK + "/delete/";

  // Hiển thị modal
  modal.style.display = "block";
}

// Hàm hiển thị modal xác nhận xóa Chi Đoàn
function confirmDeletedChiDoan(maCD) {
  var modal = document.getElementById("confirmDeleteModalChiDoan");
  var form = modal.querySelector("form");

  // Cập nhật action của form để gửi yêu cầu xóa đúng đối tượng
  form.action = "/chidoan/" + maCD + "/delete/";

  // Hiển thị modal
  modal.style.display = "block";
}
function confirmDeletedDoanVien(maDV) {
  var modal = document.getElementById("confirmDeleteModalDoanVien");  // Đổi thành confirmDeleteModalDoanVien
  var form = modal.querySelector("form");

  // Cập nhật action của form để gửi yêu cầu xóa đúng đối tượng
  form.action = "/doanvien/" + maDV + "/delete/";

  // Hiển thị modal
  modal.style.display = "block";
}

// Hàm đóng modal xác nhận Đoàn Khoa
function closeModalDoanKhoa() {
  var modal = document.getElementById("confirmDeleteModalDoanKhoa");
  modal.style.display = "none";
}

// Hàm đóng modal xác nhận Chi Đoàn
function closeModalChiDoan() {
  var modal = document.getElementById("confirmDeleteModalChiDoan");
  modal.style.display = "none";
}
function closeModalDoanVien() {
  var modal = document.getElementById("confirmDeleteModalDoanVien");  // Sửa tên ID cho đúng
  modal.style.display = "none";
}

// Đóng modal khi nhấn ra ngoài modal cho cả Đoàn Khoa và Chi Đoàn
window.onclick = function(event) {
  var modalDoanKhoa = document.getElementById("confirmDeleteModalDoanKhoa");
  var modalChiDoan = document.getElementById("confirmDeleteModalChiDoan");
  var modalDoanVien = document.getElementById("confirmDeleteModalDoanVien");

  if (event.target == modalDoanKhoa) {
      closeModalDoanKhoa();
  }

  if (event.target == modalChiDoan) {
      closeModalChiDoan();
  }

  if (event.target == modalDoanVien) {
      closeModalDoanVien();
  }
};