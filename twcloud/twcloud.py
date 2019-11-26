import twint
from stylecloud import gen_stylecloud
import re


def clean_tweet(tweet):
    """
    Cleans the tweet text of URLs, user tags, hashtags, pictures,
    and smart punctuation.

    Whitespace does not need to be normalized since it is ignored
    anyways when generating the stylecloud.
    """
    pattern = r'http\S+|pic.\S+|@[a-zA-Z0-9_]+|#[a-zA-Z0-9_]+|[‘’“”’–—…]|\xa0'
    return re.sub(pattern, '', tweet)


def get_tweet_text(username, search, limit):
    """
    Returns a bulk text of cleaned tweets.
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
        print(f"Retrieving {limit} tweets for @{username}...")
    else:
        print(f"Retrieving {limit} tweets about {search}...")
    twint.run.Search(c)
    assert len(twint.output.tweets_list) > 0, "No tweets were returned."

    tweets = [clean_tweet(tweet.tweet) for tweet in twint.output.tweets_list]

    return " ".join(tweets)


def gen_twcloud(username=None, search=None, limit=1000,
                colors='white',
                background_color='#1DA1F2',
                icon_name='fab fa-twitter',
                **kwargs):

    tweets = get_tweet_text(username, search, limit)

    print("Generating the twcloud...")
    gen_stylecloud(text=tweets,
                   output_name='twcloud.png',
                   colors=colors,
                   background_color=background_color,
                   icon_name=icon_name,
                   **kwargs)


if __name__ == "__main__":
    gen_twcloud(username='dril', limit=100, size=1024)
