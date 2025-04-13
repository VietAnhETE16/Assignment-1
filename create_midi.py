from mido import Message, MidiFile, MidiTrack
import wave

def get_wav_duration(wav_file):
    """Get the duration of a WAV file in seconds."""
    with wave.open(wav_file, 'rb') as wav:
        frames = wav.getnframes()
        rate = wav.getframerate()
        duration = frames / float(rate)
    return duration

# Path to the input WAV file
wav_file = 'recorded_audio.wav'

# Get the duration of the WAV file
wav_duration = get_wav_duration(wav_file)
print(f"Duration of '{wav_file}': {wav_duration:.2f} seconds")

# Create a new MIDI file and track
midi = MidiFile()
track = MidiTrack()
midi.tracks.append(track)

# Define tempo (microseconds per beat) and time signature
tempo = 500000  # 120 BPM
ticks_per_beat = 480  # Common default value for MIDI files
track.append(Message('program_change', program=26, time=0))  # Set instrument to Jazz Grand Piano

# Define a simple melody (note, duration in ticks)
notes = [
    (60, 240),  # C4
    (67, 240),  # G4
    (72, 480),  # C5 
    (64, 240),  # E4
    (69, 240),  # A4
    (74, 480),  # D5

    (62, 240),  # D4
    (69, 240),  # A4
    (74, 480),  # D5

    (60, 240),  # C4
    (64, 240),  # E4
    (67, 240),  # G4
    (72, 720),  # C5

    (59, 480),  # B3
    (62, 480),  # D4
    (67, 720),  # G4

    (60, 960),  # C4 (long hold)
]


# Calculate the total number of ticks for the WAV file duration
total_ticks_target = int((wav_duration * 1000000 / tempo) * ticks_per_beat)

# Repeat the melody to fill the duration of the WAV file
total_ticks = 0
while total_ticks < total_ticks_target:
    for note, duration in notes:
        if total_ticks >= total_ticks_target:
            break
        track.append(Message('note_on', note=note, velocity=64, time=0))
        track.append(Message('note_off', note=note, velocity=64, time=duration))
        total_ticks += duration

# Save the MIDI file
midi.save('midi_file.mid')
print("MIDI file 'midi_file.mid' created successfully.")