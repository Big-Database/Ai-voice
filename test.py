import torch
from TTS.api import TTS
import os
from pydub import AudioSegment


# Function to split text into 250-character chunks
def split_text(text, max_length=250):
    words = text.split()  # Split into words
    chunks = []
    current_chunk = ""

    for word in words:
        if len(current_chunk) + len(word) + 1 > max_length:
            chunks.append(current_chunk.strip())  # Save the current chunk
            current_chunk = word  # Start a new chunk
        else:
            current_chunk += " " + word

    if current_chunk:
        chunks.append(current_chunk.strip())  # Add the last chunk

    return chunks


def convert_TTS():
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


    text_chunks = split_text(text)

    # Print text chunks for debugging
    for i, chunk in enumerate(text_chunks):
        print(f"🔹 Chunk {i+1}: {chunk}\n")

    voice_sample = "speaker.wav"  
    language_code = "en"

    # Generate speech for each chunk and save as separate audio files
    for i, chunk in enumerate(text_chunks):
        output_file = f"output_chunk_{i+1}.wav"
        tts.tts_to_file(
            text=chunk,
            file_path=output_file,
            speaker_wav=voice_sample,
            language=language_code
        )
        print(f"✅ Speech synthesis complete for Chunk {i+1}! Saved as '{output_file}'.")

    combined_sounds = None

    for i, chunk in enumerate(text_chunks):
        file_name= f"output_chunk_{i+1}.wav"
        sound = AudioSegment.from_wav(file_name)
        combined_sounds = sound if combined_sounds is None else combined_sounds + sound
        # delete the file
        os.remove(file_name)
    
    #Export the combined audio
    combined_sounds.export("combined audio.wav", format="wav")
    


if __name__ == "__main__":
    convert_TTS()