# Frequency Domain Filtering
This project implements basic image processing filters such as Ideal,Butterworth,Gaussian low and high pass filters in frequency domain and their applications in creating hybrid images and in denoising

## Filter Functions

### 1. `ideal_lpf(file_path:str,cut_off:float)`

**Description:** Function to compute ideal low pass filtered image

**Parameters:**
- `file_path`: Image path as string
- `cut_off`: Cut Off frequency 

**Returns:**
- `filtrd_img`: Filtered image as np.ndarray 

### 2. `ideal_hpf(file_path:str,cut_off:float)`

**Description:** Function to compute ideal high pass filtered image

**Parameters:**
- `file_path`: Image path as string
- `cut_off`: Cut Off frequency 

**Returns:**
- `filtrd_img`: Filtered image as np.ndarray 

### 3. `gaussian_lpf(file_path:str,cut_off:float)`

**Description:** Function to compute gaussian low pass filtered image

**Parameters:**
- `file_path`: Image path as string
- `cut_off`: Cut Off frequency 

**Returns:**
- `filtrd_img`: Filtered image as np.ndarray 

### 4. `gaussian_hpf(file_path:str,cut_off:float)`

**Description:** Function to compute gaussian high pass filtered image

**Parameters:**
- `file_path`: Image path as string
- `cut_off`: Cut Off frequency 

**Returns:**
- `filtrd_img`: Filtered image as np.ndarray 

### 5. `butterworth_lpf(file_path:str,cut_off:float,order:int = 2)`

**Description:** Function to compute butterworth low pass filtered image

**Parameters:**
- `file_path`: Image path as string
- `cut_off`: Cut Off frequency 
- `order`: Order of Butterworth Filter

**Returns:**
- `filtrd_img`: Filtered image as np.ndarray

### 6. `butterworth_hpf(file_path:str,cut_off:float,order:int = 2)`

**Description:** Function to compute butterworth high pass filtered image

**Parameters:**
- `file_path`: Image path as string
- `cut_off`: Cut Off frequency 
- `order`: Order of Butterworth Filter

**Returns:**
- `filtrd_img`: Filtered image as np.ndarray 

## Application Functions:

### 1. `create_hybrid_img(img_path1:str,img_path2:str,cut_off:float = 50)`

**Description:** Function to create a hybrid image combining the given two images

**Paramters** 
- `img_path1`: Path to image 1 filtered using High pass filter
- `img_path2`: Path to image 2 filtered using Low pass filter
- `cut_off`: Cut Off frequency

**Returns:**
- `hybd_img`: Hybrid image as np.ndarray 

### 2. `de_noise(file_path:str,threshold:float)`

**Description:** Function to remove sine periodic noise from a given noisy image

**Paramters**
- `file_path`: Path to input image
- `threshold`: Threshold for generating mask

**Returns:**
- `denoised_img`: Image with noise filtered depending upon threshold
 
## Example usage
- `fltrd_img = ideal_lpf("cameraman.jpg",10)`
- `fltrd_img = ideal_hpf("jetplane.jpg",20)`
- `fltrd_img = gaussian_lpf("lake.jpg",15)`
- `fltrd_img = gaussian_hpf("lena.jpg",25)`
- `fltrd_img = butterworth_lpf("livingroom.jpg",30,3)`
- `fltrd_img = butterworth_hpf("mandril.jpg",40,2)`
- `hybd_img = create_hybrid_img("einstein.png","marilyn.png",7.5)`
- `de_img = de_noise("cameraman_noisy1.jpg",11)`