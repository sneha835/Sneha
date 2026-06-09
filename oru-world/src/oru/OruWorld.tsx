import React from "react";
import { AbsoluteFill, Audio, Sequence, useCurrentFrame, interpolate, Easing, staticFile } from "remotion";
import { Oru, OruSleeping } from "./Oru";
import { Caption } from "./Caption";
import {
  Backdrop,
  OruHouse,
  Lavender,
  Daisy,
  WateringCan,
  WaterStream,
  Sprout,
  Football,
  Goal,
  BathTub,
  BathTubFront,
  Bubbles,
  Bed,
  Moon,
  Stars,
  Zzz,
  Wordmark,
} from "./World";

const SVG: React.FC<{ children: React.ReactNode; opacity?: number }> = ({ children, opacity = 1 }) => (
  <svg viewBox="0 0 1920 1080" width="100%" height="100%" style={{ position: "absolute" }}>
    <g opacity={opacity}>{children}</g>
  </svg>
);

// fade foreground in/out at the edges of a scene
const useFade = (duration: number) => {
  const f = useCurrentFrame();
  return Math.min(
    interpolate(f, [0, 18], [0, 1], { extrapolateRight: "clamp", easing: Easing.out(Easing.cubic) }),
    interpolate(f, [duration - 18, duration], [1, 0], { extrapolateLeft: "clamp" })
  );
};

const breathe = (f: number, amp = 6, period = 70) => Math.sin(f / period) * amp;

/* persistent garden flowers (sit in front, whole film) */
const Garden: React.FC = () => (
  <SVG>
    <Lavender x={120} y={1000} s={1.1} phase={0} />
    <Daisy x={250} y={1020} s={1.0} phase={1.5} />
    <Lavender x={1780} y={1000} s={1.2} phase={2} />
    <Daisy x={1660} y={1025} s={1.0} phase={0.7} />
    <Daisy x={1830} y={1030} s={0.8} phase={3} />
  </SVG>
);

/* ---------------- Scenes ---------------- */
const S1: React.FC<{ d: number }> = ({ d }) => {
  const f = useCurrentFrame();
  const op = useFade(d);
  const wave = (Math.sin(f / 7) * 0.5 + 0.5) * 0.7; // gentle waving
  return (
    <SVG opacity={op}>
      <OruHouse x={1430} y={880} s={1.05} />
      <g transform={`translate(0 ${breathe(f)})`}>
        <Oru x={690} y={655} scale={1.7} eyeOpen={0} mouthOpen={1} wave={wave} />
      </g>
    </SVG>
  );
};

const S2: React.FC<{ d: number }> = ({ d }) => {
  const f = useCurrentFrame();
  const op = useFade(d);
  const pour = interpolate(f, [20, 45, d - 25, d - 5], [0, 1, 1, 0], { extrapolateLeft: "clamp", extrapolateRight: "clamp" });
  const g1 = interpolate(f, [40, 90], [0, 1], { extrapolateLeft: "clamp", extrapolateRight: "clamp" });
  const g2 = interpolate(f, [70, 120], [0, 1], { extrapolateLeft: "clamp", extrapolateRight: "clamp" });
  const g3 = interpolate(f, [100, 150], [0, 1], { extrapolateLeft: "clamp", extrapolateRight: "clamp" });
  return (
    <SVG opacity={op}>
      <g transform={`translate(0 ${breathe(f, 4)})`}>
        <Oru x={520} y={665} scale={1.6} eyeOpen={0} mouthOpen={0} />
      </g>
      <WateringCan x={760} y={770} s={1.4} pour={pour} />
      <WaterStream x={880} y={770} on={pour > 0.3 ? 1 : 0} />
      <Sprout x={980} y={905} grow={g1} />
      <Sprout x={1110} y={905} grow={g2} />
      <Sprout x={1240} y={905} grow={g3} />
    </SVG>
  );
};

const S3: React.FC<{ d: number }> = ({ d }) => {
  const f = useCurrentFrame();
  const op = useFade(d);
  const ballX = interpolate(f, [0, d], [1060, 1360], { easing: Easing.out(Easing.quad) });
  const roll = interpolate(f, [0, d], [0, 540]);
  const bob = Math.abs(Math.sin(f / 6)) * -10; // little running bounce
  return (
    <SVG opacity={op}>
      <Goal x={1560} y={880} s={1.15} />
      <g transform={`translate(0 ${bob})`}>
        <Oru x={760} y={650} scale={1.55} eyeOpen={0} mouthOpen={1} run={1} lean={8} wave={0.5} />
      </g>
      <Football x={ballX} y={905} s={1} roll={roll} />
    </SVG>
  );
};

const S4: React.FC<{ d: number }> = ({ d }) => {
  const f = useCurrentFrame();
  const op = useFade(d);
  const splash = Math.sin(f / 9) * 4;
  return (
    <SVG opacity={op}>
      <BathTub x={960} y={730} s={1.25} />
      <g transform={`translate(0 ${splash})`}>
        <Oru x={960} y={560} scale={1.05} eyeOpen={0} mouthOpen={1} wave={0.25} />
      </g>
      <BathTubFront x={960} y={730} s={1.25} />
      <Bubbles x={960} y={690} on={1} />
    </SVG>
  );
};

const S5: React.FC<{ d: number }> = ({ d }) => {
  const f = useCurrentFrame();
  const op = useFade(d);
  const dusk = interpolate(f, [0, 50], [0, 0.5], { extrapolateRight: "clamp" });
  const moonIn = interpolate(f, [20, 70], [0, 1], { extrapolateLeft: "clamp", extrapolateRight: "clamp" });
  const br = breathe(f, 3, 50);
  return (
    <SVG opacity={op}>
      {/* dusk tint over the world */}
      <rect x={0} y={0} width={1920} height={1080} fill="#1F2A55" opacity={dusk} />
      <g opacity={moonIn}>
        <Stars on={1} />
        <Moon x={1560} y={230} s={1.05} />
      </g>
      <Bed x={960} y={860} s={1.05} />
      <g transform={`translate(0 ${br})`}>
        <OruSleeping x={770} y={815} scale={1.15} breathe={Math.sin(f / 30) * 0.5 + 0.5} />
      </g>
      <Zzz x={1010} y={770} />
    </SVG>
  );
};

const S6: React.FC<{ d: number }> = ({ d }) => {
  const f = useCurrentFrame();
  const cream = interpolate(f, [0, 22], [0, 1], { extrapolateRight: "clamp" });
  const pop = interpolate(f, [18, 40], [0.6, 1], { extrapolateLeft: "clamp", extrapolateRight: "clamp", easing: Easing.out(Easing.back(1.4)) });
  const wave = (Math.sin(f / 7) * 0.5 + 0.5) * 0.7;
  const txtOp = interpolate(f, [34, 54], [0, 1], { extrapolateLeft: "clamp", extrapolateRight: "clamp" });
  return (
    <SVG>
      <rect x={0} y={0} width={1920} height={1080} fill="#F4ECD7" opacity={cream} />
      <g opacity={cream}>
        <g transform={`translate(960 ${260 + breathe(f, 5)}) scale(${pop})`}>
          <Oru x={0} y={0} scale={1.5} eyeOpen={0} mouthOpen={1} wave={wave} />
        </g>
        <g opacity={txtOp}>
          <Wordmark x={960} y={620} s={1} />
          <text x={960} y={812} textAnchor="middle" fontFamily="'Baloo 2','Trebuchet MS',sans-serif" fontWeight={700} fontSize={42} fill="#5C9B3E">
            Ayurveda for Everyday Growth
          </text>
        </g>
      </g>
    </SVG>
  );
};

/* ---------------- Timeline ---------------- */
const D = { s1: 150, s2: 180, s3: 150, s4: 150, s5: 165, s6: 105 };
const T = {
  s1: 0,
  s2: 150,
  s3: 330,
  s4: 480,
  s5: 630,
  s6: 795,
};

export const OruWorld: React.FC = () => {
  return (
    <AbsoluteFill style={{ backgroundColor: "#F4ECD7" }}>
      {/* persistent world */}
      <Backdrop />
      <Garden />

      {/* scene foregrounds */}
      <Sequence from={T.s1} durationInFrames={D.s1}><S1 d={D.s1} /></Sequence>
      <Sequence from={T.s2} durationInFrames={D.s2}><S2 d={D.s2} /></Sequence>
      <Sequence from={T.s3} durationInFrames={D.s3}><S3 d={D.s3} /></Sequence>
      <Sequence from={T.s4} durationInFrames={D.s4}><S4 d={D.s4} /></Sequence>
      <Sequence from={T.s5} durationInFrames={D.s5}><S5 d={D.s5} /></Sequence>
      <Sequence from={T.s6} durationInFrames={D.s6}><S6 d={D.s6} /></Sequence>

      {/* captions */}
      <Sequence from={T.s1} durationInFrames={D.s1}><Caption duration={D.s1} title="Oru's World" sub="a calm day in the garden" position="bottom" /></Sequence>
      <Sequence from={T.s2} durationInFrames={D.s2}><Caption duration={D.s2} title="Good morning!" sub="Let's grow 1… 2… 3 little sprouts" position="top" /></Sequence>
      <Sequence from={T.s3} durationInFrames={D.s3}><Caption duration={D.s3} title="Time to play!" sub="Kick the ball, Oru" position="top" /></Sequence>
      <Sequence from={T.s4} durationInFrames={D.s4}><Caption duration={D.s4} title="Splish, splash!" sub="bath time" position="top" /></Sequence>
      <Sequence from={T.s5} durationInFrames={D.s5}><Caption duration={D.s5} title="Goodnight, Oru" sub="sweet dreams 🌙" position="top" color="#FDF3C4" /></Sequence>

      {/* gentle calm music with fades */}
      <Audio src={staticFile("oru-calm.wav")} volume={(f) => interpolate(f, [0, 40, 840, 900], [0, 0.85, 0.85, 0], { extrapolateLeft: "clamp", extrapolateRight: "clamp" })} />
    </AbsoluteFill>
  );
};
