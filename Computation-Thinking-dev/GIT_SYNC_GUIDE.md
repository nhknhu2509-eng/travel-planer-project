# HƯỚNG DẪN ĐỒNG BỘ NHÁNH CÁ NHÂN VỚI NHÁNH DEV (GIỮ NGUYÊN 100% COMMIT CŨ)

Tài liệu này hướng dẫn các thành viên trong nhóm **Group 02** cách đồng bộ mã nguồn và tài liệu trên nhánh cá nhân của mình để **giống 100% với nhánh chuẩn `dev`**, đồng thời **bảo toàn nguyên vẹn 100% lịch sử commit đóng góp trong quá khứ** để giảng viên chấm điểm.

---

## I. NGUYÊN TẮC QUAN TRỌNG

1. **Commit cũ có bị mất không?**  
   👉 **HOÀN TOÀN KHÔNG.** Trong Git, toàn bộ các commit mà bạn đã tạo trong quá khứ (mã hash, ngày giờ, tên tác giả, các dòng code/báo cáo đã viết) đều được lưu vĩnh viễn trong lịch sử Git.
2. **Nội dung mới lấy từ đâu?**  
   👉 Toàn bộ thư mục và file sẽ được cập nhật chuẩn chỉnh theo nhánh `dev` (đã tổng hợp đầy đủ báo cáo, slide PDF, logbook, và tài liệu nộp bài).

---

## II. DANH SÁCH NHÁNH CỦA TỪNG THÀNH VIÊN

| STT | Thành viên | Mã số sinh viên | Tên nhánh cá nhân (`<tên_nhánh>`) |
| :---: | :--- | :---: | :--- |
| 1 | Nguyễn Huỳnh Khánh Như | `25127222` | `25127222_Nhu` |
| 2 | Nguyễn Thị Hoàng Châu | `25127022` | `25127022_nthchau` |
| 3 | Nguyễn Bạch Thành Nhân | `25127111` | `25127111_Nhan` *(hoặc `25127111/Lab01`)* |
| 4 | Từ Nguyễn Thuận Thiên | `25127146` | `algorithm_design_and_abstraction` |
| 5 | Nguyễn Bình An | `23127149` | `An` |

---

## III. QUY TRÌNH ĐỒNG BỘ 4 BƯỚC (COPY-PASTE VÀ CHẠY)

Mỗi bạn mở **Terminal** tại thư mục dự án và thực hiện tuần tự 4 bước sau:

### Bước 1: Chuyển về nhánh cá nhân và lấy dữ liệu mới nhất
Thay `<tên_nhánh>` bằng tên nhánh của bạn (xem bảng ở Mục II):
```bash
git checkout <tên_nhánh>
git fetch origin
```
*(Ví dụ với bạn Như: `git checkout 25127222_Nhu` rồi gõ `git fetch origin`)*

---

### Bước 2: Bắt đầu gộp nhánh `dev`
Chạy lệnh gộp mà không vội chốt commit tự động:
```bash
git merge origin/dev --no-commit
```

---

### Bước 3: Ép toàn bộ file và thư mục giống hệt `dev` 100%
Chạy lệnh lấy toàn bộ cây thư mục chuẩn của `dev` đè vào nhánh hiện tại:
```bash
git checkout origin/dev -- .
```
*(Dấu chấm `.` ở cuối có nghĩa là áp dụng cho toàn bộ dự án: file nào trên `dev` có thì sẽ có, file nào `dev` đã dọn thì sẽ tự dọn sạch).*

---

### Bước 4: Lưu lại và đẩy lên GitHub
```bash
git commit -m "sync 100% with dev branch"
git push origin <tên_nhánh>
```
*(Ví dụ với bạn Như: `git push origin 25127222_Nhu`)*

---

## IV. CÁCH KIỂM TRA LẠI SAU KHI XONG

Sau khi chạy xong 4 bước trên, bạn có thể tự kiểm tra để hoàn toàn an tâm:

1. **Kiểm tra trạng thái thư mục (phải sạch sẽ):**
   ```bash
   git status
   ```
   *(Kết quả báo `nothing to commit, working tree clean` là chuẩn).*

2. **Kiểm tra các commit cũ của bạn vẫn còn nguyên:**
   ```bash
   git log --oneline -n 10
   ```
   *(Bạn sẽ thấy các commit ngày xưa của bạn vẫn nằm ngay trong danh sách, kèm thêm 1 commit đồng bộ mới nhất ở trên cùng).*

---

## V. XỬ LÝ KHI GẶP MÀN HÌNH VIM / NANO (NẾU CÓ)
Nếu terminal tự động mở một màn hình chữ đen nền xanh/đen để nhập commit message:
* **Nếu là giao diện Vim:** Nhấn phím `Esc`, gõ `:wq` rồi nhấn `Enter`.
* **Nếu là giao diện Nano:** Nhấn tổ hợp phím `Ctrl + O` $\rightarrow$ `Enter` $\rightarrow$ `Ctrl + X` để thoát ra.
