import React, { useState } from "react";

function SentimentForm({ onSentiment }) {
  const [review, setReview] = useState("");

  const handleSubmit = async (e) => {
    e.preventDefault();
    const response = await fetch("http://127.0.0.1:5000/predict", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ review }),
    });
    const data = await response.json();
    onSentiment(data.sentiment);
  };

  return (
    <form onSubmit={handleSubmit}>
      <textarea value={review} onChange={(e) => setReview(e.target.value)} />
      <button type="submit">Analyze</button>
    </form>
  );
}

export default SentimentForm;
