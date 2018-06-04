import praw
import smtplib

email = ***
password = ***

reddit= praw.Reddit('bot1')

subreddit = reddit.subreddit("buildapcsales")

for submission in subreddit.new(limit=5):
    if "GPU" in submission.title and "1060" in submission.title:
        # email setup
        content = 'Subject: {}\n\n{}'.format(submission.title, submission.url)
        mail = smtplib.SMTP('smtp.gmail.com', 587)
        mail.ehlo()

        mail.starttls()

        mail.login(email, password)

        mail.sendmail(email, email, content)
        mail.close()