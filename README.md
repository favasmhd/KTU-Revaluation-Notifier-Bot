# KTU Revaluation Notifier Bot

A simple Python bot that logs into the KTU portal, checks revaluation results for a specified semester, and sends notifications via Telegram.

---

## Features

- Logs into the KTU student portal.
- Fetches revaluation results for your semester.
- Sends updates directly to your Telegram chat.
- Easy to run manually or automate using GitHub Actions.

---

## How to Use

1. Clone the repo and open `ktu_revalbot.py`.
2. Replace these placeholders with your info:

   ```python
   username = "KTU_USERNAME"
   password = "KTU_PASSWORD"
   semester = "B.Tech S5"  # Change to your semester
   bot_token = "TELEGRAM_BOT_TOKEN"
   chat_id = "TELEGRAM_CHAT_ID"
   ```

3. Don’t know how to create a Telegram bot or get your chat ID? [Refer to this guide.](https://github.com/favasmhd/Telegram-bot-setup-guide)

4. Run the script:

   ```bash
   python ktu_revalbot.py
   ```

5. Receive Telegram notification of the current revaluation status.

---

## Automation

To automate the bot using GitHub Actions:

1. Fork this repository and copy the provided `automate.yml` file into your repository’s `.github/workflows/` folder.
2. Make sure your `ktu_revalbot.py` has the correct credentials set.
3. The workflow runs daily at 12:00 AM IST or can be triggered manually from the GitHub Actions tab. The workflow can be modified accordingly to run at different times.

---

## Dependencies

* Python 3.10
* `requests`
* `beautifulsoup4`

Install dependencies via:

```bash
pip install requests beautifulsoup4
```

---

## Disclaimer

This bot uses `verify=False` for requests due to certificate issues on the KTU site. Use at your own risk.

---

Feel free to contribute or report issues!
