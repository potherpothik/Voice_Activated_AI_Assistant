import os
import wave
from deepgram import Deepgram
from typing import Optional
import pyaudio
import tempfile
import sys
sys.path.append('..')
from config import DEEPGRAM_API_KEY, CHANNELS, RATE, CHUNK, RECORD_SECONDS


class SpeechToText:
    def __init__(self):
        self.deepgram = Deepgram(DEEPGRAM_API_KEY)
        self.temp_file = tempfile.NamedTemporaryFile(suffix=".wav", delete=False)
        self.temp_file_name = self.temp_file.name
        self.temp_file.close()  # Close the file handle immediately

    def record_audio(self) -> str:
        """Record audio from microphone and return the file path."""
        p = pyaudio.PyAudio()
        
        print("Recording...")
        
        stream = p.open(format=pyaudio.paInt16,
                        channels=CHANNELS,
                        rate=RATE,
                        input=True,
                        frames_per_buffer=CHUNK)
        
        frames = []
        
        for _ in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
            data = stream.read(CHUNK)
            frames.append(data)
        
        print("Recording finished.")
        
        stream.stop_stream()
        stream.close()
        p.terminate()
        
        # Save the recorded audio to a temporary file
        wf = wave.open(self.temp_file_name, 'wb')
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(p.get_sample_size(pyaudio.paInt16))
        wf.setframerate(RATE)
        wf.writeframes(b''.join(frames))
        wf.close()
        
        return self.temp_file_name

    async def transcribe_audio(self, audio_file: Optional[str] = None) -> str:
        """Transcribe audio file to text using Deepgram."""
        file_path = audio_file if audio_file else self.temp_file_name
        
        with open(file_path, "rb") as audio:
            source = {
                "buffer": audio.read(),
                "mimetype": "audio/wav"
            }
            
            response = await self.deepgram.transcription.prerecorded(
                source,
                {
                    "smart_format": True,
                    "model": "nova-2",
                    "language": "en-US"
                }
            )
            
            # Get the transcript from the response
            transcript = response["results"]["channels"][0]["alternatives"][0]["transcript"]
            
            return transcript

    def cleanup(self):
        """Remove the temporary file."""
        try:
            if self.temp_file_name and os.path.exists(self.temp_file_name):
                os.unlink(self.temp_file_name)
        except PermissionError:
            # If we can't delete the file now, it will be cleaned up by the OS later
            pass