# Image Experiments

These are small OpenCV experiments with images and webcam video.

- `color_channels_demo.py`: loads an image and produces copies with individual color channels zeroed out or maxed out.
- `webcam_filters.py`: a live webcam demo with a menu of filters, including default, black and white, face detection boxes, face blurring, and a scanning line effect.

`haarcascade_frontalface_default.xml` is OpenCV's standard, pretrained model for face detection, used by `webcam_filters.py`.

## Requirements
```
pip install opencv-python numpy
```

## Running it
```
python webcam_filters.py
```
`color_channels_demo.py` expects an image named `George.png` in this same folder. It isn't included in this archive, so add your own image (or point the script at a different one) before running it.
