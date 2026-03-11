# precis-summary

Fast extractive summarization via RAKE keyword extraction. Zero dependencies.

## Usage

```python
from precis_summary import telegram_precis, pick_best_summary

# RAKE keyword extraction (~5ms, zero deps)
text = "Metal-organic frameworks exhibit high CO2 adsorption capacity..."
precis = telegram_precis(text)
# → "Metal-organic frameworks; high CO2 adsorption capacity; ..."

# Pick best summary from a multi-profile dict
summaries = {
    "rake": "Metal-organic frameworks; high CO2 adsorption",
    "llm:qwen3.5:9b": "MOFs show 3x CO2 uptake vs zeolites; amine-functionalized variants optimal",
}
best = pick_best_summary(summaries)
# → "MOFs show 3x CO2 uptake vs zeolites; amine-functionalized variants optimal"
```

## Summary ranking

`pick_best_summary()` uses prefix-priority matching:

1. `llm:*` — any LLM-generated summary (best quality)
2. `rake` — extractive RAKE keyphrases (instant, always available)
3. Fallback — first non-empty value

Ranking lives in code, not in the data. New summary methods are added by
extending `SUMMARY_PRIORITY` in `ranking.py`.
