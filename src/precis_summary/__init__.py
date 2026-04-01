"""Precis Summary — fast extractive summarization via RAKE keyword extraction."""

from importlib.metadata import version

__version__ = version("precis-summary")

from precis_summary.rake import telegram_precis
from precis_summary.ranking import pick_best_summary

__all__ = ["pick_best_summary", "telegram_precis"]
