
# Get TF Lite model and labels
wget http://storage.googleapis.com/download.tensorflow.org/models/tflite/coco_ssd_mobilenet_v1_1.0_quant_2018_06_29.zip
unzip coco_ssd_mobilenet_v1_1.0_quant_2018_06_29.zip -d /root/scripts/models
rm coco_ssd_mobilenet_v1_1.0_quant_2018_06_29.zip

# Get a labels file with corrected indices, delete the other one
(cd /root/scripts/models && wget https://dl.google.com/coral/canned_models/coco_labels.txt)
rm /root/scripts/models/labelmap.txt

# Get version compiled for Edge TPU
(cd /root/scripts/models && wget https://dl.google.com/coral/canned_models/mobilenet_ssd_v2_coco_quant_postprocess_edgetpu.tflite)

echo -e "Files downloaded to /root/scripts/models"