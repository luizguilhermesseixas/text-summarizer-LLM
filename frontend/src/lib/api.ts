import { API_URL } from "@/lib/config";
import { SummaryResponse, SummaryType } from "@/types/summary";

export async function summarizeText(params: {
  text: string;
  summaryType: SummaryType;
}): Promise<SummaryResponse> {
  const res = await fetch(`${API_URL}/api/v1/summarize`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      text: params.text,
      summary_type: params.summaryType,
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

  return (await res.json()) as SummaryResponse;
}
