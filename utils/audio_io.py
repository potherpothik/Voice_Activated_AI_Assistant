import pyaudio
import wave
import os
import tempfile


class AudioIO:
    def __init__(self, channels=1, rate=16000, chunk=1024, format=pyaudio.paInt16):
        self.channels = channels
        self.rate = rate
        self.chunk = chunk
        self.format = format
        self.p = pyaudio.PyAudio()
    
    def record(self, seconds=5):
        """Record audio for a specified number of seconds."""
        # Open a streaming session
        stream = self.p.open(
            format=self.format,
            channels=self.channels,
            rate=self.rate,
            input=True,
            frames_per_buffer=self.chunk
        )
        
        print("Recording...")
        frames = []
        
        # Record for the specified duration
        for _ in range(0, int(self.rate / self.chunk * seconds)):
            data = stream.read(self.chunk)
            frames.append(data)
        
        print("Recording complete.")
        
        # Stop and close the stream
        stream.stop_stream()
        stream.close()
        
        # Create a temporary file
        temp_file = tempfile.NamedTemporaryFile(suffix=".wav", delete=False)
        
        # Save the recorded data as a WAV file
        with wave.open(temp_file.name, 'wb') as wf:
            wf.setnchannels(self.channels)
            wf.setsampwidth(self.p.get_sample_size(self.format))
            wf.setframerate(self.rate)
            wf.writeframes(b''.join(frames))
        
        return temp_file.name
    
    def play(self, file_path):
        """Play an audio file."""
        # Open the sound file
        wf = wave.open(file_path, 'rb')
        
        # Open a streaming session
        stream = self.p.open(
            format=self.p.get_format_from_width(wf.getsampwidth()),
            channels=wf.getnchannels(),
            rate=wf.getframerate(),
            output=True
        )
        
        # Read data in chunks
        data = wf.readframes(self.chunk)
        
        # Play the sound
        while len(data) > 0:
            stream.write(data)
            data = wf.readframes(self.chunk)
        
        # Stop and close the stream
        stream.stop_stream()
        stream.close()
    
    def cleanup(self):
        """Terminate the PyAudio session."""
        self.p.terminate()
