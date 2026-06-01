import speech_recognition as sr
import nltk

# Initialize recognizer
recognizer = sr.Recognizer()

# Load audio file
with sr.AudioFile("Sports.wav") as source:
    print("Listening...")
    audio_data = recognizer.record(source)

# Convert speech to text
try:
    text = recognizer.recognize_google(audio_data)
    print("Recognized Text:", text)

except sr.UnknownValueError:
    print("Could not understand audio")

except sr.RequestError:
    print("API unavailable")
