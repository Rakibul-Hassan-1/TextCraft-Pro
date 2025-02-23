import React from "react";
import "./App.css"; // Make sure this is imported if you're using a separate CSS file
import MessageList from "./MessageList"; // Ensure the path is correct

function App() {
  return (
    <div className="App">
      <MessageList />
    </div>
  );
}

export default App;
