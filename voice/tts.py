import os
import time
from gtts import gTTS
from pathlib import Path
import wave
import pyaudio

class TextToSpeech:
    def __init__(self):
        self.output_dir = Path("audio_output")
        self.output_dir.mkdir(exist_ok=True, parents=True)
        self.audio = pyaudio.PyAudio()
        
    async def synthesize_speech(self, text: str) -> str:
        """Convert text to speech using Google Text-to-Speech."""
        try:
            # Generate unique filename using timestamp
            timestamp = int(time.time())
            audio_path = self.output_dir / f"response_{timestamp}.mp3"
            
            # Create gTTS object and save to file
            tts = gTTS(text=text, lang='en', slow=False)
            tts.save(str(audio_path))
            
            return str(audio_path)
            
        except Exception as e:
            print(f"Error synthesizing speech: {e}")
            return ""
    
    def play_audio(self, audio_path: str):
        """Play audio using PyAudio."""
        if not audio_path or not os.path.exists(audio_path):
            print(f"Audio file not found: {audio_path}")
            return
            
        try:
            # For MP3 files, we need to use a different approach
            import pygame
            pygame.mixer.init()
            pygame.mixer.music.load(audio_path)
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy():
                pygame.time.Clock().tick(10)
                
        except Exception as e:
            print(f"Error playing audio: {e}")
    
    def cleanup(self):
        """Clean up resources."""
        self.audio.terminate()
        # Clean up audio files older than 1 hour
        for file in self.output_dir.glob("*.mp3"):
            if file.stat().st_mtime < time.time() - 3600:
                try:
                    file.unlink()
                except:
                    pass