name: Auto Update Numbers

on:
  schedule:
    - cron: '0 * * * *'
  workflow_dispatch:

jobs:
  update:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout repo
        uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.10'

      - name: Run script
        run: python scraper.py

      - name: Commit and push changes
        run: |
          git config --global user.name "GitHub Action Bot"
          git config --global user.email "bot@github.com"
          git add numbers.json
          git diff --quiet && git diff --cached --quiet || (git commit -m "Auto-update numbers" && git push)

