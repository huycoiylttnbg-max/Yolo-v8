import cv2
from ultralytics import YOLO

# 1. Nạp "bộ não" best.pt của bạn vào hệ thống
model = YOLO('best0.pt')

# 2. Mở Webcam (Số 0 là camera mặc định của laptop)
# Nếu bạn dùng camera cắm ngoài qua cổng USB, hãy thử đổi thành số 1 hoặc 2
cap = cv2.VideoCapture(1)

print("Đang khởi động Camera... Bấm phím 'q' trên cửa sổ cam để thoát.")

while cap.isOpened():
    # Đọc từng khung hình từ camera
    success, frame = cap.read()
    if not success:
        print("Không thể kết nối với camera!")
        break

    # 3. Cho YOLO quét qua khung hình để nhận diện
    # conf=0.5 nghĩa là nó phải chắc chắn trên 50% thì mới vẽ khung
    results = model(frame, conf=0.5)

    # 4. Vẽ khung vuông và tên nhãn trực tiếp lên bức ảnh
    annotated_frame = results[0].plot()

    # 5. Hiển thị kết quả lên màn hình
    cv2.imshow("He Thong Nhan Dien So - YOLOv8", annotated_frame)

    # Bấm phím 'q' trên bàn phím để thoát và tắt cam
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Dọn dẹp sau khi thoát
cap.release()
cv2.destroyAllWindows()