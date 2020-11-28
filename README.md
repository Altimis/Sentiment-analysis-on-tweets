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
## Results 

Here is the visualization of polarity of Netflix and Disney+ tweets in both US and Europe. 

* Europe : 

![](bokeh_plot_europe.png?raw=true)

* USA : 

![](bokeh_plot_usa.png?raw=true)

Despite the limited data (only 7 days), I was able to get some useful information from it: 

- Disney+ is more popular in this period than netflix in Europe. In fact, during this period, Disney+ reached its peak in the stock market.
- On February 5, 2020, Toy story 4 was released on Disney+, which justifies the increase of positive tweets on Disney+ in the US compared to netflix, which started to decrease. 
