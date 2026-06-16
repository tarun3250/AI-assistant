import { useState } from "react";

function App() {

  const [question, setQuestion] = useState("");
  const [answer, setAnswer] = useState("");

  return (
    <div>
      <h1>AI Knowledge Assistant</h1>

      <input
        type="text"
        placeholder="Ask a question..."
        value={question}
        onChange={(e) => setQuestion(e.target.value)}
      />
      
      <button>
        Ask
      </button>

      <h3>Response:</h3>
      <p>{answer}</p>

    </div>
  );
}

export default App;