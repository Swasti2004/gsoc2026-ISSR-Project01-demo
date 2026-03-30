import streamlit as st
import os
from utils.audio import load_audio, save_audio, plot_waveform, plot_spectrograms
from utils.denoise import reduce_noise_audio
from utils.metrics import compute_stoi_score, compute_pesq_score

st.set_page_config(page_title="Audio Enhancement Dashboard", layout="wide")

st.title("🎧 Audio Noise Reduction Dashboard")

# Ensure output folder exists
os.makedirs("outputs", exist_ok=True)

uploaded_file = st.file_uploader("Upload a WAV file", type=["wav"])

if uploaded_file is not None:

    # Load audio
    y, sr = load_audio(uploaded_file)

    # Play original
    st.subheader("🔊 Original Audio")
    st.audio(uploaded_file)

    # Waveform
    st.subheader("📊 Waveform")
    fig_wave = plot_waveform(y, sr)
    st.pyplot(fig_wave)

    # Noise reduction control
    st.subheader("⚙️ Noise Reduction Settings")
    strength = st.slider("Reduction Strength", 0.0, 1.0, 0.5)

    # Process
    if st.button("Run Noise Reduction"):
        y_denoised = reduce_noise_audio(y, sr, strength)

        output_path = "outputs/denoised.wav"
        save_audio(output_path, y_denoised, sr)

        # Play output
        st.subheader("🔊 Denoised Audio")
        st.audio(output_path)

        # Spectrogram
        st.subheader("📈 Spectrogram Comparison")
        fig_spec = plot_spectrograms(y, y_denoised, sr)
        st.pyplot(fig_spec)

        # Metrics
        st.subheader("📏 Evaluation Metrics")

        stoi_score = compute_stoi_score(y, y_denoised, sr)
        st.write(f"**STOI Score:** {stoi_score:.4f}")

        pesq_score = compute_pesq_score(y, y_denoised, sr)
        st.write(f"**PESQ Score:** {pesq_score}")