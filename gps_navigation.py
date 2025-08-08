import requests
import pyttsx3
from geopy.geocoders import Nominatim

API_KEY = "YOUR_GOOGLE_MAPS_API_KEY"

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def get_location():
    try:
        response = requests.get("https://ipinfo.io/json")
        data = response.json()
        loc = data["loc"].split(",")
        geolocator = Nominatim(user_agent="drishya_sahayak")
        location = geolocator.reverse(f"{loc[0]}, {loc[1]}")
        return f"You are near {location.address}"
    except:
        return "Could not fetch location"

def navigate_to(destination):
    speak(f"Navigating to {destination}")
    url = f"https://www.google.com/maps/dir/?api=1&destination={destination}"
    import webbrowser
    webbrowser.open(url)
