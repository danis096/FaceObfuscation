import cv2
import sys


def faceRec(photoRoute, scaleFactor, recognitionModel=None):
    # minimum size of the face
    # minSize=(30,30)
    validFormats = (".png", ".jpg")
    if photoRoute == "" or not photoRoute.endswith(validFormats):
        print("Image name is empty or didn't has a valid format")
        exit()
    if recognitionModel is None or not recognitionModel.endswith(".xml"):
        recognitionModel = "haarcascade_frontalface_default.xml"

    photo = cv2.imread(photoRoute)
    gray = cv2.cvtColor(photo, cv2.COLOR_BGR2GRAY)
    recface = cv2.CascadeClassifier(recognitionModel)
    faces = recface.detectMultiScale(gray, scaleFactor, minNeighbors=5, minSize=(30, 30))
    #print(faces)
    return faces


def drawFaces(faces):
    print("FACE'S COORDINATES: ", faces, "\n")
    print(type(faces))
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
    cv2.imshow('Original image', photo)
    cv2.imshow('Gray image', gray)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return 0


def facemain(phRoute, recPath=None):
    drawFaces(faceRec(phRoute, recPath))
    return exit()

# if len(sys.argv) == 3:
# print("el de 3")
# facemain(sys.argv[1], sys.argv[2])
# else:
# print("el de 2")
# facemain(sys.argv[1])
