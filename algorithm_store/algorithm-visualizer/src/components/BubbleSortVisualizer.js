// src/components/BubbleSortVisualizer.js
import React, { useEffect, useRef, useState } from "react";
import "./Visualizer.css";

const BubbleSortVisualizer = () => {
  const [array, setArray] = useState([5, 3, 8, 4, 2]);
  const [isRunning, setIsRunning] = useState(false);
  const [comparisons, setComparisons] = useState(0);
  const [swaps, setSwaps] = useState(0);
  const [steps, setSteps] = useState([]);
  const [currentStep, setCurrentStep] = useState(0);
  const intervalRef = useRef();

  const bubbleSort = (arr) => {
    const newArr = [...arr];
    const len = newArr.length;
    let comparisonsCount = 0;
    let swapsCount = 0;
    let stepsArray = [];

    for (let i = 0; i < len; i++) {
      for (let j = 0; j < len - 1 - i; j++) {
        comparisonsCount++;
        if (newArr[j] > newArr[j + 1]) {
          swapsCount++;
          [newArr[j], newArr[j + 1]] = [newArr[j + 1], newArr[j]];
        }
        stepsArray.push([...newArr]); // Capture each step
      }
    }

    setComparisons(comparisonsCount);
    setSwaps(swapsCount);
    return stepsArray;
  };

  const handleStart = () => {
    setIsRunning(true);
    const stepsArray = bubbleSort(array);
    setSteps(stepsArray);
  };

  const handlePause = () => {
    setIsRunning(false);
    if (intervalRef.current) {
      clearInterval(intervalRef.current);
    }
  };

  const handleResume = () => {
    setIsRunning(true);
    intervalRef.current = setInterval(() => {
      if (currentStep < steps.length) {
        setArray(steps[currentStep]);
        setCurrentStep(currentStep + 1);
      } else {
        clearInterval(intervalRef.current);
      }
    }, 500);
  };

  const handleStepForward = () => {
    if (currentStep < steps.length) {
      setArray(steps[currentStep]);
      setCurrentStep(currentStep + 1);
    }
  };

  useEffect(() => {
    if (isRunning && steps.length) {
      handleResume();
    }
  }, [isRunning, steps]);

  return (
    <div className="visualizer">
      <h2 className="algorithm-title">Bubble Sort Visualization</h2>
      <div className="array-container">
        {array.map((num, index) => (
          <div
            key={index}
            className="array-bar"
            style={{ height: `${num * 30}px`, width: "30px", margin: "5px" }}
          ></div>
        ))}
      </div>
      <div className="controls">
        <button onClick={handleStart} disabled={isRunning}>
          Start
        </button>
        <button onClick={handlePause} disabled={!isRunning}>
          Pause
        </button>
        <button onClick={handleResume} disabled={isRunning}>
          Resume
        </button>
        <button onClick={handleStepForward} disabled={isRunning}>
          Step Forward
        </button>
      </div>
      <div className="statistics">
        <p>Comparisons: {comparisons}</p>
        <p>Swaps: {swaps}</p>
      </div>
    </div>
  );
};

export default BubbleSortVisualizer;
