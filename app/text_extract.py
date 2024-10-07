import pytesseract

def text_extract(image):
    # custom_config = r'--oem 3 --psm 7'
    # text = pytesseract.image_to_string(image, config=custom_config)

    text = pytesseract.image_to_string(image)
    print('extracted text:', text)
    return text

# text_extract(image='/media/rushikeshmallanath/Additional/ML_assignment/blue_text_assignment/processed_Screenshot from 2024-10-05 17-54-36.png')