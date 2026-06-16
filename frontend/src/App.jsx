import { useState } from "react";

import {
  askQuestion,
  getHistory,
  clearHistory,
} from "./services/api";

function App() {
  const [question, setQuestion] = useState("");
  const [answer, setAnswer] = useState("");
  const [history, setHistory] = useState([]);

  const handleAsk = async () => {
    if (!question.trim()) {
      alert("Please enter a question");
      return;
    }

    const data = await askQuestion(question);

    setAnswer(data.answer);
    setQuestion("");
  };

  const handleLoadHistory = async () => {
    const data = await getHistory();

    setHistory(data.history);
  };

  const handleClearHistory = async () => {
    await clearHistory();

    setHistory([]);
    setAnswer("");

    alert("History cleared successfully");
  };

  return (
    <div
      style={{
        maxWidth: "1000px",
        margin: "0 auto",
        padding: "20px",
      }}
    >
      <h1>AI Knowledge Assistant</h1>

      <div style={{ marginBottom: "20px" }}>
        <input
          type="text"
          placeholder="Ask a question..."
          value={question}
          onChange={(e) => setQuestion(e.target.value)}
          style={{
            width: "70%",
            padding: "10px",
            marginRight: "10px",
          }}
        />

        <button onClick={handleAsk}>
          Ask
        </button>

        <button
          onClick={handleLoadHistory}
          style={{ marginLeft: "10px" }}
        >
          Load History
        </button>

        <button
          onClick={handleClearHistory}
          style={{ marginLeft: "10px" }}
        >
          Clear History
        </button>
      </div>

      <h2>Response</h2>

      <div
        style={{
          border: "1px solid #ccc",
          padding: "15px",
          borderRadius: "8px",
          marginBottom: "30px",
        }}
      >
        {answer ? answer : "No response yet"}
      </div>

      <h2>Chat History</h2>

      {history.length === 0 ? (
        <p>No chat history available</p>
      ) : (
        history.map((chat, index) => (
          <div
            key={index}
            style={{
              border: "1px solid #ccc",
              padding: "15px",
              borderRadius: "8px",
              marginBottom: "15px",
            }}
          >
            <p>
              <strong>Question:</strong>
              <br />
              {chat[1]}
            </p>

            <p>
              <strong>Answer:</strong>
              <br />
              {chat[2]}
            </p>
          </div>
        ))
      )}
    </div>
  );
}

export default App;