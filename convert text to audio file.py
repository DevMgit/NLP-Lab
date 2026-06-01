from gtts import gTTS

# Text to convert into speech
text = "Hello, this is generated using Google Text to Speech."

# Create gTTS object
tts = gTTS(text=text, lang='en')

# Save audio file
tts.save("gtts_output.mp3")

print("Audio saved!")
