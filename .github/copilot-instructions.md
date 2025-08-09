# Copilot Instructions for `stock-idea`

This project automates the collection and summarization of US stock market news and investment ideas, outputting daily markdown reports. Follow these conventions and workflows to be productive:

## Architecture & Data Flow
- **Data Source**: Fetches articles from a specific note.com user using Selenium (`fetch_note_posts_selenium.py`).
- **Processing**: Extracts the latest articles, summarizes content, and generates investment ideas.
- **Output**: Writes daily market summaries and ideas to `docs/market_summary_YYYYMMDD.md` (one file per day).
- **Indexing**: Updates `docs/README.md` with links to all daily reports.

## Key Workflows
- **Daily Update**:
  1. Run: `python3 fetch_note_posts_selenium.py`
  2. Summarize the output as a US stock analyst.
  3. Save the summary and investment ideas in markdown to `docs/market_summary_YYYYMMDD.md` (use current date).
  4. Add a link to the new file in `docs/README.md`.
- **File Naming**: Use `market_summary_YYYYMMDD.md` (e.g., `market_summary_20250809.md`).
- **Directory Structure**:
  - `fetch_note_posts_selenium.py`: Main fetch & parse script
  - `docs/`: Output directory for reports
  - `prompts/daily.instructions.md`: Task instructions for daily workflow

## Project-Specific Conventions
- **Language**: All summaries and ideas are in Japanese, targeting US stock investors.
- **Article Selection**: Always use the *second most recent* article from note.com for analysis.
- **Summarization**: Limit summaries to ~100 characters for the main body, then expand with detailed analysis and investment ideas.
- **README Index**: `docs/README.md` must always list all `market_summary_YYYYMMDD.md` files as links.
- **Error Handling**: If article fetch fails, output a clear error message and do not overwrite previous reports.

## Examples
- See `docs/market_summary_20250809.md` for a typical report format.
- See `prompts/daily.instructions.md` for the daily automation prompt.

## External Dependencies
- **Selenium** and **webdriver_manager** are required for scraping. Ensure Chrome is available in the environment.

## Do Not
- Do not change the file naming or directory structure.
- Do not output summaries in English.
- Do not skip updating the index in `docs/README.md`.

---
For any unclear conventions, review the latest files in `docs/` and `prompts/` for reference patterns.
