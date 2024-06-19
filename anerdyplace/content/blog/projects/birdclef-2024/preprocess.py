"""
This is a script to preprocess audio files for the birdclef-2024 project.

Author: Philipp Unger
Project: birdclef-2024

https://git.fim.uni-passau.de/ungerp/ss24-aai-lab
"""

import multiprocessing
import os
import time
from os.path import exists
from pathlib import Path

import librosa
import matplotlib.pyplot as plt
import noisereduce as nr
import numpy as np
from tqdm import tqdm

def load_config():
    with open('config.json', 'r') as f:
        _config = json.load(f)
    return _config

config = load_config()
_input_folder = config["audio_files_input_path"]
_output_folder = config["audio_files_output_path"]


def load_audio(filename):
    # Load an audio file as a floating point time series.
    audio, sr = librosa.load(filename, sr=None)
    return audio, sr


def pad_audio(audio, n_fft):
    # If audio is too short, pad it with zeros
    if len(audio) < n_fft:
        audio = np.pad(audio, (0, n_fft - len(audio)), mode="constant")
    return audio


def segment_audio(segment, segment_length=5, sr=32000):
    # Segment audio; each chunk is a list of smaller chunks of `segment_length` seconds
    segmented_chunks = []
    samples_per_segment = segment_length * sr
    for start in range(0, len(segment), samples_per_segment):
        end = start + samples_per_segment
        segmented_chunks.append(segment[start:end])
    return segmented_chunks


def generate_square_spectrogram(audio, sr, output_path, size=224, fmin=2000, fmax=8000):
    # Compute the Mel-scaled spectrogram with specified frequency range
    s = librosa.feature.melspectrogram(y=audio, sr=sr, n_mels=128, fmax=fmax, fmin=fmin)

    # Convert to decibels
    s_dB = librosa.power_to_db(s, ref=np.max)

    # Plotting
    plt.figure(figsize=(size / 100, size / 100), dpi=100)  # Set the figure size to achieve the desired image size
    librosa.display.specshow(s_dB, sr=sr, x_axis='time', y_axis='mel', fmin=fmin, fmax=fmax, cmap='gray')
    plt.axis('off')  # Disable axes to make the image square

    # Remove borders and white space
    plt.tight_layout(pad=0)

    # Save the figure as a grayscale image
    plt.savefig(output_path, bbox_inches='tight', pad_inches=0)
    plt.close()


def process_file(file_paths):
    input_file_path, output_file_path = file_paths

    # print(f"Processing {input_file_path}")
    audio, sr = load_audio(input_file_path)
    # audio = apply_highpass_filter(audio, sr, cutoff_freq=2000.0, order=5)
    audio = nr.reduce_noise(audio, sr)  # Works much better!

    segment_length_seconds = 5
    samples_per_segment = segment_length_seconds * sr  # sr is the sample rate

    segments = segment_audio(audio, segment_length=segment_length_seconds, sr=sr)

    for i, segment in enumerate(segments):

        # If the segment is smaller than 5 seconds, skip it
        # This helps cleaning the data and avoiding distorted spectrograms
        if len(segment) < samples_per_segment:
            continue

        # Extract the directory and filename parts
        directory = os.path.dirname(output_file_path)
        filename = os.path.basename(output_file_path)
        filename_without_extension, extension = os.path.splitext(filename)

        image_name = os.path.join(
            directory,
            f"{filename_without_extension}_{i}.{extension}",
        )

        # os.makedirs(
        #     os.path.dirname(image_name), exist_ok=True
        # )  # Create output folders if they don't exist
        if not exists(image_name):  # Saves at least a little bit of time...
            # generate_spectrogram(segment, sr, image_name)
            generate_square_spectrogram(segment, sr, image_name)


def prepare_file_pairs(input_folder, output_folder):
    file_pairs = []
    input_folder = Path(input_folder)
    output_folder = Path(output_folder)
    for input_path in input_folder.rglob('*.ogg'):
        output_path = output_folder / input_path.relative_to(input_folder).with_suffix('.png')
        output_path.parent.mkdir(parents=True, exist_ok=True)  # Ensure output directory exists
        file_pairs.append((input_path, output_path))
    return file_pairs


def parallel_process_files(input_folder, output_folder):
    # Prepare input-output file pairs
    file_pairs = prepare_file_pairs(input_folder, output_folder)

    if not file_pairs:
        print("No new files to process.")
        return

    # Determine the number of processes to use
    num_processes = multiprocessing.cpu_count()

    # Create a pool of processes
    with multiprocessing.Pool(processes=num_processes) as pool:
        list(tqdm(pool.imap(process_file, file_pairs), total=len(file_pairs), desc="Processing Files"))

    print("Processing complete.")


if __name__ == "__main__":
    start_time = time.time()
    parallel_process_files(_input_folder, _output_folder)
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Processing files took {elapsed_time} seconds.")
