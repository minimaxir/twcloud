# twcloud

Generate a word cloud of [Twitter](https://twitter.com/) tweets with a single command.

stylecloud is a Python package that leverages the [twint](https://github.com/twintproject/twint) package to gather Tweets from any public account without requiring authentication, and the [stylecloud](https://github.com/minimaxir/stylecloud) package which adds many useful features to create truly unique word clouds!

* Retrieve tweets from a user, or a Twitter search.
* Gather *any number* of Tweets from the specified query (even beyond the typical 3,200 limit)
* Command Line Interface!

Additionally, from the base `stylecloud` package:

* Icon shapes (of any size!) for wordclouds
* Support for advanced color palettes (via [palettable](https://jiffyclub.github.io/palettable/))
* Manual color selection for text and backgrounds,
* Directional gradients w/ the aforementioned palettes.

## Installation

You can install [twcloud](https://pypi.org/project/twcloud/) via pip:

```sh
pip3 install twcloud
```

## Usage

### Helpful Parameters

These parameters are valid for both the Python function and the CLI (you can use `twcloud -- --help` to get this information as well). Additional visual customization parameters can be found within the stylecloud repo.

* username: Twitter @ username to gather tweets (excluding the @). Any public Twitter account is valid.
* search: Search query to use. Can use a hashtag or a tweet URL (to get quote-tweets)
* limit: Number of tweets to gather before rendering the twcloud [default: `100`]

#### stylecloud parameters w/ Changed Defaults

* icon_name: Icon Name for the stylecloud shape. (e.g. 'fas fa-grin') [default: `fab fa-twitter`]
* colors: Color(s) to use as the text colors. [default: `white`]
* background_color: Background color (name or hex) [default: `#1DA1F2`]
* output_name: Output file name of the stylecloud. [default: `twcloud.png`]

## Helpful Notes

* Specifying a `palette` parameter will override the `colors` parameter. This is the reverse of `stylecloud`.
* Saving the retrieved tweets is out of scope for this package. If you want to save the tweets + additional metadata, use `twint` directly.
* `username` queries will not return Retweets made by the user.

## Maintainer/Creator

Max Woolf ([@minimaxir](https://minimaxir.com))

*Max's open-source projects are supported by his [Patreon](https://www.patreon.com/minimaxir) and [GitHub Sponsors](https://github.com/sponsors/minimaxir). If you found this project helpful, any monetary contributions to the Patreon are appreciated and will be put to good creative use.*

## License

MIT

## Disclaimer

This repo has no affiliation with Twitter Inc.