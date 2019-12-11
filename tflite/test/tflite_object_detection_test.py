import argparse
import io
import re
import time

from annotation import Annotator

import numpy as np
import picamera

from PIL import Image
from tflite_runtime.interpreter import Interpreter

CAMERA_WIDTH = 640
CAMERA_HEIGHT = 480

def load_labels(path):
  """Loads the labels file. Supports files with or without index numbers."""
  with open(path, 'r', encoding='utf-8') as f:
    lines = f.readlines()
    labels = {}
    for row_number, content in enumerate(lines):
      pair = re.split(r'[:\s]+', content.strip(), maxsplit=1)
      if len(pair) == 2 and pair[0].strip().isdigit():
        labels[int(pair[0])] = pair[1].strip()
      else:
        labels[row_number] = pair[0].strip()
  return labels


def set_input_tensor(interpreter, image):
  """Sets the input tensor."""
  tensor_index = interpreter.get_input_details()[0]['index']
  input_tensor = interpreter.tensor(tensor_index)()[0]
  input_tensor[:, :] = image


def get_output_tensor(interpreter, index):
  """Returns the output tensor at the given index."""
  output_details = interpreter.get_output_details()[index]
  tensor = np.squeeze(interpreter.get_tensor(output_details['index']))
  return tensor


def detect_objects(interpreter, image, threshold):
  """Returns a list of detection results, each a dictionary of object info."""
  set_input_tensor(interpreter, image)
  interpreter.invoke()
  # Get all output details
  boxes = get_output_tensor(interpreter, 0)
  classes = get_output_tensor(interpreter, 1)
  scores = get_output_tensor(interpreter, 2)
  count = int(get_output_tensor(interpreter, 3))
  results = []
  for i in range(count):
    if scores[i] >= threshold:
      result = {
          'bounding_box': boxes[i],
          'class_id': classes[i],
          'score': scores[i]
      }
      results.append(result)
  return results


def annotate_objects(annotator, results, labels):
  """Draws the bounding box and label for each object in the results."""
  for obj in results:
    # Convert the bounding box figures from relative coordinates
    # to absolute coordinates based on the original resolution
    ymin, xmin, ymax, xmax = obj['bounding_box']
    xmin = int(xmin * CAMERA_WIDTH)
    xmax = int(xmax * CAMERA_WIDTH)
    ymin = int(ymin * CAMERA_HEIGHT)
    ymax = int(ymax * CAMERA_HEIGHT)
    # Overlay the box, label, and score on the camera preview
    annotator.bounding_box([xmin, ymin, xmax, ymax])
    annotator.text([xmin, ymin], '%s\n%.2f' % (labels[obj['class_id']], obj['score']))

#def main():
  #parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
  #parser.add_argument('--model', help='File path of .tflite file.', required=True)
  #parser.add_argument('--labels', help='File path of labels file.', required=True)
  #parser.add_argument('--threshold', help='Score threshold for detected objects.', required=False, type=float, default=0.4)
  #args = parser.parse_args()

labels = load_labels("/home/scripts/models/labelmap.txt")
interpreter = Interpreter("/home/scripts/models/detect.tflite")
interpreter.allocate_tensors()
_, input_height, input_width, _ = interpreter.get_input_details()[0]['shape']


image = Image.open("/home/scripts/samples/cane_gatto.jpg")
image=image.convert('RGB').resize((input_height, input_height), Image.ANTIALIAS)
results = detect_objects(interpreter, image, 0.4)
print(labels[results[0]['class_id']])
for element in results:
  ymin, xmin, ymax, xmax = element['bounding_box']
  xmin = int(xmin * CAMERA_WIDTH)
  xmax = int(xmax * CAMERA_WIDTH)
  ymin = int(ymin * CAMERA_HEIGHT)
  ymax = int(ymax * CAMERA_HEIGHT)
  print("must move camera ", (xmin*100)/CAMERA_WIDTH, "% from left")

#if __name__ == '__main__':
 # main()