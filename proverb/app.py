import json
import random
import requests
import os


proverbs = [
    {"proverb": "オレのマシンでは動いてるよ",  "who_said": "Anonymous"},
    {"proverb": "コードをデバッグするのは書くことの２倍の労力が要る。つまりあなたの頭脳を最大限に使って書いたコードをデバッグするための頭脳はあなたには無い。", "who_said": "Brian Kernighan"},
    {"proverb": "１人のプログラマーが１ヶ月でできることを２人のプログラマーでやれば、２ヶ月かかる", "who_said": "Fred Brooks"},
    {"proverb": "おしゃべりはいいから、お前のコードを見せろ", "who_said": "Linus Torvalds"}
]


def lambda_handler(event, context):
    # Funny toy app!
    proverb = random.choice(proverbs)
    proverb_text = f"きょうの名言\n*「{proverb['proverb']}」* by {proverb['who_said']}"

    token = os.getenv("SLACK_TOKEN")
    channel = os.getenv("SLACK_CHANNEL")

    result = SlackNotifier(token, channel).post(proverb_text)

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": f"{result.text}",
        })
    }


class SlackNotifier:
    SLACK_POST_MESSAGE_URL = "https://slack.com/api/chat.postMessage"

    def __init__(self, token, channel_name):
        self.token = token
        self.channel_name = channel_name

    def post(self, text):
        params = {
            "token": self.token,
            "channel": self.channel_name,
            "text": text,
            "unfurl_links": True
        }
        return requests.post(url=self.SLACK_POST_MESSAGE_URL, params=params)
