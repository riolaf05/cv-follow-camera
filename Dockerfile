FROM rio05docker/tflite_rpi:rpi3_test_2

RUN pip install imutils argparse python-opencv --user 

RUN apt-get install -y libatlas-base-dev \ 
apt-get install -y libjasper-dev \
apt-get install -y libqtgui4 \
apt-get install -y python3-pyqt5


pip install pyarrow --user \
&& pip install numpy --user \ 
&& pip install imutils --user \
&& pip install python-opencv --user \
&& pip install argparse --user \ 
&& sudo apt-get install -y libatlas-base-dev \
&& sudo apt-get install -y libjasper-dev \
&& sudo apt-get install -y libqtgui4 \
&& sudo apt-get install -y python3-pyqt5