#thanks to: https://heartbeat.fritz.ai/detecting-objects-in-videos-and-camera-feeds-using-keras-opencv-and-imageai-c869fe1ebcdb
from imageai.Detection import VideoObjectDetection
import os
import cv2

execution_path = os.getcwd()

detector = VideoObjectDetection()
detector.setModelTypeAsYOLOv3()
detector.setModelPath( os.path.join(execution_path , "models/yolo.h5"))
detector.loadModel()

camera = cv2.VideoCapture("http://http://riohomecloud.ddns.net:8081")

video_path = detector.detectObjectsFromVideo(input_file_path=os.path.join( execution_path, camera), frames_per_second=29, log_progress=True)