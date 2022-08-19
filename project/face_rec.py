# from face_recognition.api import face_encodings
import face_recognition
import cv2
import os


class FaceRec:

    def __init__(self) -> None:
        self.known_encodings = []
        self.known_names = []
        self.known_dir = os.getcwd()+'\\project\\static\\project\\photos\\known'
        self.unknown_dir = os.getcwd()+'\\project\\static\\project\\photos\\unknown'
        self.createImageEnc()

    def read_img(self, path):
        img = cv2.imread(path)
        (h, w) = img.shape[:2]
        width = 500
        ratio = width / float(w)
        height = int(h * ratio)
        return cv2.resize(img, (width, height))

    def getImageEnc(self, img_path):
        img = self.read_img(img_path)
        img_enc = face_recognition.face_encodings(img)[0]
        return img_enc

    def createImageEnc(self):
        for file in os.listdir(self.known_dir):
            img_enc = self.getImageEnc(self.known_dir+'/'+file)
            self.known_encodings.append(img_enc)
            self.known_names.append(file.split('.')[0])
            print(self.known_encodings)
            print(self.known_names)

    def recongnizeImg(self, img):
        img_enc = self.getImageEnc(img)
        results = face_recognition.compare_faces(self.known_encodings, img_enc)
        for i in range(len(results)):
            if results[i]:
                return self.known_names[i]
