import librosa
import soundfile as sf
import matplotlib.pyplot as plt
import librosa.display
import numpy as np

def load_audio(file):
    y, sr = librosa.load(file, sr=None)
    return y, sr

def save_audio(path, y, sr):
    sf.write(path, y, sr)

def plot_waveform(y, sr):
    fig, ax = plt.subplots()
    librosa.display.waveshow(y, sr=sr, ax=ax)
    ax.set_title("Waveform")
    return fig

def plot_spectrograms(y1, y2, sr):
    fig, ax = plt.subplots(1, 2, figsize=(12, 4))

    D1 = librosa.amplitude_to_db(abs(librosa.stft(y1)), ref=np.max)
    librosa.display.specshow(D1, sr=sr, x_axis='time', y_axis='log', ax=ax[0])
    ax[0].set_title("Original")

    D2 = librosa.amplitude_to_db(abs(librosa.stft(y2)), ref=np.max)
    librosa.display.specshow(D2, sr=sr, x_axis='time', y_axis='log', ax=ax[1])
    ax[1].set_title("Denoised")

    return fig