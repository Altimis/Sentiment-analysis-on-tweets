# Netflix vs Disney+ reputation in USA and Europe

Using sentiment analysis on Tweets streamed for 7 days (from February 1 2020 to February 8 2020), I studied the popularity of Netflix and Disney+ in the US and Europe, and used Bokeh library to visualize these results. 

## Getting started

This repository includes :

* [tweets.ipynb](https://github.com/Altimis/Video-streaming-services-popularity-in-USA-and-Europe-using-sentiment-analysis-on-Tweets/blob/master/tweets.ipynb) : contains the main code for streaming and processing tweets to get the polarity of each tweet. 
* [tweet_app.py](https://github.com/Altimis/Video-streaming-services-popularity-in-USA-and-Europe-using-sentiment-analysis-on-Tweets/blob/master/tweet_app.py) : contains the code for Bokeh application.
* [df.csv](https://github.com/Altimis/Video-streaming-services-popularity-in-USA-and-Europe-using-sentiment-analysis-on-Tweets/blob/master/df.csv) and [df_prepared.csv](https://github.com/Altimis/Video-streaming-services-popularity-in-USA-and-Europe-using-sentiment-analysis-on-Tweets/blob/master/df_prepared.csv) : contains streamed data.

Note that I was only able to stream Tweets for 7 days. You could use another hashtag in [tweets.ipynb](https://github.com/Altimis/Video-streaming-services-popularity-in-USA-and-Europe-using-sentiment-analysis-on-Tweets/blob/master/tweets.ipynb) instead of Netflix and Disney+ to compare other companies, or even other topics. 

## Requirements

pandas, tweepy, bokeh, nltk and cryptography

## Usage 

To visualize the results of this projet, loacte to this repository after cloning it and execute this command : 

```sh
bokeh serve --show tweet_app.py
```
