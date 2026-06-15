import requests

def generate_response(question):

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "llama3",
            "prompt": question,
            "stream": False
        }
    )

    data = response.json()

    return data["response"]


if __name__ == "__main__":
    answer = generate_response(
        "What is FastAPI?"
    )
    print(answer)