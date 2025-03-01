import torch
from TTS.api import TTS

# Ensure MPS (Metal Performance Shaders) is used for acceleration on Apple Silicon
device = "cpu"

# List available 🐸TTS models (optional)
print(TTS().list_models())

# Initialize XTTS V2 Model
tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2").to(device)


# Read the text from a file safely
with open("text.txt", "r", encoding="utf-8") as file:
    text = file.read().strip()  # Strip leading/trailing spaces and newlines

# Handle Quotes & Special Characters (Optional Formatting)
text = text.replace('“', '"').replace('”', '"')  # Convert fancy quotes to standard
text = text.replace("‘", "'").replace("’", "'")  # Convert fancy single quotes

# Ensure text is not empty
if not text:
    raise ValueError("Error: The text file is empty!")

# Print text for debugging
print("🔹 Processed Text:\n", text)

# Provide a clear speaker sample (16kHz WAV file)
voice_sample = "speaker.wav"  # Ensure this file exists

# Specify the language code (e.g., 'en' for English)
language_code = "en"

# Generate speech with the specified language and speaker sample
tts.tts_to_file(
    text=text,
    file_path="output.wav",
    speaker_wav=voice_sample,
    language=language_code
)

print("✅ Speech synthesis complete! Check 'output.wav'.")

# Play the generated speech on macOS
import os
os.system("afplay output.wav")
