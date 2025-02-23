// src/components/QuickSortVisualizer.js
import React, { useEffect, useState } from "react";
import "./Visualizer.css";

const QuickSortVisualizer = () => {
  const [array, setArray] = useState([5, 3, 8, 4, 2]);
  const [isRunning, setIsRunning] = useState(false);
  const [steps, setSteps] = useState([]);
  const [currentStep, setCurrentStep] = useState(0);

  const quickSort = (arr, low, high, stepsArray) => {
    if (low < high) {
      let pi = partition(arr, low, high, stepsArray);
      quickSort(arr, low, pi - 1, stepsArray);
      quickSort(arr, pi + 1, high, stepsArray);
    }
  };

  const partition = (arr, low, high, stepsArray) => {
    let pivot = arr[high];
    let i = low - 1;
    for (let j = low; j < high; j++) {
      if (arr[j] <= pivot) {
        i++;
        [arr[i], arr[j]] = [arr[j], arr[i]];
        stepsArray.push([...arr]);
      }
    }
    [arr[i + 1], arr[high]] = [arr[high], arr[i + 1]];
    stepsArray.push([...arr]);
    return i + 1;
  };

  const handleStart = () => {
    const stepsArray = [];
    quickSort([...array], 0, array.length - 1, stepsArray);
    setSteps(stepsArray);
    setIsRunning(true);
  };

  useEffect(() => {
    if (isRunning && currentStep < steps.length) {
      setArray(steps[currentStep]);
      setCurrentStep(currentStep + 1);
    }
  }, [isRunning, currentStep, steps]);

  return (
    <div className="visualizer">
      <h2 className="algorithm-title">Quick Sort Visualization</h2>
      <div className="array-container">
        {array.map((num, index) => (
          <div
            key={index}
            className="array-bar"
            style={{
              height: `${num * 30}px`,
              width: "30px",
              margin: "5px",
              backgroundColor: currentStep === index ? "#FF6347" : "#61dafb",
            }}
          ></div>
        ))}
      </div>
      <div className="controls">
        <button onClick={handleStart} disabled={isRunning}>
          Start
        </button>
      </div>
    </div>
  );
};

export default QuickSortVisualizer;
