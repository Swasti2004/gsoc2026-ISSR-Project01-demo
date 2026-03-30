# Team Communication Processing & Analysis
### GSoC 2026 Screening — HumanAI / TRIP Lab, University of Alabama

---

## Overview

This repository is the screening submission for the **Team Communication Processing and Analysis in Human-Factors Simulated Environment** project, HumanAI organization / TRIP Lab, University of Alabama.

The TRIP Lab studies team performance in simulated environments — settings where groups operate under realistic task conditions to examine coordination, distraction, and communication as human factors. This submission builds a pipeline that processes, enhances, and evaluates team communication audio with the direct goal of improving downstream transcription accuracy.

---

## Quick Start

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Download audio samples (run once — ~3 min each)
python generate_samples.py

# 3. Run notebooks in order
jupyter notebook Notebook1_Dataset_Selection.ipynb
jupyter notebook Notebook2_Audio_Enhancement.ipynb
```

> **Note on Whisper:** The `openai-whisper` package downloads the `base` model (~140 MB) on first run. No GPU required — all processing runs on CPU for the 3-minute sample used here.

---

## Repository Structure

```
├── Notebook1_Dataset_Selection.ipynb    # Dataset evaluation, selection & EDA
├── Notebook2_Audio_Enhancement.ipynb    # Enhancement methods, NLP & evaluation
├── generate_samples.py                  # Downloads AMI IHM + SDM audio samples
├── requirements.txt                     # All Python dependencies
└── README.md
```

**Generated at runtime (after running the notebooks):**
```
├── ami_ihm_sample.wav                   # IHM clean reference (~3 min)
├── ami_sdm_sample.wav                   # SDM degraded input (~3 min)
├── enhanced_highpass.wav
├── enhanced_spectral_subtraction.wav
├── enhanced_wiener.wav
├── enhanced_noisereduce.wav
├── enhanced_adaptive.wav                # Method 5 — adaptive pipeline
└── [visualisation .png files]
```

---

## Notebook 1 — Dataset Selection & Exploratory Analysis

Answers the two required test questions: *How will the dataset be used?* and *Why is this the best option?*

| Section | Content |
|---|---|
| 1 | Selection criteria derived from TRIP Lab's research context |
| 2 | Scored comparison: AMI vs CHiME-6 vs NOXI vs LibriSpeech |
| 3 | AMI rationale — multi-mic architecture, scenario meetings, open access |
| 4 | Data loading — IHM + SDM streams from the same session |
| 5 | Signal EDA — waveform, spectrogram, SNR distribution, MFCC comparison |
| 6 | Team dynamics — speech activity, overlap proxy, energy variability |
| 7 | Structured answers to both required questions with measured values |

**Key design choice:** Both IHM (clean headset) and SDM (single distant mic) conditions are loaded from the same session. This enables real acoustic degradation benchmarking with no synthetic noise added.

---

## Notebook 2 — Audio Enhancement & Evaluation

Primary metric: **Word Error Rate (WER)** via Whisper — directly measures whether enhancement improves transcription.

| Section | Content |
|---|---|
| 1 | Load audio |
| 2 | Baseline — raw IHM–SDM acoustic gap |
| 3 | Whisper WER baseline before any enhancement |
| 4 | Five enhancement methods on real SDM audio |
| 5 | Visual analysis — waveform, spectrogram, PSD |
| 6 | WER evaluation per method |
| 6b | NLP analysis — transcript inspection, vocabulary overlap, content-word recovery |
| 7 | Full metric table — WER + STOI + PESQ + DNSMOS + SNR |
| 8 | Pipeline ordering analysis |
| 9 | Conclusion and recommendation |

---

## Enhancement Methods

| # | Method | Type |
|---|---|---|
| 1 | High-pass filter + normalisation | Classical |
| 2 | Spectral subtraction | Classical |
| 3 | Wiener filter | Classical |
| 4 | NoiseReduce (non-stationary) | DL-inspired |
| 5 | **Adaptive pipeline** | **Ours** — HP → NoiseReduce → Wiener → normalise |

---

## Evaluation Metrics

| Metric | Type | Rationale |
|---|---|---|
| **WER** (primary) | Transcription | Directly measures the project's stated goal |
| STOI | Perceptual | Speech intelligibility |
| PESQ | Perceptual | ITU-T P.862.2 wideband quality |
| DNSMOS | Non-intrusive | No reference needed — usable in real studies |
| SNR | Signal | Baseline comparison only |

---

## Dataset: AMI Meeting Corpus

Edinburgh CSTR / HuggingFace `edinburghcstr/ami`. 100+ hours, 4–5 speakers, structured task-oriented meetings, three simultaneous mic conditions (IHM / SDM / MDM), word-level transcripts, free access.

---

## References

- Carletta et al. (2005). *The AMI Meeting Corpus.* MLMI 2005.
- Radford et al. (2023). *Robust Speech Recognition via Large-Scale Weak Supervision.* ICML 2023.
- Reddy et al. (2022). *DNSMOS P.835.* ICASSP 2022.
- Taal et al. (2011). *STOI.* IEEE TASLP.
- ITU-T P.862.2 (2007). (PESQ)
- Sainburg (2019). *noisereduce.* github.com/timsainb/noisereduce
