export interface SummaryRequest {
  text: string;
}

export interface SummaryResponse {
  summary: string;
  timestamp: string;
  wordCount: number;
}

export async function createSummary(
  baseUrl: string,
  payload: SummaryRequest
): Promise<SummaryResponse> {
  const url = `${baseUrl}/summaries`;

  const response = await fetch(url, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(payload),
  });

  // Throw error if status not ok
  if (!response.ok) {
    const errorText = await response.text().catch(() => 'Unknown error');
    throw new Error(
      `Failed to create summary: ${response.status} ${response.statusText}. ${errorText}`
    );
  }

  // Parse the response
  const data = (await response.json()) as SummaryResponse;

  // Count words
  const wordCount = data.summary?.length ? data.summary.split(' ').length : 0;

  return {
    summary: data.summary,
    timestamp: data.timestamp,
    wordCount: wordCount,
  };
}
