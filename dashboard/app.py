import streamlit as st
import os
import uuid

from utils.audio import load_audio, save_audio, plot_waveform, plot_spectrograms
from utils.denoise import reduce_noise_audio
from utils.metrics import compute_stoi_score, compute_pesq_score

# Page config
st.set_page_config(page_title="Audio Enhancement Dashboard", layout="wide")

# Title
st.title("🎧 Audio Noise Reduction Dashboard")

# Description
st.markdown("""
### 🔬 AI-based Audio Noise Reduction Demo

This tool demonstrates:
- Noise reduction using signal processing
- Audio quality evaluation using STOI/PESQ
- Spectrogram-based analysis

Built as part of GSoC 2026 ISSR proposal.
""")

# Ensure output folder exists
os.makedirs("outputs", exist_ok=True)

# File upload
uploaded_file = st.file_uploader("Upload a WAV file", type=["wav"])

if uploaded_file is not None:

    # Load audio
    y, sr = load_audio(uploaded_file)

    # Original audio
    st.subheader("🔊 Original Audio")
    st.audio(uploaded_file)

    # Waveform
    st.subheader("📊 Waveform")
    fig_wave = plot_waveform(y, sr)
    st.pyplot(fig_wave)

    # Noise reduction settings
    st.subheader("⚙️ Noise Reduction Settings")
    strength = st.slider("Reduction Strength", 0.0, 1.0, 0.5)

    # Run processing
    if st.button("Run Noise Reduction"):

        with st.spinner("Processing audio..."):
            y_denoised = reduce_noise_audio(y, sr, strength)

            # Unique file name (fix multi-user overwrite issue)
            output_path = f"outputs/{uuid.uuid4()}.wav"
            save_audio(output_path, y_denoised, sr)

        # Output audio
        st.subheader("🔊 Denoised Audio")
        st.audio(output_path)

        # Download button
        with open(output_path, "rb") as f:
            st.download_button(
                "⬇️ Download Denoised Audio",
                f,
                file_name="clean.wav"
            )

        # Comparison label
        st.write("### 🎵 Before vs After Comparison")

        # Spectrogram
        st.subheader("📈 Spectrogram Comparison")
        fig_spec = plot_spectrograms(y, y_denoised, sr)
        st.pyplot(fig_spec)

        # Metrics
        st.subheader("📏 Evaluation Metrics")

        stoi_score = compute_stoi_score(y, y_denoised, sr)
        pesq_score = compute_pesq_score(y, y_denoised, sr)

        col1, col2 = st.columns(2)
        col1.metric("STOI", f"{stoi_score:.4f}")
        col2.metric("PESQ", pesq_score)