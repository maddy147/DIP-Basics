# Spatial Domain Filtering 
This project implements basic image processing spatial filters such as Mean, Median, Prewitt, Laplacian, Sobel kernels (horizontal, vertical, diagonal), Gaussian Blur,
Laplacian of Gaussian and their applications in edge detection and noise removal.

## Filter Functions

### 1. `mean_filter(img_path,filter_size = 3)`

**Description:** Function to compute mean filtered image

**Parameters:**
- `img_path`: Image path as string
- `filter_size`: Size of kernel(must be odd, default:3)   

**Returns:**
- `filtrd_img`: Filtered image as np.ndarray

### 2. `median_filter(img_path,filter_size = 3)`

**Description:** Function to compute median filtered image

**Parameters:**
- `img_path`: Image path as string
- `filter_size`: Size of kernel(must be odd, default:3)   

**Returns:**
- `filtrd_img`: Filtered image as np.ndarray

### 3. `perwitt_filter(img_path)`

**Description:** Function to compute filtered image using Perwitt Kernel(3x3)

**Parameters:**
- `img_path`: Image path as string

**Returns:**
- `filtrd_img`: Filtered image as np.ndarray

### 4. `laplacian_filter_4(img_path)`

**Description:** Function to compute filtered image using Laplacian Kernel(3x3)(4-Neighbour)

**Parameters:**
- `img_path`: Image path as string

**Returns:**
- `filtrd_img`: Filtered image as np.ndarray

### 5. `laplacian_filter_8(img_path)`

**Description:** Function to compute filtered image using Laplacian Kernel(3x3)(8-Neighbour)

**Parameters:**
- `img_path`: Image path as string

**Returns:**
- `filtrd_img`: Filtered image as np.ndarray

### 6. `sobel_filter(img_path)`

**Description:** Function to compute filtered image using Sobel Kernel(3x3) both horizontal and vertical

**Parameters:**
- `img_path`: Image path as string

**Returns:**
- `filtrd_img`: Filtered image as np.ndarray

### 7. `sobel_filter_h(img_path)`

**Description:** Function to compute filtered image using Sobel Kernel(3x3), only horizontal

**Parameters:**
- `img_path`: Image path as string

**Returns:**
- `filtrd_img`: Filtered image as np.ndarray

### 8. `sobel_filter_v(img_path)`

**Description:** Function to compute filtered image using Sobel Kernel(3x3), only vertical

**Parameters:**
- `img_path`: Image path as string

**Returns:**
- `filtrd_img`: Filtered image as np.ndarray

### 9. `sobel_filter_d(img_path)`

**Description:** Function to compute filtered image using Sobel Kernel(3x3),along diagonal

**Parameters:**
- `img_path`: Image path as string

**Returns:**
- `filtrd_img`: Filtered image as np.ndarray

### 10. `sobel_filter_ad(img_path)`

**Description:** Function to compute filtered image using Sobel Kernel(3x3),along anti-diagonal

**Parameters:**
- `img_path`: Image path as string

**Returns:**
- `filtrd_img`: Filtered image as np.ndarray

### 11. `gaussian_filter(img_path,filter_size = 3,sigma = None)`

**Description:** Function to compute filtered image using Gaussian Kernel

**Parameters:**
- `img_path`: Image path as string
- `filter_size`: Size of kernel(must be odd, default:3)
- `sigma`: Standard Deviation of the Gaussian kernel 

**Returns:**
- `filtrd_img`: Filtered image as np.ndarray

### 12. `lap_of_gauss_filter(img_path,filter_size = 3,sigma = None)`

**Description:** Function to compute filtered image using Laplacian of Gaussian Kernel

**Parameters:**
- `img_path`: Image path as string
- `filter_size`: Size of kernel(must be odd, default:3)
- `sigma`: Standard Deviation of the Gaussian kernel 

**Returns:**
- `filtrd_img`: Filtered image as np.ndarray

### 13. `gaussian_unblur(img_path,sigma)`

**Description:** Function to deblur a Gaussian blurred image 

**Parameters:**
- `img_path`: Original Unblurred Image path as string
- `sigma`: Standard Deviation of the Gaussian kernel 

**Returns:**
- `recon_img`: Reconstructed image as np.ndarray

## Helper Functions

### 1. `convolution2d(img, ker)`

**Description:** Function to compute 2-D Convolution of an image and a kernel 

**Parameters:**
- `img`: Image as np.ndarray
- `ker`: Kernel as np.ndarray

**Returns:**
- `new_img`: Convolved image as np.ndarray

### 2. `gen_gauss_kernel(ksize,sigma)`

**Description:** Function to compute Gaussian Kernel of given size and standard deviation

**Parameters:**
- `ksize`: Size of kernel(must be odd)
- `sigma`: Standard Deviation of the Gaussian distribution

**Returns:**
- `ker`: Gaussian kernel of given size and standard deviation

### 3. `gen_lap_of_gauss_kernel(ksize,sigma)`

**Description:** Function to compute Laplacian of Gaussian Kernel of given size and standard deviation

**Parameters:**
- `ksize`: Size of kernel(must be odd)
- `sigma`: Standard Deviation of the Gaussian distribution

**Returns:**
- `ker`: Laplacian of Gaussian Kernel of given size and standard deviation

### 4. `files(path)`

**Description:** Function to list all the files in a directory

**Parameters:**
- `path`: Path as string

**Returns:**
- A generator which can be converted to list of strings

### 5. `filter(img_path)`

**Description:** Function to compute all the filters implemented here

**Parameters:**
- `img_path`: Path as string

**Returns:**
- `fltrd_imgs`: Dictionary containng various filtered images with filter names as keys