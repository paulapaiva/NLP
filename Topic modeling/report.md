I analyzed a collection of texts loaded from a saved dataset. The texts were cleaned by removing punctuation, converting to lowercase, and removing common English stopwords to focus on meaningful words. I applied two topic modeling techniques: Latent Dirichlet Allocation (LDA) and Non-negative Matrix Factorization (NMF), both set to find 10 topics.

For LDA, I used a CountVectorizer to convert the texts into word count features, while for NMF I used a TF-IDF vectorizer to emphasize important words. Both models learned patterns in the data, identifying groups of words that represent different topics.

The top words for each topic were printed, showing distinct themes discovered by each method. To better visualize the topics, I generated word clouds for each topic, highlighting the most relevant words.

LDA tends to produce more general topics based on word frequencies, while NMF captures more specific themes considering word importance. Both methods provided meaningful insights into the main subjects in the text collection. This approach helps to summarize large text data and understand its structure.
