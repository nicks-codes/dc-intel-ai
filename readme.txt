# Data Center Expert API

A FastAPI backend that powers a GPT-based assistant for real-time data center insights.

## Features

- `/news/latest` – Get the latest data center news
- `/site-reports/{location}` – Site-level insights
- `/digest` – Weekly market digest

## 🛠 Local Development

```bash
# Install dependencies
pip install -r requirements.txt

# Run the app
uvicorn main:app --reload
