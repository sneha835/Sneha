import React from "react";

/**
 * ORU — BabyOrgano mascot. Parametric front-facing vector rig.
 * Drawn in a local 240 x 300 space (feet ~ y=292, head center ~ y=92).
 * Place inside a full-frame <svg> via the x/y/scale/flip props.
 */

export const ORU = {
  skin: "#7CB342",
  skinD: "#5E9E32",
  skinL: "#93C957",
  outline: "#2E5223",
  belly: "#F5F2E4",
  bellyEdge: "#E4DEC7",
  shell: "#4C8A33",
  shellD: "#3C6E28",
  sprout: "#8FD157",
  stem: "#5E9E32",
  glass: "#34601F",
  cheek: "#F2A6A6",
  mouth: "#7A3B2E",
  tongue: "#EF9A9A",
  eye: "#23351A",
};

type Props = {
  x?: number;
  y?: number;
  scale?: number;
  flip?: boolean;
  /** 0 = happy closed crescents, 1 = round open eyes */
  eyeOpen?: number;
  /** 0 = gentle smile, 1 = open happy mouth */
  mouthOpen?: number;
  /** 0..1 raise of right arm into a wave */
  wave?: number;
  /** 0..1 running leg pose (one fwd, one back) */
  run?: number;
  /** blink amount 0..1 (squashes eyes) */
  blink?: number;
  /** lean degrees (forward lean for running) */
  lean?: number;
  /** sleeping: closed peaceful eyes + relaxed */
  asleep?: boolean;
};

const O = ORU;

export const Oru: React.FC<Props> = ({
  x = 0,
  y = 0,
  scale = 1,
  flip = false,
  eyeOpen = 0,
  mouthOpen = 0,
  wave = 0,
  run = 0,
  blink = 0,
  lean = 0,
  asleep = false,
}) => {
  const sw = 6; // outline weight
  const eo = asleep ? 0 : eyeOpen;
  const eyeSquash = 1 - blink * 0.9;

  // running leg offsets
  const legFwd = run * 24;
  const legUp = run * 6;

  return (
    <g transform={`translate(${x} ${y}) scale(${flip ? -scale : scale} ${scale})`}>
      <g transform={`rotate(${lean})`}>
        {/* soft contact shadow */}
        <ellipse cx={0} cy={150} rx={70} ry={14} fill="#3C6E28" opacity={0.18} />

        {/* ---- SHELL behind body (peeks on his right/back) ---- */}
        <g>
          <ellipse cx={34} cy={70} rx={52} ry={62} fill={O.shellD} />
          <ellipse cx={30} cy={70} rx={46} ry={56} fill={O.shell} />
          {/* shell plates */}
          <path
            d="M30 24 L30 116 M-6 70 Q30 56 66 70 M-2 44 Q30 34 62 44 M-2 96 Q30 86 62 96"
            stroke={O.shellD}
            strokeWidth={3}
            fill="none"
            opacity={0.6}
          />
        </g>

        {/* ---- LEGS ---- */}
        <g>
          {/* back leg (swings back when running) */}
          <g transform={`translate(${-22 - legFwd} ${130 - legUp})`}>
            <g transform={`rotate(${run * 42})`}>
              <ellipse cx={0} cy={6} rx={17} ry={20} fill={O.skinD} stroke={O.outline} strokeWidth={sw} />
              <ellipse cx={-2} cy={22} rx={18} ry={9} fill={O.skinL} stroke={O.outline} strokeWidth={sw} />
            </g>
          </g>
          {/* front leg (kicks forward when running) */}
          <g transform={`translate(${22 + legFwd} 130)`}>
            <g transform={`rotate(${run * -48})`}>
              <ellipse cx={0} cy={6} rx={17} ry={20} fill={O.skin} stroke={O.outline} strokeWidth={sw} />
              <ellipse cx={2} cy={22} rx={18} ry={9} fill={O.skinL} stroke={O.outline} strokeWidth={sw} />
            </g>
          </g>
        </g>

        {/* ---- BODY ---- */}
        <g>
          <path
            d="M-46 64 Q-54 138 -28 150 Q0 160 28 150 Q54 138 46 64 Q40 18 0 18 Q-40 18 -46 64 Z"
            fill={O.skin}
            stroke={O.outline}
            strokeWidth={sw}
          />
          {/* cream belly */}
          <ellipse cx={0} cy={96} rx={32} ry={42} fill={O.belly} stroke={O.bellyEdge} strokeWidth={3} />
        </g>

        {/* ---- ARMS ---- */}
        <g>
          {/* left arm (his left / screen right when not flipped) - relaxed */}
          <g transform="translate(-42 78) rotate(18)">
            <rect x={-12} y={-10} width={26} height={40} rx={13} fill={O.skinD} stroke={O.outline} strokeWidth={sw} />
            <circle cx={0} cy={30} r={12} fill={O.skinL} stroke={O.outline} strokeWidth={sw} />
          </g>
          {/* right arm - can raise into a wave */}
          <g transform={`translate(42 78) rotate(${-18 - wave * 150})`}>
            <rect x={-13} y={-10} width={26} height={42} rx={13} fill={O.skin} stroke={O.outline} strokeWidth={sw} />
            <circle cx={0} cy={32} r={13} fill={O.skinL} stroke={O.outline} strokeWidth={sw} />
          </g>
        </g>

        {/* ---- HEAD ---- */}
        <g transform="translate(0 16)">
          {/* sprout */}
          <g transform="translate(0 -78)">
            <path d="M0 18 Q0 -6 0 -22" stroke={O.stem} strokeWidth={7} fill="none" strokeLinecap="round" />
            <path d="M0 -8 Q-26 -10 -30 -34 Q-6 -34 0 -10 Z" fill={O.sprout} stroke={O.stem} strokeWidth={3} />
            <path d="M2 -14 Q26 -18 30 -42 Q6 -40 2 -16 Z" fill={O.sprout} stroke={O.stem} strokeWidth={3} />
          </g>

          {/* head shape */}
          <ellipse cx={0} cy={-58} rx={66} ry={60} fill={O.skin} stroke={O.outline} strokeWidth={sw} />
          {/* crown spots */}
          <g fill={O.skinD} opacity={0.85}>
            <ellipse cx={-22} cy={-96} rx={9} ry={6} />
            <ellipse cx={-2} cy={-104} rx={8} ry={6} />
            <ellipse cx={20} cy={-98} rx={9} ry={6} />
            <ellipse cx={36} cy={-86} rx={7} ry={5} />
            <ellipse cx={-40} cy={-82} rx={7} ry={5} />
          </g>

          {/* cheeks */}
          <ellipse cx={-40} cy={-44} rx={11} ry={8} fill={O.cheek} opacity={0.75} />
          <ellipse cx={40} cy={-44} rx={11} ry={8} fill={O.cheek} opacity={0.75} />

          {/* glasses */}
          <g stroke={O.glass} strokeWidth={6} fill="none">
            <circle cx={-24} cy={-58} r={22} fill="#FFFFFF" fillOpacity={0.18} />
            <circle cx={24} cy={-58} r={22} fill="#FFFFFF" fillOpacity={0.18} />
            <path d="M-2 -58 Q0 -64 2 -58" />
            <path d="M-46 -62 Q-58 -64 -60 -58" strokeLinecap="round" />
            <path d="M46 -62 Q58 -64 60 -58" strokeLinecap="round" />
          </g>

          {/* eyes */}
          <g>
            {eo < 0.5 ? (
              <g
                stroke={O.eye}
                strokeWidth={5}
                fill="none"
                strokeLinecap="round"
                transform={`translate(0 -58) scale(1 ${eyeSquash})`}
              >
                {/* happy closed crescents (smiling eyes) */}
                <path d="M-34 0 Q-24 -12 -14 0" />
                <path d="M14 0 Q24 -12 34 0" />
              </g>
            ) : (
              <g transform={`translate(0 -58) scale(1 ${eyeSquash})`}>
                <circle cx={-24} cy={-2} r={9} fill={O.eye} />
                <circle cx={24} cy={-2} r={9} fill={O.eye} />
                <circle cx={-21} cy={-5} r={3} fill="#fff" />
                <circle cx={27} cy={-5} r={3} fill="#fff" />
              </g>
            )}
          </g>

          {/* mouth */}
          {mouthOpen < 0.5 ? (
            <path
              d="M-16 -30 Q0 -16 16 -30"
              stroke={O.mouth}
              strokeWidth={5}
              fill="none"
              strokeLinecap="round"
            />
          ) : (
            <g>
              <path d="M-17 -32 Q0 -34 17 -32 Q14 -10 0 -10 Q-14 -10 -17 -32 Z" fill={O.mouth} />
              <ellipse cx={0} cy={-15} rx={9} ry={6} fill={O.tongue} />
            </g>
          )}
        </g>
      </g>
    </g>
  );
};

/** Sleeping pose — lying down, peaceful. Local space ~ 320 wide. */
export const OruSleeping: React.FC<{ x?: number; y?: number; scale?: number; breathe?: number }> = ({
  x = 0,
  y = 0,
  scale = 1,
  breathe = 0,
}) => {
  const sw = 6;
  return (
    <g transform={`translate(${x} ${y}) scale(${scale})`}>
      {/* shell as a rounded back, lying */}
      <g transform={`scale(1 ${1 + breathe * 0.03})`}>
        <ellipse cx={70} cy={10} rx={92} ry={56} fill={ORU.shell} stroke={ORU.outline} strokeWidth={sw} />
        <path
          d="M70 -46 L70 66 M-6 10 Q70 -6 146 10 M2 -22 Q70 -36 138 -22 M2 42 Q70 28 138 42"
          stroke={ORU.shellD}
          strokeWidth={3}
          fill="none"
          opacity={0.55}
        />
      </g>
      {/* head resting on pillow */}
      <g transform="translate(-58 -2)">
        <ellipse cx={0} cy={0} rx={54} ry={50} fill={ORU.skin} stroke={ORU.outline} strokeWidth={sw} />
        {/* sprout flopped */}
        <g transform="translate(-6 -44) rotate(-24)">
          <path d="M0 14 Q0 -4 0 -16" stroke={ORU.stem} strokeWidth={6} fill="none" strokeLinecap="round" />
          <path d="M0 -6 Q-20 -8 -24 -26 Q-4 -26 0 -8 Z" fill={ORU.sprout} stroke={ORU.stem} strokeWidth={3} />
          <path d="M2 -10 Q22 -14 24 -32 Q4 -30 2 -12 Z" fill={ORU.sprout} stroke={ORU.stem} strokeWidth={3} />
        </g>
        {/* spots */}
        <g fill={ORU.skinD} opacity={0.8}>
          <ellipse cx={-14} cy={-34} rx={7} ry={5} />
          <ellipse cx={6} cy={-40} rx={7} ry={5} />
          <ellipse cx={24} cy={-32} rx={6} ry={4} />
        </g>
        {/* glasses (resting) */}
        <g stroke={ORU.glass} strokeWidth={5} fill="none">
          <circle cx={-16} cy={4} r={17} fill="#fff" fillOpacity={0.18} />
          <circle cx={20} cy={4} r={17} fill="#fff" fillOpacity={0.18} />
          <path d="M1 4 Q3 -1 5 4" />
        </g>
        {/* peaceful closed eyes */}
        <g stroke={ORU.eye} strokeWidth={4} fill="none" strokeLinecap="round">
          <path d="M-26 6 Q-16 -4 -6 6" />
          <path d="M10 6 Q20 -4 30 6" />
        </g>
        {/* tiny content mouth */}
        <path d="M-6 22 Q2 28 10 22" stroke={ORU.mouth} strokeWidth={4} fill="none" strokeLinecap="round" />
        {/* blush */}
        <ellipse cx={-30} cy={16} rx={8} ry={6} fill={ORU.cheek} opacity={0.7} />
        <ellipse cx={34} cy={16} rx={8} ry={6} fill={ORU.cheek} opacity={0.7} />
      </g>
    </g>
  );
};
