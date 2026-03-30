from pystoi import stoi

# PESQ safe import
try:
    from pesq import pesq
    PESQ_AVAILABLE = True
except:
    PESQ_AVAILABLE = False


def compute_stoi_score(y, y_denoised, sr):
    min_len = min(len(y), len(y_denoised))
    return stoi(y[:min_len], y_denoised[:min_len], sr)


def compute_pesq_score(y, y_denoised, sr):
    if not PESQ_AVAILABLE:
        return "Not Available"

    try:
        min_len = min(len(y), len(y_denoised))
        score = pesq(sr, y[:min_len], y_denoised[:min_len], 'wb')
        return round(score, 4)
    except:
        return "Error"