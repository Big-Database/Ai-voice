# AI Voice Cloning & Text-to-Speech (macOS, XTTS v2)

A local, CPU-only **AI text-to-speech and voice cloning pipeline** for macOS using the **XTTS v2 multilingual model** from 🐸 Coqui TTS. The system converts long-form text into natural speech by chunking input text, generating audio per segment, and merging the results into a single output file.

---

## Features
- Voice cloning from a short reference sample (`speaker.wav`)
- Long-text support via automatic chunking
- Fully local execution (no external APIs)
- CPU-only (works on Macs without GPUs)
- Deterministic audio merging into a single WAV file

---

## How It Works
1. Reads text from `text.txt`
2. Normalizes special characters
3. Splits text into ~250-character chunks
4. Synthesizes speech per chunk using XTTS v2
5. Concatenates audio into one output file

---

## Usage

Place input text in text.txt

Add a reference voice clip as speaker.wav

Run:
python tests.py


Output is saved as:
combined_audio.wav
