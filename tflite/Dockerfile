FROM rio05docker/tflite_rpi:rpi3_test_4

#Install models and labels
COPY ./download.sh /home/scripts/models
RUN chmod +x /home/scripts/models/download.sh
RUN /home/scripts/models/download.sh

#Copy demo file
COPY ./tflite/pi_image_classifier_tflite_demo.py /home/scripts
