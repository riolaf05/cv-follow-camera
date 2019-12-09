FROM rio05docker/tflite_rpi:rpi3_test_5

RUN mkdir /root/scripts

WORKDIR /root/scripts

#Update pip
RUN pip install --upgrade pip

#Install pip packages dependencies
RUN apt-get update \
&& apt-get install libjpeg-dev -y \
&& apt-get install zlib1g-dev -y \
&& apt-get install libfreetype6-dev -y \
&& apt-get install liblcms1-dev -y \
&& apt-get install libopenjp2-7 -y \
&& apt-get install libtiff5 -y \
&& apt-get install -y libraspberrypi0 libraspberrypi-dev libraspberrypi-doc libraspberrypi-bin

#Installing picamera and other pip packages
#RUN pip install numpy --user
RUN pip install imutils --user
RUN pip install argparse --user 
#RUN pip install Pillow --user  
RUN pip install picamera --user
#RUN apt install ipython -y
#RUN pip install pyarrow --user 
#RUN pip install python-opencv  --user #TODO: problem..unable to find python-opencv on Debian buster repositories!

#Copy demo file
COPY ./tflite/pi_image_classifier_tflite_demo.py /home/scripts


