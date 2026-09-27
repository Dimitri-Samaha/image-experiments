# Image Experiments

Small OpenCV experiments with images and webcam video.

| File | What it does |
|---|---|
| `color_channels_demo.py` | Loads an image and produces copies with individual color channels zeroed out or maxed out |
| `webcam_filters.py` | Live webcam demo with a menu of filters: default, black & white, face detection boxes, face blurring, and a scanning-line effect |

`haarcascade_frontalface_default.xml` is OpenCV's standard pretrained face-detection model, used by `webcam_filters.py`.

## Requirements
```
pip install opencv-python numpy
```

## Running it
```
python webcam_filters.py
```
`color_channels_demo.py` expects an image named `George.png` in this same folder — it isn't included in this archive, so add your own image (or point the script at a different one) before running it.
