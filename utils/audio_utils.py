import os
import soundfile as sf
import speech_recognition as sr

from pydub import AudioSegment
from pydub.playback import play

# ✅ Hardcoded path to ffmpeg.exe
# ⚠️ Replace this with your actual path if different
AudioSegment.converter = r"C:\ffmpeg\bin\ffmpeg.exe"

AUDIO_INPUT_PATH = "audio/input.wav"
AUDIO_OUTPUT_PATH = "audio/output.wav"

def record_audio(duration=5, sample_rate=16000):
    """Records audio from the microphone and saves it to a file."""
    recognizer = sr.Recognizer()
    with sr.Microphone(sample_rate=sample_rate) as source:
        print("🎙️ Listening... Speak now.")
        audio_data = recognizer.record(source, duration=duration)
        with open(AUDIO_INPUT_PATH, "wb") as f:
            f.write(audio_data.get_wav_data())
    return AUDIO_INPUT_PATH

def play_audio(file_path: str = AUDIO_OUTPUT_PATH):
    """Plays back the given audio file."""
    if not os.path.exists(file_path):
        print(f"❌ Audio file not found: {file_path}")
        return
    audio = AudioSegment.from_file(file_path, format="wav")
    play(audio)

def convert_audio_to_wav(input_path: str, output_path: str):
    """Converts mp3/m4a to wav (if needed)."""
    audio = AudioSegment.from_file(input_path)
    audio.export(output_path, format="wav")
    return output_path
