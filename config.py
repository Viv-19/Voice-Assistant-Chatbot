import os 
from dotenv import load_dotenv

load_dotenv()

class config :
    GROQ_API_KEY = os.getenv("GROQ_API_KEY")
    ASSEMBLYAI_API_KEY = os.getenv("ASSEMBLYAI_API_KEY")
    ELEVENLAB_API_KEY = os.getenv("ELEVENLAB_API_KEY")

    USE_FREE_STT = True
    USE_FREE_TTS = True

    # STT and TTS defaults
    STT_LANGUAGE = "en"         # Used for Whisper
    TTS_VOICE_ID = "Rachel"     # Default ElevenLabs voice