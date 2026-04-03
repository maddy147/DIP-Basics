# Histogram Equalisation and Histogram Matching
This project implements histogram equalisation and histogram matching for 8-bit Grayscale and RGB images.

## Functions

### 1. `hist_eq_help(img)`

**Description:** Helper function to equalize the given 8-bit image(must be single channel).

**Parameters:**
- `img`: A single channel of an 8-bit image as np.ndarray.

**Returns:**
- `new_vals`: Equalized levels as np.ndarray.

### 2. `rgb2ycbcr(img)`

**Description:** Helper function to convert the given 8-bit image from RGB to YCbCr color space.

**Parameters:**
- `img`: An 8-bit RGB image as np.ndarray.

**Returns:**
- `ycbcr`: YCbCr image as np.ndarray.

### 3. `ycbcr2rgb(img)`

**Description:** Helper function to convert the given 8-bit image from YCbCr to RGB color space.

**Parameters:**
- `img`: An 8-bit YCbCr image as np.ndarray.

**Returns:**
- `rgb`: RGB image as np.ndarray.

### 4. `hist_eq(img_path)`

**Description:** Function to equalize a given 8-bit RGB or grayscale image.

**Parameters:**
- `img_path`: Path to 8-bit grayscale or RGB image.

**Returns:**
- `eq_img`: Equalized image as np.ndarray.

### 5. `hist_mat(src_path,tar_path)`

**Description:** Function to match a histogram of a given 8-bit RGB or grayscale image with another 8-bit RGB or grayscale image.

**Parameters:**
- `src_path`: Path to 8-bit grayscale or RGB image, which needs to be matched.
- `tar_path`: Path to 8-bit grayscale or RGB image to match histogram of. Must have same number of channels as src_path image.

**Returns:**
- `matched_img`: Matched image as np.ndarray.

## Example Usage
```
eq_img = hist_eq("lena_color_512.jpg")
```
The above snippet displays the original image, equalized image and their respective histograms.

```
matched_img = hist_mat("lena_gray_512.jpg","mandril_gray.jpg")
```
The above snippet displays the original image, reference image, matched image and their respective histograms.