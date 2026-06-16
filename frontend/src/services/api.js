const BASE_URL = "http://127.0.0.1:8000";

export async function askQuestion(question) {
  const response = await fetch(
    `${BASE_URL}/ask`,
    {
      method: "POST",

      headers: {
        "Content-Type": "application/json",
      },

      body: JSON.stringify({
        question: question,
      }),
    }
  );

  return response.json();
}

export async function getHistory() {
  const response = await fetch(
    `${BASE_URL}/history`
  );

  return response.json();
}

export async function clearHistory() {

    const response = await fetch(
      `${BASE_URL}/history`,
      {
        method: "DELETE"
      }
    );
  
    return response.json();
  }