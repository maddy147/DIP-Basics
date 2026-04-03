# 2D-FFT and 2D-IFFT Implementation
This project implements 2D-FFT and 2D-IFFT using python

## Functions

### 1. `FFT(x:np.ndarray)`

**Description:** Helper function to compute 1D-FFT 

**Parameters:**
- `x`: numpy.ndarray of length N, where N is power of 2

**Returns:**
- `X`: numpy.ndarray of length N, which is the DFT of `x` 

### 2. `IFFT(x:np.ndarray)`

**Description:** Helper function to compute 1D-IFFT 

**Parameters:**
- `x`: numpy.ndarray of length N, where N is power of 2

**Returns:**
- `X`: numpy.ndarray of length N, which is the IDFT of `x`

### 3. `FFT2d(img:np.ndarray,shift:bool = True)`

**Description:** Computes 2D-FFT of given N*N array where N is a power of 2, shift centers the FFT if set to true.

**Parameters:**
- `img`: numpy.ndarray of dimensions N*N, where N is power of 2
- `shift`: bool, centers the FFT spectrum when set to True

**Returns:**
- `fft`: numpy.ndarray of shape same as `img`, which is the 2D-DFT of `img` 

### 4. `IFFT2d(IMG:np.ndarray,shift:bool = True)`

**Description:** Computes 2D-IFFT of given N*N array where N is a power of 2, shift is true if FFT is centered.

**Parameters:**
- `IMG`: numpy.ndarray of dimensions N*N, where N is power of 2
- `shift`: bool, shift is True if FFT is centered

**Returns:**
- `ifft`: numpy.ndarray of shape same as `IMG`, which is the 2D-IDFT of `IMG` 

## Example usage
- `x = np.arange(16)`
- `fft = FFT(x)`
- `ifft = IFFT(x)`
- `img = np.arange(16).reshape(4,4)`
- `fft = FFT2d(img)`
- `ifft = IFFT2d(img)`