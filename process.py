import cv2
import pytesseract

def object_recognition(image_path):
    # Placeholder function - Replace with actual logic
    return "Detected Objects: Car, Person"

def text_recognition(image_path):
    img = cv2.imread(image_path)
    text = pytesseract.image_to_string(img)
    return text

def face_recognition(image_path):
    # Placeholder function - Replace with actual logic
    return "Face detected: John Doe"
