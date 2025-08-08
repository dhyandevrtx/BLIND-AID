import cv2
import pyttsx3

def detect_objects(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
        speak("Person ahead")
    cv2.imshow('Object Detection', frame)


def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

