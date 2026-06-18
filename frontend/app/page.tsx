"use client";

import { useState } from "react";

export default function Home() {

  const [companyName, setCompanyName] = useState("");

  const handleAnalyze = async () => {

    const response = await fetch(
      "http://localhost:8000/analyze",
      {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          company_name: companyName,
        }),
      }
    );

    const data = await response.json();

    console.log(data);

    const blob = new Blob(
      [data.report],
      {
        type: "text/markdown",
      }
    );

    const url = URL.createObjectURL(blob);

    const a = document.createElement("a");

    a.href = url;
    a.download = `${companyName}.md`;

    a.click();

    URL.revokeObjectURL(url);
  };   // <-- tutup handleAnalyze di sini

  return (
    <main className="min-h-screen flex flex-col items-center justify-center gap-6">

      <h1 className="text-4xl font-bold">
        Market Intelligence AI
      </h1>

      <input
        className="border rounded-lg p-3 w-96"
        placeholder="PT Indosat"
        value={companyName}
        onChange={(e) => setCompanyName(e.target.value)}
      />

      <button
        className="bg-blue-600 text-white px-6 py-3 rounded-lg"
        onClick={handleAnalyze}
      >
        Analyze
      </button>

    </main>
  );
}