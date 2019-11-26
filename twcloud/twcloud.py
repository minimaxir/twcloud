import twint
from stylecloud import gen_stylecloud
from wordcloud import STOPWORDS
import re
import fire


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
    Returns a bulk text of cleaned Tweets from the specified username/search.
    """

    assert any([username, search]), "Either `username` or `search`" \
        "must be specified"
    assert limit % 20 == 0, "`limit` must be a multiple of 20."

    c = twint.Config()
    c.Store_object = True
    c.Hide_output = True

    # User-specified config
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


def gen_twcloud(username=None, search=None, limit=500,
                colors='white',
                background_color='#1DA1F2',
                icon_name='fab fa-twitter',
                custom_stopwords=STOPWORDS,
                output_name='twcloud.png',
                **kwargs):
    """Generates a twcloud of any public Twitter account or search query!
    See stylecloud docs for additional parameters.
    :param username: Twitter @ username to gather tweets.
    :param search: Search query to use to gather tweets.
    :param limit: Number of tweets retrieved.
    """

    tweets = get_tweet_text(username, search, limit)

    # If `palette` is specified, override `colors`.
    # This is the opposite behavior of stylecloud.
    if 'palette' in kwargs:
        colors = None

    # Some stopwords (e.g. I'm, I've) must have quotes removed
    # to match removed smart quotes from tweets.
    noquote_stop = [re.sub(r"'", '', word) for word in custom_stopwords
                    if "'" in word]
    custom_stopwords.update(set(noquote_stop))

    print("Generating the twcloud...")
    gen_stylecloud(text=tweets,
                   output_name=output_name,
                   colors=colors,
                   background_color=background_color,
                   icon_name=icon_name,
                   custom_stopwords=custom_stopwords,
                   **kwargs)


def twcloud_cli(**kwargs):
    """Entrypoint for the twcloud CLI."""
    fire.Fire(gen_twcloud)
