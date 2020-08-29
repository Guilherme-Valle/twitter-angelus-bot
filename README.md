# twitter-angelus-bot
Bot programmed for remember Angelus prayer on Twitter, developed with Tweepy.

# Modus Operandi

The pray named Angelus are prayed by catholics at 6:00AM, 12:00 and 18:00PM, sometimes at 9:00AM too. I developed a Python application to tweet a remember 
message, using a Python package for Twitter API named Tweepy for post using the profile @AngelusBot.

With the Python file on a server, i programmed a crontab to run the process on the defined hours at the brazilian timezone.

The crontab:

`0 6,9,12,18 * * * cd ~/angelus-app-twitter && python3 bot_app.py`

# Problems

Initially i wanted to just tweet "Angelus" with a bible versicle, but i doesn't works for a Twitter bot, because the Twitter API doesn't allows duplicated tweets.
So, i decidet to tweet the message with the timestamps, solving the problem.
