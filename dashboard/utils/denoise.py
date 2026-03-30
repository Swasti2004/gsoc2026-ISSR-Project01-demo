import noisereduce as nr

def reduce_noise_audio(y, sr, strength=0.5):
    reduced = nr.reduce_noise(y=y, sr=sr, prop_decrease=strength)
    return reduced