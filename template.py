import os
from pathlib import Path

list_of_files = [
    ".env",
    "requirements.txt",
    "config.py", 
    "assistant.py", 
    "server.py", 
    "client.py",
    "audio/.keep",
    "memory/.keep",
    "utils/__init__.py",
    "utils/audio_utils.py",
    "utils/text_utils.py",
]

for filepath in list_of_files :
    path = Path(filepath)
    filedir , filename = os.path.split(path)

    if filedir != "":
        os.makedirs(filedir,exist_ok=True)

    if (not os.path.exists(path)) or (os.path.getsize(path)==0):
        with open(path, "w") as f :
            pass

    else :
        print(f"file allready exist at {path}")
