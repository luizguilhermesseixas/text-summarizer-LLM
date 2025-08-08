import { API_URL } from "@/lib/config";
import { SummaryResponse, SummaryType } from "@/types/summary";

type BackendSummaryResponsePT = {
  original_text: string;
  summary_type: "pequeno" | "medio" | "grande";
  summary: string;
  word_count: number;
};

const mapEnToPt: Record<SummaryType, BackendSummaryResponsePT["summary_type"]> =
  {
    small: "pequeno",
    medium: "medio",
    large: "grande",
  };

const mapPtToEn: Record<BackendSummaryResponsePT["summary_type"], SummaryType> =
  {
    pequeno: "small",
    medio: "medium",
    grande: "large",
  };

export async function summarizeText(params: {
  text: string;
  summaryType: SummaryType;
}): Promise<SummaryResponse> {
  const res = await fetch(`${API_URL}/api/v1/summarize`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      text: params.text,
      summary_type: mapEnToPt[params.summaryType],
    }),
  });

  if (!res.ok) {
    const err = await res.json().catch(() => ({} as { detail?: unknown }));
    const message =
      typeof err?.detail === "string"
        ? err.detail
        : JSON.stringify(err?.detail ?? "Unexpected error");
    throw new Error(message);
  }

  const data = (await res.json()) as BackendSummaryResponsePT;
  const mapped: SummaryResponse = {
    original_text: data.original_text,
    summary_type: mapPtToEn[data.summary_type],
    summary: data.summary,
    word_count: data.word_count,
  };
  return mapped;
}
