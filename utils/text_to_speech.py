from gtts import gTTS
import tempfile
import os

def text_to_audio(text, lang="de"):
    tts = gTTS(text=text, lang=lang)
    tmp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".mp3")
    tts.save(tmp_file.name)
    return tmp_file.name
    
