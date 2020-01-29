### rpi3_rt_tflite_tpu

Object detection inference with Edge TPU

Based on Raspbian Stretch, it contains:

* Python 3.5.3
* Tensorflow Lite
* Picamera module
* Edge TPU runtime

It must run on RaspberryPi with Edge TPU Coral device

Use CI/CD pipeline to build.

To run with Raspberry Camera and Edge TPU usb device:

```console
docker run -it --rm --privileged -p 8000:8000 -v /dev/bus/usb:/dev/bus/usb --device=/dev/vchiq --rm rio05docker/ai_obj_detection_camera:rpi3_rt_tflite_tpu_${GITHUB_SHA}
```

Then exec the container and run: 

```console
python3 demo_real_time_obj_detection_server.py --model /tmp/mobilenet_ssd_v2_coco_quant_postprocess_edgetpu.tflite --label /tmp/coco_labels.txt
```

Then log in on: `http://<<rpi3_ip>>:8000`

### TODO: 
* ~~Test real time predictions~~
* Add CI/CD for batch edge TPU
* ~~Add transfer learning with Edge TPU API~~
* (maybe?) Add MLFlow logging and packaging
