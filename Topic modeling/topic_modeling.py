# -*- coding: utf-8 -*-
"""Topic modeling

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1N6hAS6HYGyFPA_4LqjG4MwutzVsUsS8F
"""

import pickle
import pandas as pd
import re
import nltk
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.decomposition import LatentDirichletAllocation, NMF
from wordcloud import WordCloud
import matplotlib.pyplot as plt

nltk.download('stopwords')
stop_words = set(stopwords.words('english'))


with open('/content/newsgroups', 'rb') as f:
    newsgroup_data = pickle.load(f)

texts = newsgroup_data

# clean the data
def clean_text(text):
    text = re.sub(r'\W+', ' ', text)  # remove pontuação
    text = text.lower()
    text = ' '.join([word for word in text.split() if word not in stop_words])
    return text

cleaned = [clean_text(t) for t in texts]
df = pd.DataFrame({'cleaned_text': cleaned})

# LDA
count_vectorizer = CountVectorizer(max_df=0.95, min_df=2, stop_words='english')
count_data = count_vectorizer.fit_transform(df['cleaned_text'])

# NMF
tfidf_vectorizer = TfidfVectorizer(max_df=0.95, min_df=2, stop_words='english')
tfidf_data = tfidf_vectorizer.fit_transform(df['cleaned_text'])

# models
n_topics = 10

lda = LatentDirichletAllocation(n_components=n_topics, random_state=42)
lda.fit(count_data)

nmf = NMF(n_components=n_topics, random_state=42)
nmf.fit(tfidf_data)

# viz
def print_topics(model, vectorizer, top_n=10):
    words = vectorizer.get_feature_names_out()
    for topic_idx, topic in enumerate(model.components_):
        print(f"\nTopic #{topic_idx}:")
        print(" ".join([words[i] for i in topic.argsort()[:-top_n - 1:-1]]))

print("LDA Topics:")
print_topics(lda, count_vectorizer)

print("\nNMF Topics:")
print_topics(nmf, tfidf_vectorizer)

# wordClouds
def plot_wordclouds(model, vectorizer, n_topics):
    words = vectorizer.get_feature_names_out()
    for topic_idx, topic in enumerate(model.components_):
        print(f"\nWordCloud for Topic #{topic_idx}")
        topic_words = {words[i]: topic[i] for i in topic.argsort()[:-30:-1]}
        wordcloud = WordCloud(width=800, height=400, background_color='white').generate_from_frequencies(topic_words)
        plt.figure()
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis('off')
        plt.title(f'Topic #{topic_idx}')
        plt.show()

plot_wordclouds(lda, count_vectorizer, n_topics)
plot_wordclouds(nmf, tfidf_vectorizer, n_topics)