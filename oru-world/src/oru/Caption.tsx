import React from "react";
import { useCurrentFrame, interpolate, Easing, AbsoluteFill } from "remotion";

const FONT = "'Baloo 2','Quicksand','Trebuchet MS','Verdana',sans-serif";

export const Caption: React.FC<{
  title: string;
  sub?: string;
  duration: number;
  position?: "top" | "bottom" | "center";
  color?: string;
}> = ({ title, sub, duration, position = "bottom", color = "#2E6B2E" }) => {
  const frame = useCurrentFrame();
  const inOp = interpolate(frame, [0, 16], [0, 1], { extrapolateRight: "clamp", easing: Easing.out(Easing.cubic) });
  const outOp = interpolate(frame, [duration - 16, duration], [1, 0], { extrapolateLeft: "clamp" });
  const opacity = Math.min(inOp, outOp);
  const rise = interpolate(frame, [0, 18], [26, 0], { extrapolateRight: "clamp", easing: Easing.out(Easing.cubic) });

  const justify = position === "top" ? "flex-start" : position === "center" ? "center" : "flex-end";
  const pad = position === "center" ? 0 : 90;

  return (
    <AbsoluteFill
      style={{
        justifyContent: justify,
        alignItems: "center",
        paddingTop: position === "top" ? pad : 0,
        paddingBottom: position === "bottom" ? pad : 0,
      }}
    >
      <div style={{ opacity, transform: `translateY(${rise}px)`, textAlign: "center" }}>
        <div
          style={{
            fontFamily: FONT,
            fontWeight: 800,
            fontSize: 84,
            color,
            lineHeight: 1.05,
            textShadow: "0 3px 0 rgba(255,255,255,0.85), 0 6px 18px rgba(0,0,0,0.12)",
            WebkitTextStroke: "1px rgba(255,255,255,0.6)",
          }}
        >
          {title}
        </div>
        {sub ? (
          <div
            style={{
              fontFamily: FONT,
              fontWeight: 700,
              fontSize: 44,
              color,
              marginTop: 12,
              textShadow: "0 2px 0 rgba(255,255,255,0.85)",
            }}
          >
            {sub}
          </div>
        ) : null}
      </div>
    </AbsoluteFill>
  );
};
