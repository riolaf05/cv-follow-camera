FROM rio05docker/tflite_rpi:rpi3_test_4.1

#Install models and labels
RUN apt-get install zip
ADD http://storage.googleapis.com/download.tensorflow.org/models/tflite/coco_ssd_mobilenet_v1_1.0_quant_2018_06_29.zip /home/scripts/models
COPY ./download.sh /home/scripts/models
RUN chmod +x /home/scripts/models/download.sh
RUN bash /home/scripts/models/download.sh

#Copy demo file
COPY ./tflite_object_detection.py /home/scripts
