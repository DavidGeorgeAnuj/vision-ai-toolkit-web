import cv2
import numpy as np

# Model paths (update these paths if needed)
DETECTOR_PROTO = "./deploy.prototxt"
DETECTOR_MODEL = "res10_300x300_ssd_iter_140000.caffemodel"
EMBEDDER_MODEL = "./openface.nn4.small2.v1.t7"

# Load models
face_detector = cv2.dnn.readNetFromCaffe(DETECTOR_PROTO, DETECTOR_MODEL)
embedder = cv2.dnn.readNetFromTorch(EMBEDDER_MODEL)

def get_face_embedding(image_path):
    image = cv2.imread(image_path)
    if image is None:
        return None
    (h, w) = image.shape[:2]
    resized = cv2.resize(image, (300, 300))
    blob = cv2.dnn.blobFromImage(resized, 1.0, (300, 300), (104.0, 177.0, 123.0))
    face_detector.setInput(blob)
    detections = face_detector.forward()

    if detections.shape[2] > 0:
        i = np.argmax(detections[0, 0, :, 2])
        confidence = detections[0, 0, i, 2]
        if confidence < 0.5:
            return None
        box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
        (startX, startY, endX, endY) = box.astype("int")
        face = image[startY:endY, startX:endX]
        if face.size == 0:
            return None
        face_blob = cv2.dnn.blobFromImage(face, 1.0/255, (96, 96), (0, 0, 0), swapRB=True, crop=False)
        embedder.setInput(face_blob)
        vec = embedder.forward()
        return vec.flatten()
    else:
        return None

def check_face_match(image_path1, image_path2, threshold=0.5):
    embedding1 = get_face_embedding(image_path1)
    embedding2 = get_face_embedding(image_path2)
    if embedding1 is None or embedding2 is None:
        return False
    similarity = np.dot(embedding1, embedding2) / (np.linalg.norm(embedding1) * np.linalg.norm(embedding2))
    return similarity > threshold
