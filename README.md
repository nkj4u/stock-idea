# Stock Idea - 米国株投資アイデア生成システム

このプロジェクトは、noteから株式関連記事を自動取得し、米国株市場の要約レポートおよび投資アイデアを生成するシステムです。

## 機能

- Seleniumを使用してnote記事の自動取得
- 米国株市場の日次要約レポート生成
- AI分析による投資アイデアの提案
- Markdown形式でのレポート出力

## 使い方

### 1. 記事の取得と要約生成

以下のコマンドを実行して、note記事を取得し市場要約を生成します：

```bash
python3 fetch_note_posts_selenium.py
```

### 2. 出力ファイル

- 生成されるファイルは `./docs/market_summary_YYYYMMDD.md` 形式で保存されます
- 各ファイルには市場要約と投資アイデアが含まれます

## ファイル構成

```text
stock-idea/
├── README.md                      # このファイル
├── fetch_note_posts_selenium.py   # note記事取得スクリプト
├── prompt.txt                     # AI分析用プロンプト
└── docs/                          # 出力ディレクトリ
    ├── README.md                  # レポートファイル一覧
    ├── market_summary_20250807.md # 市場要約レポート
    └── market_summary_20250808.md # 市場要約レポート
```

## 必要環境

- Python 3.x
- Selenium WebDriver
- Chrome Browser
- webdriver-manager

## 注意事項

- 本システムで生成される情報は投資助言を目的としたものではありません
- 投資判断はご自身の責任でお願いいたします
- note記事の取得には適切な利用規約の遵守が必要です

## レポート一覧

生成されたレポートファイルの詳細は [docs/README.md](./docs/README.md) をご参照ください。