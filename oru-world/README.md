# Oru's World — 2D Animation (Remotion)

Calm, Oswald-style 2D animated sample for a kids' education channel, starring
**ORU** (the BabyOrgano mascot). Built with [Remotion](https://remotion.dev)
(programmatic video in React) using the `remotion-best-practices` skill.

## The sample: "Oru's World — A Day in the Garden"
30s · 1920×1080 · 30fps · original calm lullaby score.

Scenes (one continuous garden, gentle dissolves):
1. Sunrise — ORU waves outside his sprout-topped house 🌱
2. Garden — ORU waters the garden, 1·2·3 sprouts grow
3. Play — ORU plays football ⚽
4. Bath time — splish splash 🛁
5. Goodnight — ORU sleeps under the moon 🌙
6. BabyOrgano logo lockup + "Ayurveda for Everyday Growth"

## Files
- `src/oru/Oru.tsx` — the parametric ORU character rig (poses: wave, run, sit, sleep)
- `src/oru/World.tsx` — backdrop, sun, clouds, hills, flowers, house, props
- `src/oru/Caption.tsx` — on-screen kid-friendly captions
- `src/oru/OruWorld.tsx` — the timeline / scene sequencing + music
- `make_music.py` — generates the original calm music bed (no licensing)

## Render
```bash
npm install
python3 make_music.py            # writes public/oru-calm.wav
npx remotion studio              # live preview & edit
npx remotion render OruWorld out/oru-world.mp4
```

In a sandboxed/CI environment where Remotion can't download its Chrome shell,
point it at a local Chromium **headless shell**:
```bash
npx remotion render OruWorld out/oru-world.mp4 \
  --browser-executable=/path/to/chrome-headless-shell
```

## Notes
- ORU palette and the "Oruverse" (football, bath, sleep) follow the
  BabyOrgano packaging master.
- Animation uses `interpolate()` + `useCurrentFrame()` (no CSS transitions),
  per Remotion best practices.
