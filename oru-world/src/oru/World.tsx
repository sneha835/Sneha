import React from "react";
import { useCurrentFrame, interpolate, Easing } from "remotion";

const BRAND = "#2E6B2E";

/* ------------------------------------------------------------------ */
/* Persistent garden backdrop — rendered for the whole film so scene   */
/* changes dissolve over a continuous world (the "Oruverse").          */
/* ------------------------------------------------------------------ */
export const Backdrop: React.FC = () => {
  const frame = useCurrentFrame();
  const rayRot = interpolate(frame, [0, 900], [0, 25]);
  return (
    <svg viewBox="0 0 1920 1080" width="100%" height="100%" style={{ position: "absolute" }}>
      <defs>
        <linearGradient id="sky" x1="0" y1="0" x2="0" y2="1">
          <stop offset="0%" stopColor="#BFE6F2" />
          <stop offset="55%" stopColor="#DCEFE3" />
          <stop offset="100%" stopColor="#F4ECD7" />
        </linearGradient>
        <radialGradient id="sunGlow" cx="50%" cy="50%" r="50%">
          <stop offset="0%" stopColor="#FFF4CF" stopOpacity={0.9} />
          <stop offset="100%" stopColor="#FFF4CF" stopOpacity={0} />
        </radialGradient>
        <linearGradient id="grass" x1="0" y1="0" x2="0" y2="1">
          <stop offset="0%" stopColor="#8FCB63" />
          <stop offset="100%" stopColor="#6FB347" />
        </linearGradient>
      </defs>

      <rect x={0} y={0} width={1920} height={1080} fill="url(#sky)" />

      {/* soft sun, upper-left */}
      <g transform="translate(300 220)">
        <circle cx={0} cy={0} r={170} fill="url(#sunGlow)" />
        <g transform={`rotate(${rayRot})`} opacity={0.5}>
          {Array.from({ length: 12 }).map((_, i) => {
            const a = (i / 12) * Math.PI * 2;
            return (
              <line
                key={i}
                x1={Math.cos(a) * 95}
                y1={Math.sin(a) * 95}
                x2={Math.cos(a) * 125}
                y2={Math.sin(a) * 125}
                stroke="#FCD976"
                strokeWidth={9}
                strokeLinecap="round"
              />
            );
          })}
        </g>
        <circle cx={0} cy={0} r={82} fill="#FCE08A" />
      </g>

      {/* drifting clouds (continuous across whole film) */}
      <Clouds />

      {/* hills */}
      <path d="M0 760 Q480 620 960 720 T1920 700 L1920 1080 L0 1080 Z" fill="#AED98B" />
      <path d="M0 820 Q560 700 1120 800 T1920 790 L1920 1080 L0 1080 Z" fill="#97CC6E" />
      {/* front grass */}
      <rect x={0} y={840} width={1920} height={240} fill="url(#grass)" />
      <path d="M0 850 Q480 820 960 850 T1920 850 L1920 900 L0 900 Z" fill="#9BD06A" opacity={0.6} />

      {/* grass tufts */}
      <GrassRow y={846} />
    </svg>
  );
};

const Clouds: React.FC = () => {
  const frame = useCurrentFrame();
  const cloud = (x0: number, y: number, s: number, speed: number, op = 1) => {
    const x = ((x0 + interpolate(frame, [0, 900], [0, speed])) % 2240) - 160;
    return (
      <g transform={`translate(${x} ${y}) scale(${s})`} opacity={op}>
        <ellipse cx={0} cy={0} rx={70} ry={46} fill="#fff" />
        <ellipse cx={55} cy={12} rx={52} ry={36} fill="#fff" />
        <ellipse cx={-52} cy={14} rx={50} ry={34} fill="#fff" />
        <ellipse cx={4} cy={26} rx={80} ry={30} fill="#fff" />
      </g>
    );
  };
  return (
    <g opacity={0.92}>
      {cloud(250, 170, 1, 180)}
      {cloud(900, 110, 0.7, 130, 0.85)}
      {cloud(1450, 240, 1.15, 220)}
      {cloud(650, 320, 0.55, 100, 0.7)}
    </g>
  );
};

export const GrassRow: React.FC<{ y: number }> = ({ y }) => {
  const frame = useCurrentFrame();
  const sway = Math.sin(frame / 22) * 3;
  return (
    <g stroke="#5FA037" strokeWidth={5} strokeLinecap="round">
      {Array.from({ length: 40 }).map((_, i) => {
        const x = 20 + i * 49;
        const s = (i % 3) - 1;
        return (
          <path key={i} d={`M${x} ${y + 18} Q${x + s * 6 + sway} ${y - 14} ${x + s * 10 + sway} ${y - 2}`} fill="none" />
        );
      })}
    </g>
  );
};

/* ------------------------------------------------------------------ */
/* Flowers (lavender + daisy) — gentle sway                             */
/* ------------------------------------------------------------------ */
export const Lavender: React.FC<{ x: number; y: number; s?: number; phase?: number }> = ({ x, y, s = 1, phase = 0 }) => {
  const frame = useCurrentFrame();
  const sway = Math.sin(frame / 26 + phase) * 4;
  return (
    <g transform={`translate(${x} ${y}) scale(${s})`}>
      <path d={`M0 0 Q${sway} -60 ${sway * 1.4} -110`} stroke="#5FA037" strokeWidth={6} fill="none" strokeLinecap="round" />
      {Array.from({ length: 6 }).map((_, i) => (
        <circle key={i} cx={sway * (1 + i * 0.08)} cy={-60 - i * 12} r={9 - i} fill="#B49AD8" />
      ))}
      <ellipse cx={-12} cy={-26} rx={5} ry={14} fill="#6BAE42" transform={`rotate(-20 -12 -26)`} />
      <ellipse cx={12} cy={-30} rx={5} ry={14} fill="#6BAE42" transform={`rotate(20 12 -30)`} />
    </g>
  );
};

export const Daisy: React.FC<{ x: number; y: number; s?: number; phase?: number }> = ({ x, y, s = 1, phase = 0 }) => {
  const frame = useCurrentFrame();
  const sway = Math.sin(frame / 24 + phase) * 4;
  return (
    <g transform={`translate(${x} ${y}) scale(${s})`}>
      <path d={`M0 0 Q${sway} -50 ${sway * 1.4} -96`} stroke="#5FA037" strokeWidth={6} fill="none" strokeLinecap="round" />
      <g transform={`translate(${sway * 1.4} -100)`}>
        {Array.from({ length: 8 }).map((_, i) => {
          const a = (i / 8) * Math.PI * 2;
          return <ellipse key={i} cx={Math.cos(a) * 16} cy={Math.sin(a) * 16} rx={9} ry={5} fill="#fff" transform={`rotate(${(a * 180) / Math.PI} ${Math.cos(a) * 16} ${Math.sin(a) * 16})`} />;
        })}
        <circle cx={0} cy={0} r={10} fill="#FCD45E" />
      </g>
    </g>
  );
};

/* ------------------------------------------------------------------ */
/* Scene props                                                          */
/* ------------------------------------------------------------------ */
export const OruHouse: React.FC<{ x: number; y: number; s?: number }> = ({ x, y, s = 1 }) => (
  <g transform={`translate(${x} ${y}) scale(${s})`}>
    {/* walls */}
    <rect x={-130} y={-150} width={260} height={170} rx={14} fill="#F3E7CC" stroke="#C9B58A" strokeWidth={5} />
    {/* roof */}
    <path d="M-160 -150 L0 -270 L160 -150 Z" fill="#5C9B3E" stroke="#3C6E28" strokeWidth={6} />
    {/* sprout finial echoing Oru */}
    <g transform="translate(0 -270)">
      <path d="M0 8 Q0 -10 0 -26" stroke="#3C6E28" strokeWidth={6} fill="none" strokeLinecap="round" />
      <path d="M0 -12 Q-18 -14 -22 -34 Q-2 -32 0 -14 Z" fill="#8FD157" stroke="#5E9E32" strokeWidth={2} />
      <path d="M2 -16 Q20 -20 22 -40 Q4 -38 2 -18 Z" fill="#8FD157" stroke="#5E9E32" strokeWidth={2} />
    </g>
    {/* door */}
    <rect x={-34} y={-100} width={68} height={120} rx={32} fill="#A9743F" stroke="#7A4F28" strokeWidth={5} />
    <circle cx={20} cy={-40} r={5} fill="#F3E7CC" />
    {/* round windows */}
    <circle cx={-88} cy={-90} r={26} fill="#CDE8F2" stroke="#C9B58A" strokeWidth={5} />
    <circle cx={88} cy={-90} r={26} fill="#CDE8F2" stroke="#C9B58A" strokeWidth={5} />
    <path d="M-88 -116 L-88 -64 M-114 -90 L-62 -90" stroke="#9FC4D4" strokeWidth={3} />
    <path d="M88 -116 L88 -64 M62 -90 L114 -90" stroke="#9FC4D4" strokeWidth={3} />
  </g>
);

export const WateringCan: React.FC<{ x: number; y: number; s?: number; pour?: number }> = ({ x, y, s = 1, pour = 0 }) => (
  <g transform={`translate(${x} ${y}) scale(${s})`}>
    <g transform={`rotate(${pour * 28})`}>
      <path d="M-30 -20 Q-40 30 -16 40 L34 40 Q48 26 44 -12 Q40 -26 6 -26 Q-22 -26 -30 -20 Z" fill="#8FB8D8" stroke="#3C6E28" strokeWidth={4} />
      <path d="M-2 -22 Q4 -44 30 -40" stroke="#3C6E28" strokeWidth={6} fill="none" />
      <path d="M40 -6 L78 -28 L86 -18 L48 8 Z" fill="#8FB8D8" stroke="#3C6E28" strokeWidth={4} />
      <ellipse cx={86} cy={-24} rx={12} ry={8} fill="#7AA7C8" stroke="#3C6E28" strokeWidth={3} />
    </g>
  </g>
);

export const WaterStream: React.FC<{ x: number; y: number; on: number }> = ({ x, y, on }) => {
  const frame = useCurrentFrame();
  if (on < 0.5) return null;
  return (
    <g transform={`translate(${x} ${y})`} stroke="#7FB8E0" strokeWidth={4} strokeLinecap="round" opacity={0.85}>
      {Array.from({ length: 7 }).map((_, i) => {
        const p = ((frame * 6 + i * 18) % 110) / 110;
        return <line key={i} x1={i * 2} y1={p * 90} x2={i * 2 + 3} y2={p * 90 + 12} />;
      })}
    </g>
  );
};

export const Sprout: React.FC<{ x: number; y: number; grow: number }> = ({ x, y, grow }) => {
  const h = interpolate(grow, [0, 1], [0, 70], { extrapolateRight: "clamp", easing: Easing.out(Easing.cubic) });
  const leaf = interpolate(grow, [0.4, 1], [0, 1], { extrapolateLeft: "clamp", extrapolateRight: "clamp" });
  return (
    <g transform={`translate(${x} ${y})`}>
      <path d={`M0 0 Q0 ${-h / 2} 0 ${-h}`} stroke="#5E9E32" strokeWidth={6} fill="none" strokeLinecap="round" />
      <g transform={`translate(0 ${-h}) scale(${leaf})`}>
        <path d="M0 0 Q-22 -4 -26 -26 Q-4 -24 0 -4 Z" fill="#8FD157" stroke="#5E9E32" strokeWidth={2} />
        <path d="M2 -4 Q22 -10 24 -32 Q4 -28 2 -6 Z" fill="#8FD157" stroke="#5E9E32" strokeWidth={2} />
      </g>
    </g>
  );
};

export const Football: React.FC<{ x: number; y: number; s?: number; roll?: number }> = ({ x, y, s = 1, roll = 0 }) => (
  <g transform={`translate(${x} ${y}) scale(${s}) rotate(${roll})`}>
    <circle cx={0} cy={0} r={40} fill="#fff" stroke="#2E5223" strokeWidth={4} />
    <path d="M0 -16 L15 -5 L9 13 L-9 13 L-15 -5 Z" fill="#2E5223" />
    {Array.from({ length: 5 }).map((_, i) => {
      const a = (i / 5) * Math.PI * 2 - Math.PI / 2;
      return <circle key={i} cx={Math.cos(a) * 34} cy={Math.sin(a) * 34} r={7} fill="#2E5223" />;
    })}
  </g>
);

export const Goal: React.FC<{ x: number; y: number; s?: number }> = ({ x, y, s = 1 }) => (
  <g transform={`translate(${x} ${y}) scale(${s})`} stroke="#fff" fill="none" strokeWidth={6}>
    <rect x={-120} y={-150} width={240} height={150} rx={4} fill="#fff" fillOpacity={0.08} />
    <g stroke="#E8EEE6" strokeWidth={2} opacity={0.85}>
      {Array.from({ length: 9 }).map((_, i) => (
        <line key={"v" + i} x1={-120 + i * 30} y1={-150} x2={-120 + i * 30} y2={0} />
      ))}
      {Array.from({ length: 6 }).map((_, i) => (
        <line key={"h" + i} x1={-120} y1={-150 + i * 30} x2={120} y2={-150 + i * 30} />
      ))}
    </g>
    <path d="M-120 0 L-120 -150 L120 -150 L120 0" stroke="#fff" strokeWidth={7} />
  </g>
);

export const BathTub: React.FC<{ x: number; y: number; s?: number }> = ({ x, y, s = 1 }) => (
  <g transform={`translate(${x} ${y}) scale(${s})`}>
    <ellipse cx={0} cy={70} rx={150} ry={26} fill="#000" opacity={0.12} />
    <path d="M-150 -20 Q-150 70 -90 78 L90 78 Q150 70 150 -20 Z" fill="#FBFAF4" stroke="#C9B58A" strokeWidth={6} />
    <ellipse cx={0} cy={-20} rx={150} ry={32} fill="#EAF6FF" stroke="#C9B58A" strokeWidth={6} />
    {/* water */}
    <ellipse cx={0} cy={-16} rx={134} ry={24} fill="#BFE4F5" />
    {/* little feet */}
    <rect x={-130} y={70} width={20} height={24} rx={8} fill="#C9B58A" />
    <rect x={110} y={70} width={20} height={24} rx={8} fill="#C9B58A" />
  </g>
);

export const Bubbles: React.FC<{ x: number; y: number; on?: number }> = ({ x, y, on = 1 }) => {
  const frame = useCurrentFrame();
  if (on < 0.5) return null;
  return (
    <g transform={`translate(${x} ${y})`}>
      {Array.from({ length: 14 }).map((_, i) => {
        const seed = i * 37;
        const rise = ((frame * 1.4 + seed) % 160);
        const bx = Math.sin((frame + seed) / 30 + i) * 40 + (i - 7) * 18;
        const r = 6 + (i % 4) * 4;
        const op = interpolate(rise, [0, 30, 130, 160], [0, 0.8, 0.8, 0]);
        return <circle key={i} cx={bx} cy={-rise} r={r} fill="#fff" opacity={op} stroke="#CDE8F2" strokeWidth={1.5} />;
      })}
    </g>
  );
};

/** Front rim + water surface of the tub, drawn AFTER Oru so he sits inside it. */
export const BathTubFront: React.FC<{ x: number; y: number; s?: number }> = ({ x, y, s = 1 }) => (
  <g transform={`translate(${x} ${y}) scale(${s})`}>
    <ellipse cx={0} cy={-16} rx={134} ry={22} fill="#BFE4F5" opacity={0.92} />
    <ellipse cx={0} cy={-16} rx={134} ry={22} fill="none" stroke="#8FC4E6" strokeWidth={3} />
    <path d="M-150 -18 Q-150 70 -90 78 L90 78 Q150 70 150 -18 Q150 28 0 28 Q-150 28 -150 -18 Z" fill="#FBFAF4" stroke="#C9B58A" strokeWidth={6} />
  </g>
);

export const Zzz: React.FC<{ x: number; y: number }> = ({ x, y }) => {
  const frame = useCurrentFrame();
  return (
    <g>
      {[0, 1, 2].map((i) => {
        const t = ((frame - i * 28) % 84) / 84;
        if (t < 0) return null;
        const op = Math.sin(Math.PI * t);
        return (
          <text
            key={i}
            x={x + i * 34 + t * 20}
            y={y - t * 90}
            fontFamily="'Baloo 2',sans-serif"
            fontSize={36 + i * 10}
            fontWeight={800}
            fill="#FFF6CF"
            opacity={op}
          >
            z
          </text>
        );
      })}
    </g>
  );
};

export const Bed: React.FC<{ x: number; y: number; s?: number }> = ({ x, y, s = 1 }) => (
  <g transform={`translate(${x} ${y}) scale(${s})`}>
    <ellipse cx={0} cy={70} rx={250} ry={26} fill="#000" opacity={0.12} />
    {/* mattress */}
    <rect x={-240} y={0} width={480} height={70} rx={20} fill="#EADFC6" stroke="#C9B58A" strokeWidth={5} />
    {/* pillow */}
    <rect x={-220} y={-46} width={150} height={70} rx={28} fill="#FBFAF4" stroke="#C9B58A" strokeWidth={5} />
    {/* blanket */}
    <path d="M-40 6 Q120 -30 240 18 L240 64 L-40 64 Z" fill="#AFD8EF" stroke="#7FB8E0" strokeWidth={5} />
    <path d="M-40 24 Q120 -8 240 36" stroke="#8FC4E6" strokeWidth={4} fill="none" />
  </g>
);

export const Moon: React.FC<{ x: number; y: number; s?: number }> = ({ x, y, s = 1 }) => (
  <g transform={`translate(${x} ${y}) scale(${s})`}>
    <circle cx={0} cy={0} r={60} fill="#FDF3C4" />
    <circle cx={22} cy={-8} r={56} fill="#DCEFE3" />
    <circle cx={-18} cy={6} r={9} fill="#F2E7A8" opacity={0.6} />
    <circle cx={2} cy={26} r={6} fill="#F2E7A8" opacity={0.6} />
  </g>
);

export const Stars: React.FC<{ on: number }> = ({ on }) => {
  const frame = useCurrentFrame();
  const pts = [
    [220, 160], [520, 110], [780, 200], [1150, 140], [1500, 110], [1720, 230], [1340, 300], [380, 320], [980, 90],
  ];
  return (
    <g opacity={on}>
      {pts.map(([px, py], i) => {
        const tw = 0.5 + 0.5 * Math.sin(frame / 12 + i);
        return (
          <g key={i} transform={`translate(${px} ${py})`} opacity={tw}>
            <path d="M0 -10 L3 -3 L10 0 L3 3 L0 10 L-3 3 L-10 0 L-3 -3 Z" fill="#FFF6CF" />
          </g>
        );
      })}
    </g>
  );
};

/* BabyOrgano wordmark (vector, brand green) */
export const Wordmark: React.FC<{ x: number; y: number; s?: number }> = ({ x, y, s = 1 }) => (
  <g transform={`translate(${x} ${y}) scale(${s})`} textAnchor="middle">
    <text x={0} y={0} fontFamily="'Baloo 2','Trebuchet MS',sans-serif" fontWeight={800} fontSize={92} fill={BRAND} letterSpacing={2}>
      BABY
    </text>
    <text x={0} y={92} fontFamily="'Baloo 2','Trebuchet MS',sans-serif" fontWeight={800} fontSize={92} fill={BRAND} letterSpacing={2}>
      ORGANO
    </text>
  </g>
);
