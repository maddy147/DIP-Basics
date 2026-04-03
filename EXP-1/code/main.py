import cv2
from transforms import *

def main(path):
    img = cv2.imread(path)
    print("Choose transformation(Enter number)")
    print("1.Scale Image using Nearest Neighbour")
    print("2.Scale Image using Bilinear Interpolation")
    print("3.Rotate Image using Nearest Neighbour")
    print("4.Rotate Image using Bilinear Interpolation")
    ch = int(input())
    if(ch == 1):
        sf = float(input("Enter Scaling factor(sf) "))
        tfrm_img = scale_nn(img,sf)
        cv2.imwrite("Scaled_NN.png",tfrm_img)
        cv2.imshow("Scaled NN",tfrm_img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    elif(ch == 2):
        sf = float(input("Enter Scaling factor(sf) "))
        tfrm_img = scale_bl(img,sf)
        cv2.imwrite("Scaled_BL.png",tfrm_img)
        cv2.imshow("Scaled BL",tfrm_img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    elif(ch == 3):
        ang = float(input("Enter Angle(in deg) "))
        tfrm_img = rotate_nn(img,ang)
        cv2.imwrite("Rotated_NN.png",tfrm_img)
        cv2.imshow("Rotated NN",tfrm_img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    elif(ch == 4):
        ang = float(input("Enter Angle(in deg) "))
        tfrm_img = rotate_bl(img,ang)
        cv2.imwrite("Rotated_BL.png",tfrm_img)
        cv2.imshow("Rotated BL",tfrm_img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    else:
        print("Invlaid Choice ")


if(__name__  == "__main__"):
    import argparse
    parser = argparse.ArgumentParser(description ='Image Transformations')
    parser.add_argument('path_to_img',type=str,help="Path to Image")
    args = parser.parse_args()

    main(args.path_to_img)