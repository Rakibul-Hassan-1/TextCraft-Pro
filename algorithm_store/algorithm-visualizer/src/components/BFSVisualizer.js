import React, { useEffect, useState } from "react";
import "./Visualizer.css";

const BFSVisualizer = () => {
  // Initialize state
  const [visited, setVisited] = useState([]);
  const [queue, setQueue] = useState([]);
  const [isRunning, setIsRunning] = useState(false);
  const [steps, setSteps] = useState([]);
  const [stepIndex, setStepIndex] = useState(0);
  const [bfsPath, setBfsPath] = useState([]); // To store the BFS path

  const nodes = [
    { id: 1, label: "A", x: 200, y: 100 },
    { id: 2, label: "B", x: 100, y: 200 },
    { id: 3, label: "C", x: 300, y: 200 },
    { id: 4, label: "D", x: 100, y: 300 },
    { id: 5, label: "E", x: 300, y: 300 },
  ];

  const edges = [
    { from: 1, to: 2 },
    { from: 1, to: 3 },
    { from: 2, to: 4 },
    { from: 2, to: 5 },
    { from: 3, to: 5 },
  ];

  // BFS function logic
  const bfs = (startNode) => {
    const visitedNodes = [startNode];
    const queueNodes = [startNode];
    let stepsList = [[startNode]];
    let path = [startNode]; // Track BFS path

    while (queueNodes.length > 0) {
      const node = queueNodes.shift();
      const neighbors = edges
        .filter((edge) => edge.from === node)
        .map((edge) => edge.to);

      neighbors.forEach((neighbor) => {
        if (!visitedNodes.includes(neighbor)) {
          visitedNodes.push(neighbor);
          queueNodes.push(neighbor);
          path.push(neighbor); // Add to BFS path
        }
      });

      stepsList.push([...queueNodes]);
    }

    return { stepsList, path };
  };

  const handleStart = (startNode) => {
    setIsRunning(true);
    const { stepsList, path } = bfs(startNode); // Start BFS from selected node
    setSteps(stepsList);
    setBfsPath(path); // Save BFS path
    setVisited([startNode]);
    setQueue([startNode]);
    setStepIndex(0);
  };

  const handleNodeClick = (nodeId) => {
    if (!isRunning) {
      handleStart(nodeId);
    }
  };

  // Update state step by step after BFS starts
  useEffect(() => {
    if (isRunning && steps.length > 0 && stepIndex < steps.length) {
      const interval = setInterval(() => {
        setVisited(steps[stepIndex]);
        setQueue(steps[stepIndex + 1] || []);
        setStepIndex((prevIndex) => prevIndex + 1);

        if (stepIndex >= steps.length - 1) {
          clearInterval(interval);
          setIsRunning(false);
        }
      }, 1000);

      return () => clearInterval(interval);
    }
  }, [isRunning, stepIndex, steps]);

  return (
    <div className="visualizer">
      <h2 className="algorithm-title">BFS Visualization</h2>
      <div className="graph-container">
        {edges.map((edge, idx) => (
          <line
            key={idx}
            x1={nodes.find((node) => node.id === edge.from).x}
            y1={nodes.find((node) => node.id === edge.from).y}
            x2={nodes.find((node) => node.id === edge.to).x}
            y2={nodes.find((node) => node.id === edge.to).y}
            stroke="#61dafb"
            strokeWidth="2"
          />
        ))}
        {nodes.map((node) => (
          <div
            key={node.id}
            className={`node ${visited.includes(node.id) ? "visited" : ""} ${
              queue.includes(node.id) ? "highlight" : ""
            }`}
            style={{ left: node.x, top: node.y }}
            onClick={() => handleNodeClick(node.id)}
          >
            {node.label}
          </div>
        ))}
      </div>
      <div className="controls">
        <button onClick={() => handleStart(1)} disabled={isRunning}>
          {isRunning ? "Running..." : "Start BFS from A"}
        </button>
      </div>
      {isRunning && <div className="statistics">Running BFS...</div>}
      {/* Display BFS Path */}
      {!isRunning && bfsPath.length > 0 && (
        <div className="statistics">
          <h3>BFS Path:</h3>
          <p>{bfsPath.join(" -> ")}</p>
        </div>
      )}
    </div>
  );
};

export default BFSVisualizer;
