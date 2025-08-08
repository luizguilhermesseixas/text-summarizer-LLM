export type SummaryType = "small" | "medium" | "large";

export type SummaryResponse = {
  original_text: string;
  summary_type: SummaryType;
  summary: string;
  word_count: number;
};

export type ConversationEntry = {
  id: string;
  text: string;
  summaryType: SummaryType;
  response?: SummaryResponse;
  error?: string;
};

export type HttpErrorBody = { detail?: unknown } | undefined;
