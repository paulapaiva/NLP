
I analyzed 500 tweets by first cleaning the text, removing links, mentions, hashtags, punctuation, and common stopwords to keep only important words. Then, I applied two sentiment analysis methods.

The first method was lexicon-based using the VADER tool, which assigns a sentiment score from negative to positive. Tweets with scores above 0.05 were labeled positive, below -0.05 negative, and the rest neutral. This method is fast and easy but sometimes misses the meaning in complex cases.

The second method used a machine learning model from Hugging Face’s transformers pipeline, which classifies each tweet as positive or negative with a confidence score. This model is more sensitive to context and usually gives confident predictions.

 Both methods give useful insights, but combining them or using more data could improve results. 
