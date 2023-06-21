import tweepy


results = tweepy.api.search(q='twython3k')

for tweet in results:
    print('     User: @{}'.format(tweet.from_user))
    print('     Date: {}'.format(tweet.created_at))
    print('     Tweet: {}'.format(tweet.text))
