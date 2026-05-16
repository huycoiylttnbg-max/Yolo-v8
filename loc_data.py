import os

def check_dataset_pairs(folder_path):
    # Các định dạng ảnh phổ biến (bạn có thể thêm nếu cần)
    image_extensions = {'.jpg', '.jpeg', '.png', '.bmp'}
    
    image_bases = set()
    text_bases = set()
    
    # 1. Đọc tất cả các file trong thư mục
    if not os.path.exists(folder_path):
        print("Đường dẫn thư mục không tồn tại!")
        return

    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        
        # Chỉ xử lý file, bỏ qua thư mục con
        if os.path.isfile(file_path):
            base_name, ext = os.path.splitext(filename)
            ext = ext.lower() # Chuyển đuôi về chữ thường để so sánh (VD: .JPG -> .jpg)
            
            if ext in image_extensions:
                image_bases.add(base_name)
            elif ext == '.txt':
                text_bases.add(base_name)
                
    # 2. Tìm ra các file bị "lẻ loi"
    images_without_texts = image_bases - text_bases
    texts_without_images = text_bases - image_bases
    
    # 3. In kết quả
    print(f"Đã quét tổng cộng: {len(image_bases)} file ảnh và {len(text_bases)} file text.\n")
    print("-" * 50)
    
    if not images_without_texts and not texts_without_images:
        print("✅ Tuyệt vời! Tất cả các file ảnh và text đều đã khớp với nhau 100%.")
    else:
        if images_without_texts:
            print(f"❌ CẢNH BÁO: Có {len(images_without_texts)} file ảnh không có file text (.txt) tương ứng:")
            for name in sorted(images_without_texts):
                print(f"   -> {name} (thiếu file text)")
                
        print() # Dòng trống
        
        if texts_without_images:
            print(f"❌ CẢNH BÁO: Có {len(texts_without_images)} file text không có ảnh tương ứng:")
            for name in sorted(texts_without_images):
                print(f"   -> {name}.txt (thiếu file ảnh)")

# ==========================================
# CÁCH SỬ DỤNG:
# Sửa đường dẫn bên dưới thành thư mục chứa data của bạn
# Lưu ý giữ nguyên chữ 'r' ở đầu chuỗi để tránh lỗi đường dẫn trong Windows
# ==========================================
folder_path = r"D:\Data_YOLO\dlib\DataDongHoTaiLieubosung" 

check_dataset_pairs(folder_path)