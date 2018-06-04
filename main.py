import praw

reddit= praw.Reddit('bot1')

subreddit = reddit.subreddit("buildapcsales")

for submission in subreddit.new(limit=10):
    if "GPU" in submission.title and "1080" in submission.title:
        print("Title: ", submission.title)