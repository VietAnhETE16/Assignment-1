import os
import subprocess

def midi_to_wav(midi_file, soundfont_path, wav_file):
    # Command to convert MIDI to WAV using fluidsynth
    cmd = [
        "fluidsynth",
        "-ni", soundfont_path,
        midi_file,
        "-F", wav_file,
        "-r", "48000"
    ]
    print("Running command:", " ".join(cmd))
    try:
        subprocess.run(cmd, check=True)
        print(f"Conversion complete: {wav_file}")
    except subprocess.CalledProcessError as e:
        print(f"Error during conversion: {e}")


if __name__ == "__main__":
    midi_file = "midi_file.mid"  
    wav_file = "converted_midi.wav"  
    soundfont_path = "C:/SoundFonts/FluidR3_GM.sf2"  

    if not os.path.exists(midi_file):
        print(f"Error: {midi_file} does not exist.")
    elif not os.path.exists(soundfont_path):
        print(f"Error: {soundfont_path} does not exist.")
    else:
        midi_to_wav(midi_file, soundfont_path, wav_file)