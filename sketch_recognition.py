import cv2
import numpy as np

class SketchRecognizer:
    def predict(self, img):
        if hasattr(img, "convert"):
            img = np.array(img.convert("L"))

        _, thresh = cv2.threshold(img, 200, 255, cv2.THRESH_BINARY_INV)
        contours, _ = cv2.findContours(
            thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
        )

        if not contours:
            return "No Sketch", 0.0

        cnt = max(contours, key=cv2.contourArea)
        peri = cv2.arcLength(cnt, True)
        approx = cv2.approxPolyDP(cnt, 0.04 * peri, True)

        if len(approx) == 3:
            return "Triangle", 0.85
        elif len(approx) == 4:
            return "Rectangle", 0.80
        elif len(approx) > 6:
            return "Circle", 0.90
        else:
            return "Unknown Shape", 0.50
