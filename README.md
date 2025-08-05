# BLIND-AID
👓 Blind Aid – AI-Powered Smart Glasses for the Visually Impaired
Blind Aid is an intelligent, AI-driven wearable system designed to assist visually impaired individuals in understanding their surroundings and navigating both indoor and outdoor environments with confidence. This innovation combines real-time computer vision, audio and haptic feedback, GPS-based navigation, and voice interaction – all packed into a lightweight and portable system powered by a Raspberry Pi 5. The primary objective of this project is to enhance the independence and safety of visually challenged individuals through accessible and affordable technology.

🧠 System Overview
The "brain" of the device is a Raspberry Pi 5, which is housed in a compact side bag worn by the user. This bag is connected to a pair of smart glasses that contain a camera module, microphone, and small speaker or earphone jack. All components are battery-powered and optimized for energy efficiency.

The system operates entirely offline, with no need for constant internet access (except for GPS/map initialization), and leverages AI models that run directly on the Raspberry Pi.

🔍 Key Features (In-Depth)
🧠 AI-Powered Object Detection
Uses a camera mounted on the eyeglasses to capture live video.

Processes each frame in real-time using computer vision models (TensorFlow Lite or YOLO on edge).

Detects and identifies common obstacles like:

People

Vehicles

Poles

Walls

Stairs (up/down)

Doors

Detected objects are interpreted contextually to give smart feedback about danger or navigation suggestions.

🔊 Real-Time Voice Alerts
Converts detection results into spoken voice alerts using text-to-speech (TTS).

Audio is played via a speaker or headphones connected to the system.

Examples:

“Stairs ahead on the left”

“Pole in front. Step aside”

“Empty path. You’re clear”

🗺️ GPS Navigation with Google Maps API
Outdoor navigation feature using GPS module and Google Maps API.

Offers turn-by-turn audio guidance when the user sets a destination via voice.

Supports common phrases like:

“Navigate to railway station”

“Guide me to school”

Handles rerouting if the user changes direction or misses a turn.

📳 Directional Vibration Feedback
Vibration motors placed on left and right side of the frame or wristband.

Alerts the user with silent cues:

Left or right vibration = direction change

Both sides = obstacle ahead

Stronger vibration = closer distance

Useful in crowded or noisy environments where voice alerts might be missed.

🎙️ Voice Assistant
Activated via wake word (e.g., "Hello Aid").

Accepts a limited set of offline voice commands for interaction.

Example commands:

“What’s ahead?”

“How far to destination?”

“Battery status”

“Start navigation to market”

The assistant improves usability without requiring buttons or screens.

🔋 Power & Portability
Fully powered by a rechargeable battery system (can be power bank or lithium battery).

Designed to last 6–8 hours on a single charge.

Compact, lightweight, and wearable design – discreet enough to be used comfortably in public.

🛠️ Tech Stack
Component	Tool/Tech Used
Core Processing Unit	Raspberry Pi 5
Programming Language	Python
Object Detection	TensorFlow Lite / OpenCV
Voice Alerts	pyttsx3 or gTTS + VLC/omxplayer
Voice Commands	Vosk or Picovoice for offline ASR
GPS Navigation	Google Maps API + GPS Module
Vibration Feedback	PWM + Vibration motors
Power Supply	5V Rechargeable Battery/Power Bank

🎯 Goal & Vision
This project aims to empower the blind and visually impaired with technology that helps them:

Walk safely in unfamiliar places

Detect obstacles and avoid accidents

Receive directions to a destination

Interact with the system using just their voice

Maintain independence and dignity

