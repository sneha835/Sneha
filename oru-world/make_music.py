#!/usr/bin/env python3
"""Generate a calm, lullaby-style music bed for Oru's World.
Soft sustained pad (I-vi-IV-V) + gentle music-box pentatonic melody.
Original composition, no external assets. Outputs 44.1k stereo WAV.
"""
import numpy as np, wave, struct

SR = 44100
BPM = 68
beat = 60.0 / BPM

def note(freq):  # midi-ish helper via frequency directly
    return freq

# Note frequencies
N = {
    'C3':130.81,'E3':164.81,'G3':196.00,'A3':220.00,'F3':174.61,'D3':146.83,
    'C4':261.63,'D4':293.66,'E4':329.63,'F4':349.23,'G4':392.00,'A4':440.00,'B4':493.88,
    'C5':523.25,'D5':587.33,'E5':659.25,'G5':783.99,'A5':880.00,
}

def env_pad(n, attack, release):
    e = np.ones(n)
    a = int(attack*SR); r = int(release*SR)
    a = min(a, n//2); r = min(r, n//2)
    if a>0: e[:a] = np.linspace(0,1,a)
    if r>0: e[-r:] = np.linspace(1,0,r)
    return e

def pad_chord(freqs, dur):
    n = int(dur*SR)
    t = np.arange(n)/SR
    sig = np.zeros(n)
    for f in freqs:
        # warm pad: fundamental + soft harmonics, slight detune for width
        sig += np.sin(2*np.pi*f*t)
        sig += 0.5*np.sin(2*np.pi*f*1.002*t)
        sig += 0.28*np.sin(2*np.pi*2*f*t)
        sig += 0.12*np.sin(2*np.pi*3*f*t)
    sig /= (len(freqs)*1.9)
    sig *= env_pad(n, 0.9, 1.1)
    return sig

def bell(freq, dur, amp=0.5):
    n = int(dur*SR)
    t = np.arange(n)/SR
    # music-box / soft bell: a few inharmonic partials with exp decay
    s  = 1.0*np.sin(2*np.pi*freq*t)*np.exp(-t*3.0)
    s += 0.6*np.sin(2*np.pi*2*freq*t)*np.exp(-t*4.5)
    s += 0.25*np.sin(2*np.pi*3.01*freq*t)*np.exp(-t*6.0)
    # gentle pluck attack
    s *= np.minimum(1.0, t/0.005)
    return s*amp

# ---- Pad progression: C  Am  F  G  (each 2 bars = 8 beats) ----
chords = [
    (['C3','C4','E4','G4'], 8*beat),
    (['A3','C4','E4','A4'], 8*beat),
    (['F3','C4','F4','A4'], 8*beat),
    (['G3','D4','G4','B4'], 8*beat),
]
pad = np.concatenate([pad_chord([N[x] for x in c], d) for c,d in chords])
pad = np.tile(pad, 2)  # two passes
total = len(pad)

# ---- Melody: gentle pentatonic phrases over the progression ----
mel = np.zeros(total)
# (note, start_beat, dur_beats) — soft, sparse, lullaby phrasing
phrase = [
    ('G4',0,2),('E4',2,2),('C5',4,2),('G4',6,2),          # over C
    ('A4',8,2),('C5',10,2),('E5',12,3),('C5',15,1),       # over Am
    ('A4',16,2),('F4',18,2),('A4',20,2),('C5',22,2),      # over F
    ('B4',24,2),('D5',26,2),('G4',28,4),                  # over G
]
def place(sig, src, start_sample):
    end = min(len(sig), start_sample+len(src))
    sig[start_sample:end] += src[:end-start_sample]

bars_samples = int(8*beat*SR)
for pass_i in range(2):
    base = pass_i*4*bars_samples
    for nm, sb, db in phrase:
        st = base + int(sb*beat*SR)
        place(mel, bell(N[nm], db*beat*0.98, amp=0.42), st)

# ---- Soft sub bass on chord roots ----
bass = np.zeros(total)
roots = ['C3','A3','F3','G3']*2
for i,r in enumerate(roots):
    st = i*bars_samples
    n = bars_samples
    t = np.arange(n)/SR
    b = (np.sin(2*np.pi*(N[r]/2)*t))*env_pad(n,0.4,0.6)*0.35
    place(bass, b, st)

# ---- Mix ----
mix = 0.55*pad + 0.9*mel + 0.6*bass

# ---- Simple Schroeder-ish reverb (a few decayed delays) ----
def reverb(x, delays_ms=(37,53,71,97), decay=0.35):
    out = x.copy()
    for d in delays_ms:
        ds = int(d*SR/1000)
        echo = np.zeros_like(x)
        echo[ds:] = x[:-ds]*decay
        out += echo
        decay *= 0.7
    return out
wet = reverb(mix)
mix = 0.75*mix + 0.45*wet

# ---- Master: gentle fade in/out + normalize ----
fade = int(1.6*SR)
mix[:fade] *= np.linspace(0,1,fade)
mix[-fade:] *= np.linspace(1,0,fade)
peak = np.max(np.abs(mix)) or 1.0
mix = (mix/peak)*0.85

# soft stereo: tiny haas + pan width
left = mix.copy()
right = mix.copy()
sh = int(0.008*SR)
right[sh:] = mix[:-sh]
stereo = np.stack([left, right], axis=1)

# write 16-bit WAV
data = np.clip(stereo, -1, 1)
ints = (data*32767).astype('<i2')
with wave.open('/tmp/cartoon-demo/public/oru-calm.wav','wb') as w:
    w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR)
    w.writeframes(ints.tobytes())
print("wrote oru-calm.wav  duration %.2fs" % (total/SR))
