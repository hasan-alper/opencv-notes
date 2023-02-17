# OpenCV Notes
My awesome notes about computer vision

## Description
This is the notes I took in my computer vision journey. Contents are from image basics and processing to object detection and tracking, even deep learning. 

## Contents
These notes consist of six topics. You can easily access all the content below.

### 1. Image Basics
* 1.1 [Numpy Basics](01-numpy-basics.ipynb) *(Creating Arrays, Indexing)*
* 1.2 [Numpy and Images](02-numpy-and-images.ipynb) *(PIL)*
* 1.3 [Image Basics](03-image-basics.ipynb) *(Resizing, Flipping and Saving Images)*
* 1.4 [Opening Images with OpenCV](04-opening-images-with-opencv.py) 
* 1.5 [Drawing on Images](05-drawing-on-images.ipynb) *(Draw a Circle, Rectangle, Line, Text and Polygon)*
* 1.6 [Drawing on Images with a Mouse](06-drawing-on-images-with-a-mouse.py)

### 2. Image Processing
* 2.1 [Colorspaces](07-colorspaces.ipynb) *(RGB, BGR, HSV, HSL)*
* 2.2 [Blending and Pasting Images](08-blending-and-pasting-images.ipynb)
* 2.3 [Image Thresholding](09-image-thresholding.ipynb)
* 2.4 [Blurring and Smoothing](10-blurring-and-smoothing.ipynb)
* 2.5 [Morphological Operators](11-morphological-operators.ipynb) *(Erosion, Opening, Closing and Gradient)*
* 2.6 [Gradients](12-gradients.ipynb) *(Sobel, Laplacian)*
* 2.7 [Histograms](13-histograms.ipynb)

### 3. Video Basics
* 3.1 [Connecting to Camera](14-connecting-to-camera.py)
* 3.2 [Saving Video](15-saving-video.py)
* 3.3 [Opening Video Files](16-opening-video-files.py)
* 3.4 [Drawing on Video](17-drawing-on-video.py)

## Play Around
In order to play around with the notes, you can set up this repository locally following these simple steps.

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

     
## Contributing

Any contributions are greatly appreciated. Feel free to create a pull request to improve one or two things. You can also simply open an issue.

## License

Distributed under the MIT License. See [LICENSE](LICENSE) for more information.