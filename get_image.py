import os
from common import ADB_PATH, ANDROID_PORT

def get_image_from_app():

    # Take a screenshot of the app using ADB
    os.system(f"{ADB_PATH} shell screencap -p /sdcard/screenshot.png")
    os.system(f"{ADB_PATH} pull /sdcard/screenshot.png .")

    print("Get Screenshot successfully!")

    # image = Image.open('screenshot.png')
    # cropped_image = image.crop((550, 15 ,1250,80))  # left, top, right, bottom
    # cropped_image.save('screenshot.png')

    # Pre-process the image to improve OCR accuracy
    # process_image = cropped_image.convert('L')  # convert to grayscale
    # process_image = cropped_image.filter(ImageFilter.SHARPEN)  # sharpen the image
    # process_image = ImageEnhance.Contrast(cropped_image).enhance(3.0)  # increase contrast
    # process_image = cropped_image.filter(ImageFilter.MedianFilter())  # apply median filter to reduce noise

    # return process_image

