import "./index.css";
import { Composition } from "remotion";
import { OruWorld } from "./oru/OruWorld";

export const RemotionRoot: React.FC = () => {
  return (
    <>
      <Composition
        id="OruWorld"
        component={OruWorld}
        durationInFrames={900}
        fps={30}
        width={1920}
        height={1080}
      />
    </>
  );
};
