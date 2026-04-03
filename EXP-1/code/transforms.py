import numpy as np

def scale_nn(img:np.ndarray,sf:float) -> np.ndarray:
    '''
    Scales the given image by the scaling factor(sf) using Nearest Neighbour Interpolation
    img: np.ndarray,sf:float
    '''

    # Add channel dimension if image has shape (H,W) -> (H,W,1) 
    if( len(img.shape) == 2):
        img = np.expand_dims(img, axis = -1)

    # Create image with scaled dimensions
    scld_img = np.zeros((int(np.floor(img.shape[0]*sf)),int(np.floor(img.shape[1]*sf)),img.shape[2])).astype(np.uint8)

    # Iterate over the pixels and assign values to scaled image
    for i in range(scld_img.shape[0]):
        for j in range(scld_img.shape[1]):
            scld_img[i][j][:]= img[int(np.floor(i/sf))][int(np.floor(j/sf))][:]

    return scld_img

def scale_bl(img:np.ndarray,sf:float) -> np.ndarray:
    '''
    Scale the given image by the scaling factor(sf) using Bilinear Interpolation
    img: np.ndarray,sf:float
    '''

    # Add channel dimension if image has shape (H,W) -> (H,W,1)
    if( len(img.shape) == 2):
        img = np.expand_dims(img, axis = -1)

    # Create image with scaled dimensions
    scld_img = np.zeros((int(np.floor(img.shape[0]*sf)),int(np.floor(img.shape[1]*sf)),img.shape[2])).astype(np.uint8)

    # Iterate over the pixels and assign values to scaled image 
    for i in range(scld_img.shape[0]):
        for j in range(scld_img.shape[1]):
            x = i/sf
            y = j/sf

            # Calculate neighbouring pixels
            x_l = int(np.floor(x))
            x_r = int(min(img.shape[0] - 1,int(np.ceil(x))))
            y_l = int(np.floor(y))
            y_r = int(min(img.shape[1] - 1,int(np.ceil(y))))

            # If x,y are integers assign value to scaled image directly
            if(x_l == x_r  and y_l == y_r):
                p = img[int(x),int(y),:]
            # If x in an integer, interpolate using y 
            elif(x_l == x_r):
                p1 = img[int(x), int(y_l),:]
                p2 = img[int(x), int(y_r),:]
                p = p1 * (y_r - y) + p2 * (y - y_l)
            # If y in an integer, interpolate using x 
            elif(y_l == y_r):
                p1 = img[int(x_l), int(y),:]
                p2 = img[int(x_r), int(y),:]
                p = p1 * (x_r - x) + p2 * (x - x_l)
            # Interpolate using both x,y
            else:
                r1 = img[x_l, y_l,:]
                r2 = img[x_r, y_l,:]
                r3 = img[x_l, y_r,:]
                r4 = img[x_r, y_r,:]
                
                p1 = r1 * (x_r - x) + r2 * (x - x_l)
                p2 = r3 * (x_r - x) + r4 * (x - x_l)
                p = p1 * (y_r - y) + p2 * (y - y_l)
            
            scld_img[i,j,:] = p

    return scld_img

def rotate_nn(img:np.ndarray,angle:float) -> np.ndarray:
    '''
    Rotate the given image by a given angle(in deg) and 
    returns rotated image without cropping using nearest neighbour interpolation
    image: np.ndarray of dimensions (H,W,C) or (H,W) - Height, Width, Channel
    angle > 0 -> Anti-clockwise
    angle < 0 -> Clockwise 
    '''
    angle = (np.pi/180)*angle # Convert Deg to Rad

    # Calculating new dimensions of the image
    rot_img_h = int(np.round(np.abs(img.shape[0]*np.cos(angle))) + np.round(np.abs(img.shape[1]*np.sin(angle))))
    rot_img_w = int(np.round(np.abs(img.shape[1]*np.cos(angle))) + np.round(np.abs(img.shape[0]*np.sin(angle))))

    # Add channel dimension if image has shape (H,W) -> (H,W,1) 
    if( len(img.shape) == 2):
        img = np.expand_dims(img, axis = -1)

    # Center of original image 
    center_x, center_y = img.shape[0]//2,img.shape[1]//2

    # Center of rotated image
    center_rot_x,center_rot_y = rot_img_h//2, rot_img_w//2

    # Create image with modified shape
    rot_img = np.zeros((rot_img_h,rot_img_w,img.shape[2])).astype(np.uint8)

    # Iterate through the pixels and assign values
    for i in range(rot_img_h):
        for j in range(rot_img_w):
            # Rotating 
            x= (i-center_rot_x)*np.cos(angle)+(j-center_rot_y)*np.sin(angle)
            y= -(i-center_rot_x)*np.sin(angle)+(j-center_rot_y)*np.cos(angle)

            x=int(np.round(x))+center_y
            y=int(np.round(y))+center_x

            # Checking if x,y corresponds to valid pixel in original image
            if (x>=0 and y>=0 and x<img.shape[0] and  y<img.shape[1]):
                rot_img[i,j,:] = img[x,y,:]

    return rot_img

def rotate_bl(img:np.ndarray,angle:float) -> np.ndarray:
    '''
    Rotates the given image by a given angle(in deg) and 
    returns rotated image without cropping using Bilinear interpolation
    image: np.ndarray of dimensions (H,W,C) or (H,W) - Height, Width, Channel
    angle > 0 -> Anti-clockwise
    angle < 0 -> Clockwise
    '''
    angle = (np.pi/180)*angle # Convert Deg to Rad

    # Calculating new dimensions of the image
    rot_img_h = int(np.round(np.abs(img.shape[0]*np.cos(angle))) + np.round(np.abs(img.shape[1]*np.sin(angle))))
    rot_img_w = int(np.round(np.abs(img.shape[1]*np.cos(angle))) + np.round(np.abs(img.shape[0]*np.sin(angle))))

    # Add channel dimension if image has shape (H,W) -> (H,W,1) 
    if( len(img.shape) == 2):
        img = np.expand_dims(img, axis = -1)

    # Center of original image 
    center_x, center_y = img.shape[0]//2,img.shape[1]//2

    # Center of rotated image
    center_rot_x,center_rot_y = rot_img_h//2, rot_img_w//2

    # Create image with modified shape
    rot_img = np.zeros((rot_img_h,rot_img_w,img.shape[2])).astype(np.uint8)

    # Iterate through the pixels and assign values 
    for i in range(rot_img_h):
        for j in range(rot_img_w):
            # Mapping t
            x= (i-center_rot_x)*np.cos(angle)+(j-center_rot_y)*np.sin(angle)
            y= -(i-center_rot_x)*np.sin(angle)+(j-center_rot_y)*np.cos(angle)

            x=int(np.round(x))+center_y
            y=int(np.round(y))+center_x

            # Checking if x,y corresponds to valid pixel in original image
            if (x>=0 and y>=0 and x<img.shape[0] and  y<img.shape[1]):
                x_l = int(np.floor(x))
                x_r = int(min(img.shape[0] - 1,int(np.ceil(x))))
                y_l = int(np.floor(y))
                y_r = int(min(img.shape[1] - 1,int(np.ceil(y))))

                if(x_l == x_r  and y_l == y_r):
                    p = img[int(x),int(y),:]
                elif(x_l == x_r):
                    p1 = img[int(x), int(y_l),:]
                    p2 = img[int(x), int(y_r),:]
                    p = p1 * (y_r - y) + p2 * (y - y_l)
                elif(y_l == y_r):
                    p1 = img[int(x), int(y_l),:]
                    p2 = img[int(x), int(y_r),:]
                    p = p1 * (x_r - x) + p2 * (x - x_l)
                else:
                    r1 = img[x_l, y_l,:]
                    r2 = img[x_r, y_l,:]
                    r3 = img[x_l, y_r,:]
                    r4 = img[x_r, y_r,:]
                
                    p1 = r1 * (x_r - x) + r2 * (x - x_l)
                    p2 = r3 * (x_r - x) + r4 * (x - x_l)
                    p = p1 * (y_r - y) + p2 * (y - y_l)
                
                rot_img[i,j,:] = p

    return rot_img