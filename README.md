# News API Email Digest 📰✉️

A Python project that fetches the latest news about any topic using NewsAPI and sends a curated digest via email.

## Features ✨

- **Automated News Fetching**: Gets latest articles via NewsAPI
- **Customizable Topics**: Change `topic` variable for different subjects
- **Email Delivery**: Sends formatted digest to your inbox
- **Multi-language Support**: Handles international news sources
- **Error Handling**: Robust email sending with try-catch

## How It Works ⚙️

1. **Fetches News** using NewsAPI
2. **Formats Digest** with titles, descriptions and URLs
3. **Sends Email** via SMTP (Gmail supported)
4. **Runs Daily** (when scheduled)

## Code Structure
### 📦project
    ├── 📄main.py # Fetches news and creates digest
    ├── 📄Send_Emails.py # Handles email delivery
    └── 📄mail.env # Stores email credentials (gitignored)


## Example Output 📧

```text
Subject: Today's news

Tesla lancia il Cybertruck RWD: meno costoso...
New cheaper Cybertruck version announced...
https://example.com/tesla-news

Morgan Stanley Traders Rally Past Estimates...
Bank outperforms despite market conditions...
https://example.com/finance-news
```
## Setup Guide 🛠️
Get NewsAPI key from newsapi.org
https://newsapi.org/<br>
Configure email in mail.env:
```
EMAIL_USER=your@gmail.com<br>
EMAIL_PASSWORD=app_password<br>
EMAIL_RECEIVER=recipient@email.com<br>
```

```text
Install requirements:<br>
pip install requests python-dotenv <br>
Run: main.py
```