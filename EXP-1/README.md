# Rotation and Scaling of Image
<!-- [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT) -->

## Requirements:
Python

Opencv

Numpy
## How to run:
Run the following command:

``
python main.py [path_to_img]
``
## Functions:
``transforms.py`` contains four functions which implements Scaling,Rotation using nearest neighbour,bilinear interpolation
- ``scale_nn(img,sf)`` -> Scaling with nearest neighbour interpolation
- ``scale_bl(img,sf)`` -> Scaling with bilinear interpolation
- ``rotate_nn(img,angle)`` -> Rotation with nearest neighbour interpolation
- ``rotate_bl(img,angle)`` -> Rotation with bilinear interpolation
### scale_nn(img,sf):
- Takes two arguments image``img:numpy.ndarray``, scaling factor ``sf:float`` and returns scaled image using nearest neighbour interpolation  ``numpy.ndarray``
- Note: Height and width are scaled by same factor
### scale_bl(img,sf):
- Takes two arguments image``img:numpy.ndarray``, scaling factor ``sf:float`` and returns scaled image using bilinear interpolation ``numpy.ndarray``
- Note: Height and width are scaled by same factor
### rotate_nn(img,sf):
- Takes two arguments image``img:numpy.ndarray``, angle(in degrees) ``angle:float`` and returns rotated image using nearest neighbour interpolation ``numpy.ndarray``
### rotate_bl(img,sf):
- Takes two arguments image``img:numpy.ndarray``, angle(in degrees) ``angle:float`` and returns rotated image using bilinear interpolation ``numpy.ndarray``
