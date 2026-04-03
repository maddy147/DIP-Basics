# Morphological Operations 
This project implements morphological opertaions such as dilation,erosion,opening and closing for binary image.

## Functions

### 1. `plus(ker_size)`

**Description:** Helper function to get structuring element with ones at middle of structuring element.

**Parameters:**
- `ker_size`: Size of structuring element as tuple.

**Returns:**
- `ker`: Structuring element as np.ndarray.

**Example:**
For `ker_size = (3,3)` the output will be `ker = [[0,1,0],[1,1,1],[0,1,0]]`

### 2. `DillateBinary(img,ker_size = (5,5),shape = None,iter = 1)`

**Description:** Function to dilate the given image.

**Parameters:**
- `img`: Image as np.ndarray
- `ker_size`: Size of structuring element as tuple.
- `shape`: Shape of sturcturing element, if set to "plus" the plus structuring element is used, otherwise structuring element with all ones is used.
- `iter`: Number of Iterations 

**Returns:**
- `dil`: Dilated image as np.ndarray.

### 3. `ErodeBinary(img,ker_size = (5,5),shape = None,iter = 1)`

**Description:** Function to erode the given image.

**Parameters:**
- `img`: Image as np.ndarray
- `ker_size`: Size of structuring element as tuple.
- `shape`: Shape of sturcturing element, if set to "plus" the plus structuring element is used, otherwise structuring element with all ones is used.
- `iter`: Number of Iterations 

**Returns:**
- `ero`: Eroded image as np.ndarray.

### 4. `OpenBinary(img,ker_size = (5,5),shape = None,iter = 1)`

**Description:** Function to perform opening of the given image.

**Parameters:**
- `img`: Image as np.ndarray
- `ker_size`: Size of structuring element as tuple.
- `shape`: Shape of sturcturing element, if set to "plus" the plus structuring element is used, otherwise structuring element with all ones is used.
- `iter`: Number of Iterations 

**Returns:**
- `ope`: Opened image as np.ndarray.

### 5. `CloseBinary(img,ker_size = (5,5),shape = None,iter = 1)`

**Description:** Function to perform closing of the given image.

**Parameters:**
- `img`: Image as np.ndarray
- `ker_size`: Size of structuring element as tuple.
- `shape`: Shape of sturcturing element, if set to "plus" the plus structuring element is used, otherwise structuring element with all ones is used.
- `iter`: Number of Iterations 

**Returns:**
- `cls`: Closed image as np.ndarray.

