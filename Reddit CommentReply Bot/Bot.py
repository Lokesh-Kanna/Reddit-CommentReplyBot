import praw
import time
import random

from praw.reddit import Submission

# personal use script: -G-xARupY0L-fsY-FeYXbQ
# secret:	YityOfa9sp-x90VvYn650T-HskMEUA

reddit = praw.Reddit(
    client_id="-G-xARupY0L-fsY-FeYXbQ",
    client_secret="YityOfa9sp-x90VvYn650T-HskMEUA",
    user_agent="<COnsole:Mr.Robot> 1.0",
    username="War_God_Kratos",
    password="gorgantua"
)

subreddit = reddit.subreddit("Aww")

for post in subreddit.new(limit=5):
    for comment in post.comments:
        if hasattr(comment, "body"):
            lowerComment = comment.body.lower()
            if " cute " in lowerComment:
                reply = ["Sooo Cute!!!", "Adorable", "Niccceeee"]
                random_number = random.randint(0, len(reply)-1)
                print(reply[random_number])
                comment.reply(reply[random_number])
                time.sleep(60)

