import webbrowser
import pyttsx3
import time

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def emergency_call():
    speak("Initiating emergency contact")
    webbrowser.open("tel:+911234567890")  # Replace with your relative's number
    time.sleep(15)
    speak("No answer. Calling emergency services")
    webbrowser.open("tel:112")
