"""Summary ranking — pick the best summary from a multi-profile dict.

The summaries dict uses keys like:
  "rake"              — extractive RAKE keyphrases
  "llm:qwen3.5:9b"   — LLM-generated summary
  "llm:gpt-4o"        — LLM-generated summary (different model)

Ranking is a simple prefix-priority list: first matching prefix wins.
"""

from __future__ import annotations

# Ordered best → worst.  First matching prefix wins.
SUMMARY_PRIORITY: list[str] = [
    "llm:",
    "rake",
]


def pick_best_summary(summaries: dict[str, str] | None) -> str:
    """Pick the highest-ranked summary from a summaries dict.

    Args:
        summaries: Dict mapping profile key to summary text.
            Example: {"rake": "...", "llm:qwen3.5:9b": "..."}

    Returns:
        Best available summary text, or empty string if none.
    """
    if not summaries:
        return ""

    for prefix in SUMMARY_PRIORITY:
        for key, val in summaries.items():
            if key.startswith(prefix) and val:
                return val

    # Fallback: return first non-empty value
    for val in summaries.values():
        if val:
            return val

    return ""
