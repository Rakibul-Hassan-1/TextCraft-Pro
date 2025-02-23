// src/components/AlgorithmList.js
import React from "react";

const AlgorithmList = ({ algorithms, onSelect }) => {
  return (
    <div>
      <h3>Select an Algorithm</h3>
      <ul>
        {algorithms.map((algorithm, index) => (
          <li key={index} onClick={() => onSelect(algorithm)}>
            {algorithm}
          </li>
        ))}
      </ul>
    </div>
  );
};

export default AlgorithmList;
