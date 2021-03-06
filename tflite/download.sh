# Get TF Lite model and labels
#wget http://storage.googleapis.com/download.tensorflow.org/models/tflite/coco_ssd_mobilenet_v1_1.0_quant_2018_06_29.zip -P /home/scripts/models
unzip /home/scripts/models/coco_ssd_mobilenet_v1_1.0_quant_2018_06_29.zip -d /home/scripts/models
rm /home/scripts/models/coco_ssd_mobilenet_v1_1.0_quant_2018_06_29.zip

# Get a labels file with corrected indices, delete the other one
(cd /home/scripts/models && wget https://dl.google.com/coral/canned_models/coco_labels.txt)
rm /home/scripts/models/labelmap.txt

# Get version compiled for Edge TPU
(cd /home/scripts/models && wget https://dl.google.com/coral/canned_models/mobilenet_ssd_v2_coco_quant_postprocess_edgetpu.tflite)

echo -e "Files downloaded to /home/scripts/models"