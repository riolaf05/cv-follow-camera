### Tensorflow Lite Object Detection on RaspberryPI (tflite_rpi4)

Dockerfile is based on Raspbian Stretch, it contains:

* Python3.5 (**only use Python3.5**)
* Tensorflow Lite 1.14
* Miniconda3
* Picamera and other Raspberry Pi tools

To cross compile Dockerfile (requieres Buildx binary): 

```console
~/.docker/cli-plugins/buildx-v0.3.1.linux-amd64 build --tag rio05docker/ai_obj_detection_camera:rpi3_test_1 --platform linux/arm/v7 --output "type=image,push=true" --file ~/Codice/cv-follow-camera/tflite/Dockerfile ~/Codice/cv-follow-camera/tflite/
```

To compile from RaspberryPi

```console
docker build -t "rio05docker/ai_obj_detection_camera:rpi3_test_1" .
docker push rio05docker/ai_obj_detection_camera:rpi3_test_1
```

To run with Raspberry Camera (assumes the camera appears as /dev/vidoe0 on the Raspberry Pi):

```console
docker run -it -d --restart unless-stopped --privileged --device /dev/vidoe0 --name pi_obj_detection rio05docker/tflite_rpi3_tpu:rpi3_test_4 python /home/scripts/tflite_object_detection.py
```

