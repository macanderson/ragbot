import { useState } from "react";

export default function Home() {
  const [question, setQuestion] = useState("");
  const [answer, setAnswer] = useState("");

  const ask = async () => {
    const res = await fetch("process.env.NEXT_PUBLIC_API_URL", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ question }),
    });
    const data = await res.json();
    setAnswer(data.answer);
  };

  return (
    <div className="flex flex-col items-center justify-center h-screen">
      <h1 className="text-2xl font-bold">RAG Bot</h1>
      <input
        className="border-2 border-gray-300 rounded-md p-2"
        value={question}
        onChange={(e) => setQuestion(e.target.value)}
      />
      <button className="bg-blue-500 text-white p-2 rounded-md" onClick={ask}>
        Ask
      </button>
      <p className="text-lg">{answer}</p>
    </div>
  );
}
