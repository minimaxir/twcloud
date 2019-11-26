import twint
from stylecloud import gen_stylecloud
import re


def clean_tweet(tweet):
    """
    Cleans the tweet text of URLs, user tags, and hashtags.

    Whitespace does not need to be normalized since it is ignored
    anyways when generating the stylecloud.
    """
    return re.sub(r'http\S+|@[a-zA-Z0-9_]+|#[a-zA-Z0-9_]+', '', tweet)


def get_tweet_text(username=None, search=None, limit=1000):
    """
    Returns a list of cleaned tweets.
    """

    assert any([username, search]), "Either `username` or `search`" \
        "must be specified"
    assert limit % 20 == 0, "`limit` must be a multiple of 20."

    c = twint.Config()
    c.Store_object = True
    c.Hide_output = True

    # User config
    c.Search = search
    c.Username = username
    c.Limit = limit

    # Run the tweet search (may take awhile)
    if username:
        print(f"Retrieving {limit} tweets for {username}")
    else:
        print(f"Retrieving {limit} tweets about {search}")
    twint.run.Search(c)
    assert len(twint.output.tweets_list) > 0, "No tweets were returned."

    tweets = [clean_tweet(tweet.tweet) for tweet in twint.output.tweets_list]

    return tweets


if __name__ == "__main__":
    x = get_tweet_text(username='realdonaldtrump', limit=20)
    print(x)
