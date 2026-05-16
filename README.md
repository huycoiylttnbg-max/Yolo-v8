#Ket noi drive
from google.colab import drive
drive.mount('/content/drive')


#Cai thu vien 
!pip install ultralytics
import ultralytics
ultralytics.checks()


#Train mo hinh
!yolo task=detect mode=train model=/content/drive/MyDrive/YOLOv8_Project/train_lan_3-2/weights/best.pt data=/content/drive/MyDrive/Dataset/data.yaml epochs=50 imgsz=640 project=/content/drive/MyDrive/YOLOv8_Project name=train_lan_4


#test bang video 
!yolo task=detect mode=predict model=/content/drive/MyDrive/YOLOv8_Project/train_lan_3-2/weights/best.pt source='/content/drive/MyDrive/7784140311314.mp4' save=True conf=0.3
