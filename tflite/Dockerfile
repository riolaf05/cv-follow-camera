FROM raspbian/stretch:latest

#Workdir
RUN mkdir /home/scripts
WORKDIR /home/scripts
RUN mkdir /home/scripts/models

#Updating packet manager
RUN apt-get update

#Install Python3
RUN apt-get install -y build-essential tk-dev libncurses5-dev libncursesw5-dev libreadline6-dev libdb5.3-dev libgdbm-dev libsqlite3-dev libssl-dev libbz2-dev libexpat1-dev liblzma-dev zlib1g-dev
RUN wget https://www.python.org/ftp/python/3.6.5/Python-3.6.5.tar.xz \
&& tar xf Python-3.6.5.tar.xz \
&& cd Python-3.6.5 \
&& ./configure \
&& make \
&& make altinstall

#Cleaning python installation junk
RUN cd ..
RUN rm -r Python-3.6.5 
RUN rm Python-3.6.5.tar.xz 

#Install pip3
RUN apt-get install python3-pip -y

#Update pip3
RUN pip3 install --upgrade pip

#Tensorflow Lite installing
RUN wget 'https://dl.google.com/coral/python/tflite_runtime-1.14.0-cp35-cp35m-linux_armv7l.whl'
RUN pip3 install tflite_runtime-1.14.0-cp35-cp35m-linux_armv7l.whl
RUN rm tflite_runtime-1.14.0-cp35-cp35m-linux_armv7l.whl

#Install pip packages dependencies
RUN apt-get install libjpeg-dev -y \
&& apt-get install libjpeg-dev -y \
&& apt-get install libfreetype6-dev -y \
&& apt-get install liblcms1-dev -y \
&& apt-get install libopenjp2-7 -y \
&& apt-get install libtiff5 -y \
&& apt-get install -y libraspberrypi0 libraspberrypi-dev libraspberrypi-doc libraspberrypi-bin

#Installing picamera, jupyter and other pip packages
RUN pip3 install numpy --user
RUN pip3 install imutils --user
RUN pip3 install argparse --user 
RUN pip3 install Pillow --user  
RUN pip3 install picamera --user

#Cleaning pip packages junk
RUN apt-get --purge remove -y build-essential tk-dev
RUN apt-get --purge remove -y libncurses5-dev libncursesw5-dev libreadline6-dev
RUN apt-get --purge remove -y libdb5.3-dev libgdbm-dev libsqlite3-dev libssl-dev 
RUN apt-get --purge remove -y libbz2-dev libexpat1-dev liblzma-dev zlib1g-dev 
RUN apt-get autoremove -y 
RUN apt-get clean

#Install models and labels
RUN apt-get install -y zip
ADD http://storage.googleapis.com/download.tensorflow.org/models/tflite/coco_ssd_mobilenet_v1_1.0_quant_2018_06_29.zip /home/scripts/models
COPY ./download.sh /home/scripts/models
RUN chmod +x /home/scripts/models/download.sh
RUN bash /home/scripts/models/download.sh

#Copy demo file
COPY ./tflite_object_detection_demo.py /home/scripts
COPY ./annotation.py /home/scripts

#Copy test file
COPY ./test/tflite_object_detection_test.py /home/scripts