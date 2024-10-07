import cv2
import numpy as np
import os
import pytesseract


def extract_blue_text(image_path, output_path):
    images = [f for f in os.listdir(image_path) if f.endswith(('.png', '.jpg', '.jpeg'))]

    for image_name in images:
        image_path = os.path.join(image_path, image_name)

        image = cv2.imread(image_path)
        
        hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        
        lower_blue = np.array([70, 50, 10])
        upper_blue = np.array([140, 255, 255])
        
        mask = cv2.inRange(hsv, lower_blue, upper_blue)
        
        kernel = np.ones((3,3),np.uint8)
        mask = cv2.erode(mask, kernel, iterations = 1)
        mask = cv2.dilate(mask, kernel, iterations = 2)
        
        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        
        result = np.zeros_like(image)
        
        for contour in contours:
            area = cv2.contourArea(contour)
            if area > 100:
                x, y, w, h = cv2.boundingRect(contour)
                roi = image[y:y+h, x:x+w]
                result[y:y+h, x:x+w] = roi
    
        save_path = os.path.join(output_path, 'processed_' + image_name)
        cv2.imwrite(save_path, result)
        print('worked!')
        return result

# from pathlib import Path
# BASE_DIR = Path(__file__).resolve().parent.parent
# print('PATH IS ::', BASE_DIR)

# image_path = '/media'
# output_path = BASE_DIR
# extract_blue_text(image_path, output_path)