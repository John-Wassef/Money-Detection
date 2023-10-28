import os
import cv2
from ultralytics import  YOLO


def DetectionOnImage(image_path):
    model_path = os.path.join('.', 'runs', 'detect', 'train', 'weights', 'best.pt')
    model = YOLO(model_path)
    img = cv2.imread(image_path)
    model.predict(source=img, show=True, conf=0.5)
    cv2.waitKey(0)


DetectionOnImage("C:/Users/John Wassef/OneDrive/Desktop/demo CV/data1/frame_0.jpg")