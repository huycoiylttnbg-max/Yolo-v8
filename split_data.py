import os
import random
import shutil

# --- 1. CẤU HÌNH ĐƯỜNG DẪN (DÀNH CHO MÁY TÍNH / VS CODE) ---
# THAY ĐỔI ĐƯỜNG DẪN DƯỚI ĐÂY THÀNH THƯ MỤC THỰC TẾ TRÊN MÁY CỦA BẠN
# Lưu ý: Dùng dấu gạch chéo tiến (/) thay vì gạch chéo ngược (\) để tránh lỗi trên Windows
SOURCE_DIR = 'D:/Data_YOLO/dlib/newdata' 

# Thư mục mới sẽ chứa dữ liệu đã chia chuẩn form YOLO
DEST_DIR = 'D:/Data_YOLO/my-data'

# Tỷ lệ chia (80% train, 20% val)
SPLIT_RATIO = 0.8

# --- 2. TẠO CẤU TRÚC THƯ MỤC YOLO ---
folders = ['train/images', 'train/labels', 'val/images', 'val/labels']
for folder in folders:
    os.makedirs(os.path.join(DEST_DIR, folder), exist_ok=True)

# --- 3. LẤY DANH SÁCH VÀ TRỘN NGẪU NHIÊN ---
# Lọc ra các file ảnh (hỗ trợ các đuôi phổ biến)
all_files = os.listdir(SOURCE_DIR)
image_files = [f for f in all_files if f.lower().endswith(('.png', '.jpg', '.jpeg'))]

# Trộn ngẫu nhiên danh sách để đảm bảo mô hình học đều các đặc trưng
random.seed(42) 
random.shuffle(image_files)

# --- 4. CHIA TỶ LỆ ---
split_index = int(len(image_files) * SPLIT_RATIO)
train_images = image_files[:split_index]
val_images = image_files[split_index:]

# --- 5. HÀM SAO CHÉP DỮ LIỆU ---
def copy_data(image_list, phase):
    for img_name in image_list:
        # Đường dẫn gốc
        src_img_path = os.path.join(SOURCE_DIR, img_name)
        
        # Đường dẫn đích cho ảnh
        dst_img_path = os.path.join(DEST_DIR, f'{phase}/images', img_name)
        
        # Tìm file label tương ứng (đổi đuôi ảnh thành .txt)
        label_name = os.path.splitext(img_name)[0] + '.txt'
        src_label_path = os.path.join(SOURCE_DIR, label_name)
        dst_label_path = os.path.join(DEST_DIR, f'{phase}/labels', label_name)

        # Copy ảnh
        shutil.copy(src_img_path, dst_img_path)
        
        # Copy label (nếu tồn tại file txt)
        if os.path.exists(src_label_path):
            shutil.copy(src_label_path, dst_label_path)
        else:
            print(f"Cảnh báo: Không tìm thấy file nhãn (.txt) cho ảnh {img_name}")

# --- 6. THỰC THI ---
print("Đang sao chép dữ liệu vào tập Train (80%)...")
copy_data(train_images, 'train')

print("Đang sao chép dữ liệu vào tập Val (20%)...")
copy_data(val_images, 'val')

print("-" * 30)
print("✅ HOÀN THÀNH!")
print(f"📁 Dữ liệu mới đã được phân loại chuẩn YOLO tại: {DEST_DIR}")
print(f"📊 Số lượng: Train có {len(train_images)} ảnh | Val có {len(val_images)} ảnh.")