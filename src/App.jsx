import React, { memo } from 'react';

// We use memo to keep the render smooth and fast
const ModelStage = memo(({ modelImage, modelName }) => (
  <div className="main-stage">
    {/* This is the container that 'grounds' her to the floor */}
    <div className="runway-path">
      <img 
        src={modelImage} 
        className="realist-model" 
        alt={modelName} 
      />
      
      {/* Visual FX Layers: These add the 'Virtually Realistic' lighting */}
      <div className="bridge-ambient-glow"></div>
      <div className="engine-glow"></div>
    </div>

    {/* HUD Overlay */}
    <div className="ui-overlay">
      <h3>{modelName}</h3>
      <p>STATUS: ACTIVE // SECTOR: STARSHIP BRIDGE</p>
    </div>
  </div>
));

export default function App() {
  return (
    <div className="starship-main">
      {/* Pointing to your Red Demon Girl image in the public folder */}
      <ModelStage modelImage="/model_a.png" modelName="RED DEMON GIRL" />
    </div>
  );
}
