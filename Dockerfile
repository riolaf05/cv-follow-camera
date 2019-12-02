FROM rio05docker/tflite_rpi:rpi3_test_2

#Installing OpenCV and other pip packages
RUN pip3 install imutils argparse jupyter --user  
#RUN pip install pyarrow --user 
#RUN pip install python-opencv  --user #TODO: problem..unable to find python-opencv on Debian buster!

# Installing dependencies
RUN apt-get update \
&& apt-get install -y libatlas-base-dev \ 
&& apt-get install -y libjasper-dev \
&& apt-get install -y libqtgui4 \
&& apt-get install -y python3-pyqt5

# Miniconda installing
RUN wget http://repo.continuum.io/miniconda/Miniconda3-latest-Linux-armv7l.sh
RUN md5sum Miniconda3-latest-Linux-armv7l.sh
RUN bash Miniconda3-latest-Linux-armv7l.sh -b
RUN rm Miniconda3-latest-Linux-armv7l.sh

# Set path to conda
ENV PATH /root/anaconda3/bin:$PATH

# Updating Miniconda packages
RUN conda update conda -y
RUN conda update --all

# Configuring access to Jupyter
RUN mkdir /root/notebooks
RUN jupyter notebook --generate-config --allow-root
RUN echo "c.NotebookApp.password = u'sha1:6a3f528eec40:6e896b6e4828f525a6e20e5411cd1c8075d68619'" >> /root/.jupyter/jupyter_notebook_config.py

# Jupyter listens port: 8888
EXPOSE 8888

# Run Jupytewr notebook as Docker main process
CMD ["jupyter", "notebook", "--allow-root", "--notebook-dir=/home/ubuntu/notebooks", "--ip='*'", "--port=8888", "--no-browser"]
