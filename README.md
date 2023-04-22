# OpenCV Notes
My awesome notes about computer vision

## Description
This is the notes I took in my computer vision journey. Contents are from image basics and processing to object detection and tracking, even deep learning. 

## Contents
These notes consist of six topics. You can easily access all the content below.

### 1. Image Basics
* 1.1 [Numpy Basics](01-IMAGE-BASICS/1.1-numpy-basics.ipynb) *np.array, np.zeros, np.ones, np.arange, np.linspace, np.random.randint, np.reshape*
* 1.2 [OpenCV Basics](01-IMAGE-BASICS/1.2-opencv-basics.ipynb) *cv2.imread, cv2.cvtColor, cv2.resize, cv2.flip, cv2.rotate, cv2.imwrite*
* 1.3 [Opening Images with OpenCV](01-IMAGE-BASICS/1.3-opening-images-with-opencv.py) 
* 1.4 [Drawing on Images](01-IMAGE-BASICS/1.4-drawing-on-images.ipynb) *cv2.rectangle, cv2.circle, cv2.line, cv2.putText, cv2.polylines*
* 1.5 [Drawing on Images with a Mouse](01-IMAGE-BASICS/1.5-drawing-on-images-with-a-mouse.py)

### 2. Image Processing
* 2.1 [Colorspaces](02-IMAGE-PROCESSING/2.1-colorspaces.ipynb)
* 2.2 [Blending and Pasting Images](02-IMAGE-PROCESSING/2.2-blending-and-pasting-images.ipynb)
* 2.3 [Image Thresholding](02-IMAGE-PROCESSING/2.3-image-thresholding.ipynb)
* 2.4 [Image Blurring](02-IMAGE-PROCESSING/2.4-image-blurring.ipynb)
* 2.5 [Morphological Operators](02-IMAGE-PROCESSING/2.5-morphological-operators.ipynb) 
* 2.6 [Gradients](02-IMAGE-PROCESSING/2.6-gradients.ipynb)
* 2.7 [Histograms](02-IMAGE-PROCESSING/2.7-histograms.ipynb)
* 2.8 [Transformations](02-IMAGE-PROCESSING/2.8-transformations.ipynb) *cv2.getAffineTransform, cv2.warpAffine, cv2.getPerspectiveTransform, cv2.warpPerspective*

### 3. Video Basics
* 3.1 [Connecting to Camera](03-VIDEO-BASICS/3.1-connecting-to-camera.py)
* 3.2 [Saving Video](03-VIDEO-BASICS/3.2-saving-video.py)
* 3.3 [Opening Video Files](03-VIDEO-BASICS/3.3-opening-video-files.py)
* 3.4 [Drawing on Video](03-VIDEO-BASICS/3.4-drawing-on-video.py)

### 4. Object Detection
* 4.1 [Template Matching](04-OBJECT-DETECTION/4.1-template-matching.ipynb)
* 4.2 [Corner Detection](04-OBJECT-DETECTION/4.2-corner-detection.ipynb)
* 4.3 [Edge Detection](04-OBJECT-DETECTION/4.3-edge-detection.ipynb)
* 4.4 [Grid Detection](04-OBJECT-DETECTION/4.4-grid-detection.ipynb)
* 4.5 [Contour Detection](04-OBJECT-DETECTION/4.5-contour-detection.ipynb)
* 4.6 [Feature Matching](04-OBJECT-DETECTION/4.6-feature-matching.ipynb)
* 4.7 [Watershed Algorithm](04-OBJECT-DETECTION/4.7-watershed-algorithm.ipynb)
* 4.8 [Custom Seeds with Watershed Algorithm](04-OBJECT-DETECTION/4.8-custom-seeds-with-watershed-algorithm.py)
* 4.9 [Face Detection](04-OBJECT-DETECTION/4.9-face-detection.ipynb)

### 5. Object Tracking
* 5.1 [Lucas-Kanade Optical Flow](05-OBJECT-TRACKING/5.1-lucas-kanade-optical-flow.py)
* 5.2 [Dense Optical Flow](05-OBJECT-TRACKING/5.2-dense-optical-flow.py)
* 5.3 [MeanShift Tracking](05-OBJECT-TRACKING/5.3-meanshift-tracking.py)
* 5.4 [CAMShift Tracking](05-OBJECT-TRACKING/5.4-camshift-tracking.py)

### 6. Deep Learning
* 6.1 [Keras Basics](06-DEEP-LEARNING/6.1-keras-basics.ipynb)
* 6.2 [Keras CNN (MNIST)](06-DEEP-LEARNING/6.2-keras-cnn-mnist.ipynb)
* 6.3 [Working with Custom Images](06-DEEP-LEARNING/6.3-deep-learning-custom-images.ipynb)

## Installation
In order to play around with the notes, you can set up this repository locally following these simple steps.

Note that in order to avoid potential conflicts with other packages, it is strongly recommended to use a virtual environment or a conda environment.

### Install using pip
1. Clone the repo
    ```sh
    git clone https://github.com/hasan-alper/opencv-notes.git
    ```
2. Move inside your copy
    ```sh
    cd opencv-notes
    ```
3. Create a virtual environment
    ```sh
    virtualenv [my_virtual_env_name]
    ```
4. Active the virtual environment
    ```sh
    source [my_virtual_env_name]/bin/activate
    ```
5. Install necessary packages
    ```sh
    pip install -r requirements.txt
    ```

### Install using conda

1. Clone the repo
    ```sh
    git clone https://github.com/hasan-alper/opencv-notes.git
    ```
2. Move inside your copy
    ```sh
    cd opencv-notes
    ```
3. Create a conda environment
    ```sh
    conda create --name [my_conda_env_name]
    ```
4. Active the conda environment
    ```sh
    conda activate [my_conda_env_name]
    ```
5. Install necessary packages
    ```sh
    pip install -r requirements.txt
    ```
     ⚠️ For Apple silicon Macs, you must follow these steps instead:
    ```sh
    conda install -c apple tensorflow-deps
    ```
    ```sh
    pip install -r requirements-apple-silicon.txt
    ```
     
## Contributing

Any contributions are greatly appreciated. Feel free to create a pull request to improve one or two things. You can also simply open an issue.

## License

Distributed under the MIT License. See [LICENSE](LICENSE) for more information.