import cv2
import threading
import time
from object_detection import detect_objects
from voice_assistant import listen_for_command, speak
from gps_navigation import get_location, navigate_to
from emergency import emergency_call

def main():
    speak("Drishya Sahayak is now active")
    
    camera = cv2.VideoCapture(0)

    def detection_loop():
        while True:
            ret, frame = camera.read()
            if not ret:
                continue
            detect_objects(frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    threading.Thread(target=detection_loop, daemon=True).start()

    while True:
        command = listen_for_command()
        if command:
            if "where am i" in command:
                location = get_location()
                speak(location)
            elif "navigate to" in command:
                destination = command.replace("navigate to", "").strip()
                navigate_to(destination)
            elif "call for help" in command:
                emergency_call()
            elif "stop" in command:
                speak("Stopping Drishya Sahayak")
                break

    camera.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()

