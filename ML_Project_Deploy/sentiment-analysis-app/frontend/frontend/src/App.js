import React, { useState } from "react";
import SentimentForm from "./components/SentimentForm";
import SentimentResult from "./components/SentimentResult";

function App() {
  const [sentiment, setSentiment] = useState(null);

  const handleSentiment = (result) => {
    setSentiment(result);
  };

  return (
    <div className="App">
      <h1>Sentiment Analysis</h1>
      <SentimentForm onSentiment={handleSentiment} />
      {sentiment && <SentimentResult sentiment={sentiment} />}
    </div>
  );
}

export default App;
