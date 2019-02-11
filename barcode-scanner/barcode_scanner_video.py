# USAGE
# python barcode_scanner_video.py

# import the necessary packages
from imutils.video import VideoStream
from pyzbar import pyzbar
import datetime
import imutils
import time
#import cv2

def readQR():
    # initialize the video stream and allow the camera sensor to warm up
    print("[INFO] skannataan...")
    vs = VideoStream(src=0).start()
    vs = VideoStream(usePiCamera=True).start()
    time.sleep(2.0)
    barcodeData = None
    i = 0

    # loop over the frames from the video stream
    while True:
        # grab the frame from the threaded video stream and resize it to
        # have a maximum width of 400 pixels
        frame = vs.read()
        frame = imutils.resize(frame, width=400)

        # find the barcodes in the frame and decode each of the barcodes
        barcodes = pyzbar.decode(frame)
        # loop over the detected barcodes
        for barcode in barcodes:
            barcodeData = barcode.data.decode("utf-8")
        i += 1
        if i > 55:
                    i = 0
                    print("ei loytyny koodia")
                    break
        if barcodeData is not None:
                    print(barcodeData)
                    break

    print("[INFO] cleaning up...")
    vs.stop()
    return barcodeData


