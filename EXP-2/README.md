# BMP Image Read,Write and Manipualtion

This project implements various operations on BMP images such as read, write and channel manipulation in python.

## Functions

### 1. `read_bmp(file_path:str)`

**Description**: Reads a BMP image as byte string referred to by `file_path(str)` and returns `bmp_info:dict` containing BMP structure info.

**Parameters**:
- `file_path`: The file path to the BMP image.

**Returns**:
- A dcitionary containing BMP structure information. 

### 2. `write_bmp(file_path:str,bmp_info:dict)`

**Description**: Writes a BMP file with name `file_path:str`(must end with `.bmp`) given the BMP structure info(`bmp_info:dict`).

**Parameters**:
- `file_path`: The file path where the BMP image should be saved.
- `bmp_info`: Dictionary containing BMP structure information. 

### 3. `color_channel_manp(file_path:str,file_name:str)`

**Description**: Sets each channel of the BMP image to zero one at a time and writes as a BMP image each time.

**Parameters**:
- `file_path`: The file path to the BMP image.
- `file_name`: The file name to be saved

## Example Usage
- `bmp_corn = read_bmp("corn.bmp")`
- `write_bmp("wrt_corn.bmp",bmp_corn)`
- `color_channel_manp("corn.bmp","corn")`
