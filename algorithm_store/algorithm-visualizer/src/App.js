// src/App.js
import React, { useState } from "react";
import "./App.css";
import AlgorithmList from "./components/AlgorithmList";
import BFSVisualizer from "./components/BFSVisualizer";
import BubbleSortVisualizer from "./components/BubbleSortVisualizer";
import QuickSortVisualizer from "./components/QuickSortVisualizer";

const App = () => {
  const [selectedAlgorithm, setSelectedAlgorithm] = useState(null);

  // List of algorithms
  const algorithms = ["Bubble Sort", "Quick Sort", "BFS"];

  // Handle algorithm selection
  const handleSelect = (algorithm) => {
    setSelectedAlgorithm(algorithm);
  };

  return (
    <div className="app-container">
      <div className="sidebar">
        <h1 className="title">Algorithm Visualizer</h1>
        <AlgorithmList algorithms={algorithms} onSelect={handleSelect} />
      </div>
      <div className="visualizer-container">
        {/* Render selected algorithm */}
        {selectedAlgorithm === "Bubble Sort" && <BubbleSortVisualizer />}
        {selectedAlgorithm === "Quick Sort" && <QuickSortVisualizer />}
        {selectedAlgorithm === "BFS" && <BFSVisualizer />}
      </div>
    </div>
  );
};

export default App;
