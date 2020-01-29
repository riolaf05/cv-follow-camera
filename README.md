# cv-follow-camera
This is a Tensorflow based object detection container which can be used to drive a RaspberyyPi-powered servo motor to point a selected object. 

This repo contains a continuous integration pipeline which automatically build the container.

## Install with Docker and Coral Edge TPU

Follow the instructions on tflite_edge_tpu folder.

## Install with Docker 
TODO

### Dependencies

```console
apt-get install python-opencv \
&& apt-get install python-scipy \
&& apt-get install ipython \
&& apt install libqt4-test
&& apt-get install -y libatlas-base-dev \
&& apt-get install -y libjasper-dev \
&& apt-get install -y libqtgui4 \
&& apt-get install -y python3-pyqt5
```

```console
pip install pyarrow --user \
&& pip install numpy --user \ 
&& pip install imutils --user \
&& pip install python-opencv --user \
&& pip install argparse --user \ 
```
