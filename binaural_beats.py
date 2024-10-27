import numpy as np
import time
import sounddevice as sd

def generate_binaural_beat(freq1=400, freq2=415, duration=20, volume=1.0):
    """Generates a binaural beat with given frequencies and duration."""
    time.sleep(17)

    sample_rate = 44100  # Standard audio sampling rate
    t = np.linspace(0, duration, int(duration * sample_rate), False)

    # Generate the left and right channel waveforms
    left_channel = volume * np.sin(2 * np.pi * freq1 * t)
    right_channel = volume * np.sin(2 * np.pi * freq2 * t)

    # Combine channels into a stereo signal
    stereo_signal = np.vstack((left_channel, right_channel)).T

    # Play the sound
    sd.play(stereo_signal, samplerate=sample_rate)
    sd.wait()

    #return stereo_signal
