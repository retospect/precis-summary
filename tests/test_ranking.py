"""Tests for summary ranking."""

from precis_summary.ranking import SUMMARY_PRIORITY, pick_best_summary


class TestPickBestSummary:
    def test_llm_beats_rake(self):
        summaries = {
            "rake": "keyword; phrases; here",
            "llm:qwen3.5:9b": "LLM sentence summary",
        }
        assert pick_best_summary(summaries) == "LLM sentence summary"

    def test_rake_when_no_llm(self):
        summaries = {"rake": "keyword; phrases; here"}
        assert pick_best_summary(summaries) == "keyword; phrases; here"

    def test_empty_dict(self):
        assert pick_best_summary({}) == ""

    def test_none(self):
        assert pick_best_summary(None) == ""

    def test_skips_empty_values(self):
        summaries = {
            "llm:qwen3.5:9b": "",
            "rake": "keyword; phrases",
        }
        assert pick_best_summary(summaries) == "keyword; phrases"

    def test_llm_gpt4o_beats_rake(self):
        summaries = {
            "rake": "keywords",
            "llm:gpt-4o": "GPT summary",
        }
        assert pick_best_summary(summaries) == "GPT summary"

    def test_first_llm_wins_when_multiple(self):
        summaries = {
            "llm:qwen3.5:9b": "Qwen summary",
            "llm:gpt-4o": "GPT summary",
        }
        # First matching LLM key wins (dict insertion order)
        result = pick_best_summary(summaries)
        assert result == "Qwen summary"

    def test_unknown_key_fallback(self):
        summaries = {"tfidf": "TF-IDF summary"}
        assert pick_best_summary(summaries) == "TF-IDF summary"

    def test_priority_list_has_llm_first(self):
        assert SUMMARY_PRIORITY[0] == "llm:"
        assert "rake" in SUMMARY_PRIORITY
