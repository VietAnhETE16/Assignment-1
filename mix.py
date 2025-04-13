import wave
import numpy as np

def mix_wav_files(file1, file2, output_file, gain=1.0):
    # Open the first WAV file
    with wave.open(file1, 'rb') as wav1:
        params1 = wav1.getparams()
        frames1 = wav1.readframes(params1.nframes)
        data1 = np.frombuffer(frames1, dtype=np.int16)

    # Open the second WAV file
    with wave.open(file2, 'rb') as wav2:
        params2 = wav2.getparams()
        frames2 = wav2.readframes(params2.nframes)
        data2 = np.frombuffer(frames2, dtype=np.int16)

    # Pad the shorter audio with zeros to match the length of the longer audio
    max_length = max(len(data1), len(data2))
    if len(data1) < max_length:
        data1 = np.pad(data1, (0, max_length - len(data1)), mode='constant', constant_values=0)
    if len(data2) < max_length:
        data2 = np.pad(data2, (0, max_length - len(data2)), mode='constant', constant_values=0)

    # Mix the audio data
    mixed_data = data1 // 2 + data2 // 2

    # Apply gain to increase volume
    mixed_data = (mixed_data * gain).clip(-32768, 32767)  # Ensure values stay within int16 range

    # Write the mixed data to the output file
    with wave.open(output_file, 'wb') as output_wav:
        output_wav.setparams(params1)
        output_wav.writeframes(mixed_data.astype(np.int16).tobytes())

def check_wav_params(file):
    with wave.open(file, 'rb') as wav:
        params = wav.getparams()
        print(f"File: {file}")
        print(f"  Channels: {params.nchannels}")
        print(f"  Sample Width: {params.sampwidth}")
        print(f"  Frame Rate: {params.framerate}")
        print(f"  Number of Frames: {params.nframes}")
        print(f"  Duration: {params.nframes / params.framerate:.2f} seconds\n")

file1 = "recorded_audio.wav"
file2 = "converted_midi.wav"
output_file = "mixed_output.wav"

check_wav_params(file1)
check_wav_params(file2)

# Mix files with increased volume (gain = 3.0)
mix_wav_files(file1, file2, output_file, gain=3.0)