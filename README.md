# OpenCV Notes
My awesome notes about computer vision

## Description
This is the notes I took in my computer vision journey. Contents are from image basics and processing to object detection and tracking, even deep learning. 

## Contents
These notes consist of six topics. You can easily access all the content below.

### 1. Image Basics
* 1.1 [Numpy Basics](01-IMAGE-BASICS/1.1-numpy-basics.ipynb)
* 1.2 [OpenCV Basics](01-IMAGE-BASICS/1.2-opencv-basics.ipynb)
* 1.3 [Opening Images with OpenCV](01-IMAGE-BASICS/1.3-opening-images-with-opencv.py) 
* 1.4 [Drawing on Images](01-IMAGE-BASICS/05-drawing-on-images.ipynb) *(Draw a Circle, Rectangle, Line, Text and Polygon)*
* 1.5 [Drawing on Images with a Mouse](01-IMAGE-BASICS/06-drawing-on-images-with-a-mouse.py)

### 2. Image Processing
* 2.1 [Colorspaces](02-IMAGE-PROCESSING/07-colorspaces.ipynb) *(RGB, BGR, HSV, HSL)*
* 2.2 [Blending and Pasting Images](02-IMAGE-PROCESSING/08-blending-and-pasting-images.ipynb)
* 2.3 [Image Thresholding](02-IMAGE-PROCESSING/09-image-thresholding.ipynb)
* 2.4 [Blurring and Smoothing](02-IMAGE-PROCESSING/10-blurring-and-smoothing.ipynb)
* 2.5 [Morphological Operators](02-IMAGE-PROCESSING/11-morphological-operators.ipynb) 
* 2.6 [Gradients](02-IMAGE-PROCESSING/12-gradients.ipynb) *(Sobel, Laplacian)*
* 2.7 [Histograms](02-IMAGE-PROCESSING/13-histograms.ipynb)

### 3. Video Basics
* 3.1 [Connecting to Camera](03-VIDEO-BASICS/14-connecting-to-camera.py)
* 3.2 [Saving Video](03-VIDEO-BASICS/15-saving-video.py)
* 3.3 [Opening Video Files](03-VIDEO-BASICS/16-opening-video-files.py)
* 3.4 [Drawing on Video](03-VIDEO-BASICS/17-drawing-on-video.py)

### 4. Object Detection
* 4.1 [Template Matching](04-OBJECT-DETECTION/18-template-matching.ipynb)
* 4.2 [Corner Detection](04-OBJECT-DETECTION/19-corner-detection.ipynb) *(Harris, Shi-Tomasi)*
* 4.3 [Edge Detection](04-OBJECT-DETECTION/20-edge-detection.ipynb) *(Canny)*
* 4.4 [Grid Detection](04-OBJECT-DETECTION/21-grid-detection.ipynb) *(findChessboardCorners, findCirclesGrid)*
* 4.5 [Contour Detection](04-OBJECT-DETECTION/22-contour-detection.ipynb)
* 4.6 [Feature Matching](04-OBJECT-DETECTION/23-feature-matching.ipynb)
* 4.7 [Watershed Algorithm](04-OBJECT-DETECTION/24-watershed-algorithm.ipynb)
* 4.8 [Custom Seeds with Watershed Algorithm](04-OBJECT-DETECTION/25-custom-seeds-with-watershed-algorithm.py)
* 4.9 [Face Detection](04-OBJECT-DETECTION/26-face-detection.ipynb)

### 5. Object Tracking
* 5.1 [Lucas-Kanade Optical Flow](05-OBJECT-TRACKING/27-lucas-kanade-optical-flow.py)
* 5.2 [Dense Optical Flow](05-OBJECT-TRACKING/28-dense-optical-flow.py)
* 5.3 [MeanShift Tracking](05-OBJECT-TRACKING/29-meanshift-tracking.py)
* 5.4 [CAMShift Tracking](05-OBJECT-TRACKING/30-camshift-tracking.py)

### 6. Deep Learning
* 6.1 [Keras Basics](06-DEEP-LEARNING/31-keras-basics.ipynb)
* 6.2 [Keras CNN (MNIST)](06-DEEP-LEARNING/32-keras-cnn-mnist.ipynb)
* 6.3 [Working with Custom Images](06-DEEP-LEARNING/33-deep-learning-custom-images.ipynb)

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