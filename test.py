import numpy as np
from PIL import Image
import cv2

dimensions = [(250, 122), (296, 128), (160, 160), (296, 152), (400, 300)]


def binarize_image(filename):
    img = cv2.imread(filename, 2)
    ret, bw_img = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
    # converting to its binary form
    bw = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
    cv2.imshow("Binary", bw_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def image_array(width, height, color, filename):
    if color == 'white':
        array_created = np.full((dimension[0], dimension[1], 3),
                                255, dtype=np.uint8)
    elif color == 'black':
        array_created = np.zeros([dimensions[0], dimension[1], 3], dtype=np.uint8)
    else:
        array_created = np.zeros([0, 0, 3], dtype=np.uint8)
        array_created[:, :] = [255, 0, 0]
    cv2.imwrite(filename, array_created)


for dimension in dimensions:
    image_array(*dimension, color='black', filename=f'uploads/black_{dimension[0]}_{dimension[1]}.png')
    image_array(*dimension, color='white', filename=f'uploads/white_{dimension[0]}_{dimension[1]}.png')
    image_array(*dimension, color='red', filename=f'uploads/red_{dimension[0]}_{dimension[1]}.png')
