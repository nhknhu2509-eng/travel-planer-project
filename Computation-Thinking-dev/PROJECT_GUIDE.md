# HƯỚNG DẪN CẤU TRÚC THƯ MỤC VÀ QUY CHUẨN NHÁNH GIT (GROUP 02)
> **Môn học:** CSC10014 - Tư duy Tính toán (Computational Thinking)  
> **Dự án:** Trợ lý Ảo Lập Kế hoạch Du lịch Cá nhân hóa (Travel Planner Assistant)  
> **Áp dụng cho:** Tất cả các thành viên Group 02

---

## PHẦN 1: QUY CHUẨN ĐỔI TÊN NHÁNH CÁ NHÂN (BRANCH NAMING)

Hiện tại tên các nhánh cá nhân của nhóm đang bị phân tán và không đồng bộ (bạn có MSSV, bạn viết thường, bạn đặt tên theo tính năng). Nhóm thống nhất quy chuẩn tên nhánh cá nhân theo định dạng **tên cá nhân viết thường (không dấu)** để ngắn gọn và dễ thao tác.

### 1. Bảng quy đổi tên nhánh chuẩn của 5 thành viên

| STT | Thành viên | MSSV | Tên nhánh hiện tại | Tên nhánh MỚI chuẩn |
| :---: | :--- | :---: | :--- | :---: |
| 1 | Nguyễn Huỳnh Khánh Như | `25127222` | `25127222_Nhu` | **`nhu`** |
| 2 | Nguyễn Thị Hoàng Châu | `25127022` | `25127022_nthchau` | **`chau`** |
| 3 | Nguyễn Bạch Thành Nhân | `25127111` | `25127111_Nhan` *(hoặc `25127111/Lab01`)* | **`nhan`** |
| 4 | Từ Nguyễn Thuận Thiên | `25127146` | `algorithm_design_and_abstraction` | **`thien`** |
| 5 | Nguyễn Bình An | `23127149` | `An` *(hoặc `23127149_An`)* | **`an`** |

> ⚠️ **LƯU Ý QUAN TRỌNG VỀ COMMIT LOG:**  
> **Đổi tên nhánh HOÀN TOÀN KHÔNG làm mất commit log hay công sức đóng góp của bạn!**  
> Trong Git, nhánh chỉ là một chiếc nhãn dán (label) trỏ tới commit. Khi bạn đổi tên nhánh, toàn bộ lịch sử commit, tác giả, ngày giờ và code của bạn đều được giữ nguyên 100%.

---

### 2. Hướng dẫn các bước đổi tên nhánh

Mỗi bạn thực hiện **3 câu lệnh Git** cực kỳ đơn giản sau trên máy của mình:

#### Bước 1: Chuyển về nhánh cũ và đổi tên sang nhánh mới
*(Ví dụ với bạn Như, các bạn khác chỉ cần thay tên tương ứng theo bảng trên)*:
```bash
# 1. Chuyển sang nhánh hiện tại của bạn
git checkout 25127222_Nhu

# 2. Đổi tên nhánh cục bộ thành tên mới
git branch -m nhu
```

#### Bước 2: Đẩy nhánh tên mới lên GitHub
```bash
git push origin -u nhu
```

#### Bước 3: Xóa nhánh tên cũ trên GitHub
```bash
git push origin --delete 25127222_Nhu
```

*(Hoặc cách tiện nhất: Bạn có thể vào trực tiếp trang GitHub repo -> mục **Branches** -> bấm biểu tượng **Chiếc bút chì (Rename)** ở cạnh nhánh của bạn để đổi tên, GitHub sẽ tự động đổi và giữ nguyên toàn bộ lịch sử).*

---

## PHẦN 2: CẤU TRÚC THƯ MỤC DỰ ÁN (PROJECT DIRECTORY STRUCTURE)

Cây thư mục của dự án đã được thiết kế chuẩn chỉnh theo mô hình phát triển phần mềm chuyên nghiệp:

```text
Computation-Thinking/
├── src/                          # MÃ NGUỒN CHÍNH CỦA ỨNG DỤNG
│   ├── frontend/                 # Giao diện người dùng Web App (HTML/CSS/JS/React...)
│   └── backend/                  # Xử lý logic, thuật toán và API (Python)
│       ├── app/                  # Các module xử lý (lọc POI, Knapsack, TSPTW...)
│       ├── main.py               # Entrypoint khởi chạy server
│       └── requirements.txt      # Danh sách thư viện Python phụ thuộc
│
├── tests/                        # BỘ KIỂM THỬ (TESTING)
│   ├── frontend/                 # Test giao diện, luồng người dùng
│   └── backend/                  # Unit test thuật toán tính đường đi, ngân sách
│
├── docs/                         # TÀI LIỆU KỸ THUẬT & HỌC THUẬT CỦA ĐỒ ÁN
│   ├── 01_Engineering_Report/    # Báo cáo kỹ thuật chi tiết
│   ├── 03_Architecture_Design/   # Sơ đồ kiến trúc, mã giả (pseudocode), hợp đồng API
│   ├── 04_Evaluation_Pack/       # Bộ dữ liệu đánh giá, benchmark kiểm thử, độ đo
│   ├── 05_Failure_Risk_Pack/     # Phân tích rủi ro, dự phòng rủi ro và bảo mật dữ liệu
│   ├── 06_Presentation/          # Slide thuyết trình (Canva/PDF)
│   └── 07_Team_Logbook/          # Nhật ký đóng góp, phân chia task và ghi nhận AI Usage
│
├── submissions/                  # THƯ MỤC LƯU BÀI NỘP THEO TỪNG TUẦN
├── .gitignore                    # Chặn các file rác (.DS_Store, __pycache__, venv, *.zip)
├── README.md                     # Giới thiệu tổng quan về đề tài và nhóm
└── PROJECT_GUIDE.md              # File hướng dẫn cấu trúc và quy trình này
```



## PHẦN 3: QUY TRÌNH LÀM VIỆC GIT HÀNG NGÀY (DAILY WORKFLOW)

Để nhóm không bao giờ bị lệch code so với nhánh chính, mỗi khi làm việc các bạn tuân thủ **4 bước sau**:

1. **Trước khi bắt đầu làm:** Luôn kéo code mới nhất từ nhánh `dev` về nhánh cá nhân:
   ```bash
   git checkout <tên_nhánh>       # Về nhánh của bạn (ví dụ: git checkout nhu)
   git pull origin dev            # Cập nhật các thay đổi mới nhất từ nhóm về
   ```
2. **Khi làm bài:** Chỉ thao tác và chỉnh sửa file trong khu vực được phân công (xem bảng ở Phần 2).
3. **Khi làm xong (Lưu lại và đẩy lên):**
   ```bash
   git add .
   git commit -m "mô tả ngắn gọn công việc bạn vừa làm"
   git push origin <tên_nhánh>
   ```
4. **Hợp nhất vào nhánh chung (`dev`):**
   * Lên web GitHub, tạo một **Pull Request (PR)** từ nhánh cá nhân của bạn vào nhánh **`dev`**.
   * Nhắn tin cho nhóm để Leader hoặc các bạn cùng review và bấm merge.

