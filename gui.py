import tkinter as tk
from tkinter import messagebox, ttk
import threading
import speech_recognition as sr
import pyttsx3
import time

# === Voice Engine Setup ===
engine = pyttsx3.init()
def speak(text):
    engine.say(text)
    engine.runAndWait()

# === GUI Class ===
class BlindAidApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Drishya Sahayak - Blind Aid")
        self.root.geometry("500x500")
        self.root.resizable(False, False)

        self.setup_ui()

    def setup_ui(self):
        ttk.Label(self.root, text="Drishya Sahayak", font=("Helvetica", 20, "bold")).pack(pady=20)

        ttk.Button(self.root, text="Start Voice Assistant", command=self.start_voice_assistant).pack(pady=10)
        ttk.Button(self.root, text="Emergency Contact", command=self.emergency_contact).pack(pady=10)
        ttk.Button(self.root, text="Get Location Info", command=self.get_location).pack(pady=10)
        ttk.Button(self.root, text="Exit", command=self.root.quit).pack(pady=30)

        self.status_label = ttk.Label(self.root, text="Status: Idle", font=("Arial", 12))
        self.status_label.pack(pady=10)

    def update_status(self, text):
        self.status_label.config(text=f"Status: {text}")

    def start_voice_assistant(self):
        threading.Thread(target=self.voice_assistant).start()

    def voice_assistant(self):
        self.update_status("Listening...")
        r = sr.Recognizer()
        with sr.Microphone() as source:
            try:
                audio = r.listen(source, timeout=5)
                command = r.recognize_google(audio)
                self.update_status("Processing...")
                self.handle_command(command.lower())
            except sr.WaitTimeoutError:
                speak("I didn't hear anything. Please try again.")
            except sr.UnknownValueError:
                speak("Sorry, I didn't catch that.")
            except Exception as e:
                speak("An error occurred.")
                print(e)
        self.update_status("Idle")

    def handle_command(self, command):
        if "location" in command:
            self.get_location()
        elif "emergency" in command:
            self.emergency_contact()
        else:
            speak("Command not recognized.")

    def get_location(self):
        # Dummy GPS Info
        speak("You are currently near XYZ Street, ABC City.")
        messagebox.showinfo("Location", "Near XYZ Street, ABC City")

    def emergency_contact(self):
        speak("Calling your emergency contact.")
        messagebox.showwarning("Emergency", "Calling relative... If unanswered, calling 112")
        time.sleep(3)
        speak("No answer. Now calling 112 emergency services.")


# === Main ===
if __name__ == "__main__":
    root = tk.Tk()
    app = BlindAidApp(root)
    root.mainloop()
