import cv2
import numpy as np
import base64

def read_image_from_file(file):
    file_bytes = np.asarray(bytearray(file.read()), dtype=np.uint8)
    image = cv2.imdecode(file_bytes, cv2.IMREAD_GRAYSCALE)
    return image

def read_image_from_base64(base64_string):
    img_data = base64.b64decode(base64_string)
    image = np.frombuffer(img_data, np.uint8)
    image = cv2.imdecode(image, cv2.IMREAD_GRAYSCALE)
    return image

def stamp_matching(invoice_image_base64, stamp_type,result, threshold=0.8):
    print("checking stamp")
    try:
        stamp = cv2.imread(f'stamp_checker/stamps/{stamp_type}.jpg', 0)
    except:
        result[0]= False
        return

    invoice_image = read_image_from_base64(invoice_image_base64)
    stamp_height, stamp_width = stamp.shape
    result = cv2.matchTemplate(invoice_image, stamp, cv2.TM_CCOEFF_NORMED)
    locations = np.where(result >= threshold)

    if len(locations[0]) > 0:
        result[0]= True
        return
    else:
        result[0]= False
        return