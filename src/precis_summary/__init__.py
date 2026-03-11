"""Precis Summary — fast extractive summarization via RAKE keyword extraction."""

__version__ = "0.1.0"

from precis_summary.rake import telegram_precis
from precis_summary.ranking import pick_best_summary

__all__ = ["telegram_precis", "pick_best_summary"]
