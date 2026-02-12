https://share.google/aimode/I5J4WUnmG4SKPwT5s


```python
import numpy as np
import matplotlib.pyplot as plt

# 1. Setup Signal Parameters
fs = 100          # Sampling frequency (Hz)
T = 1.0           # Duration (seconds)
t = np.arange(0, T, 1/fs)
freq = 5.5        # 5.5 Hz (non-integer cycles in 1s causes leakage)

# 2. Generate the Raw Signal
signal = np.sin(2 * np.pi * freq * t)

# 3. Create the Hanning Window
window = np.hanning(len(t))
windowed_signal = signal * window

# 4. Perform FFT
def get_fft(sig, fs):
    n = len(sig)
    mag = np.abs(np.fft.rfft(sig)) / (n / 2) # Normalized Magnitude
    freqs = np.fft.rfftfreq(n, 1/fs)
    return freqs, mag

f_rect, m_rect = get_fft(signal, fs)
f_hann, m_hann = get_fft(windowed_signal, fs)

# 5. Plotting
fig, axes = plt.subplots(2, 2, figsize=(12, 8))
plt.subplots_adjust(hspace=0.4)

# Time Domain Plots
axes[0,0].plot(t, signal, color='tab:red')
axes[0,0].set_title("Time Domain: No Window (Rectangular)")
axes[0,0].set_ylabel("Amplitude")

axes[0,1].plot(t, windowed_signal, color='tab:green')
axes[0,1].set_title("Time Domain: Hanning Window Applied")

# Frequency Domain Plots (The Spectra)
axes[1,0].stem(f_rect, m_rect, basefmt=" ")
axes[1,0].set_title("FFT: No Window (Notice the 'Leakage')")
axes[1,0].set_xlabel("Frequency (Hz)")
axes[1,0].set_ylabel("Magnitude")
axes[1,0].set_xlim(0, 15)

axes[1,1].stem(f_hann, m_hann, basefmt=" ")
axes[1,1].set_title("FFT: Hanning Window (Clean Peak)")
axes[1,1].set_xlabel("Frequency (Hz)")
axes[1,1].set_xlim(0, 15)

plt.show()

```