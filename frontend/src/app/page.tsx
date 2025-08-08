"use client";

import { useState } from "react";
import {
  ConversationEntry,
  SummaryResponse,
  SummaryType,
} from "@/types/summary";
import { summarizeText } from "@/lib/api";
import { API_URL } from "@/lib/config";

export default function Home() {
  const [text, setText] = useState("");
  const [summaryType, setSummaryType] = useState<SummaryType>("medium");
  const [loading, setLoading] = useState(false);
  const [history, setHistory] = useState<ConversationEntry[]>([]);

  async function handleSummarize() {
    if (!text || text.trim().length < 10) {
      alert("Please enter at least 10 characters.");
      return;
    }

    setLoading(true);
    const id = crypto.randomUUID();
    try {
      const data: SummaryResponse = await summarizeText({ text, summaryType });
      setHistory((prev) => [
        { id, text, summaryType, response: data },
        ...prev,
      ]);
    } catch (e) {
      const message = e instanceof Error ? e.message : "Network error";
      setHistory((prev) => [
        { id, text, summaryType, error: message },
        ...prev,
      ]);
    } finally {
      setLoading(false);
    }
  }

  function handleNewChat() {
    setText("");
    setSummaryType("medium");
    setHistory([]);
  }

  return (
    <div className="min-h-screen w-full bg-background text-foreground">
      <div className="mx-auto max-w-3xl px-4 py-10">
        <header className="mb-8 flex items-center justify-between">
          <h1 className="text-2xl font-semibold tracking-tight">
            Text Summarizer
          </h1>
          <button
            onClick={handleNewChat}
            className="rounded-md border px-3 py-2 text-sm font-medium hover:bg-muted"
          >
            New chat
          </button>
        </header>

        <section className="mb-8 space-y-4">
          <div>
            <label
              htmlFor="summary-type"
              className="mb-2 block text-sm font-medium"
            >
              Summary size
            </label>
            <select
              id="summary-type"
              value={summaryType}
              onChange={(e) => setSummaryType(e.target.value as SummaryType)}
              className="w-full rounded-md border bg-background px-3 py-2 text-sm focus:outline-none"
            >
              <option value="small">Small</option>
              <option value="medium">Medium</option>
              <option value="large">Large</option>
            </select>
          </div>

          <div>
            <label
              htmlFor="input-text"
              className="mb-2 block text-sm font-medium"
            >
              Paste your text
            </label>
            <textarea
              id="input-text"
              value={text}
              onChange={(e) => setText(e.target.value)}
              placeholder="Paste your text here (at least 10 characters)"
              rows={8}
              className="w-full resize-y rounded-md border bg-background px-3 py-2 text-sm leading-6 focus:outline-none"
            />
          </div>

          <div className="flex items-center gap-3">
            <button
              onClick={handleSummarize}
              disabled={loading}
              className="rounded-md bg-foreground px-4 py-2 text-sm font-medium text-background hover:opacity-90 disabled:opacity-50"
            >
              {loading ? "Summarizing..." : "Summarize"}
            </button>
            <span className="text-xs text-muted-foreground">
              Backend: {API_URL.replace(/https?:\/\//, "")}
            </span>
          </div>
        </section>

        <section className="space-y-4">
          {history.length === 0 ? (
            <p className="text-sm text-muted-foreground">
              No messages yet. Submit a summary to get started.
            </p>
          ) : (
            history.map((entry) => (
              <div key={entry.id} className="rounded-md border p-4">
                <div className="mb-2 flex items-center justify-between gap-2">
                  <span className="text-xs uppercase tracking-wide text-muted-foreground">
                    Request
                  </span>
                  <span className="text-xs text-muted-foreground">
                    Type: {entry.summaryType}
                  </span>
                </div>
                <p className="whitespace-pre-wrap text-sm">{entry.text}</p>
                <div className="my-3 h-px w-full bg-border" />
                {entry.error ? (
                  <div>
                    <div className="mb-1 text-xs uppercase tracking-wide text-red-600">
                      Error
                    </div>
                    <p className="text-sm text-red-600">{entry.error}</p>
                  </div>
                ) : entry.response ? (
                  <div>
                    <div className="mb-1 text-xs uppercase tracking-wide text-muted-foreground">
                      Summary
                    </div>
                    <p className="whitespace-pre-wrap text-sm">
                      {entry.response.summary}
                    </p>
                    <div className="mt-2 text-xs text-muted-foreground">
                      Words: {entry.response.word_count}
                    </div>
                  </div>
                ) : null}
              </div>
            ))
          )}
        </section>
      </div>
    </div>
  );
}
