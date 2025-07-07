
This task consists of classifying texts into two categories: spam and ham (not spam), based on the content.

First, I applied unsupervised learning techniques to explore the data:

- I transformed the texts into numerical data using TF-IDF vectorization.

- Then, I reduced the dimensions with PCA to visualize the data.

- Using K-Means and Hierarchical clustering, I grouped the texts into two clusters.

- The visualization shows some grouping of texts but without using the true labels for training.

After that, I applied supervised learning methods:

- Texts were preprocessed by removing stopwords and tokenizing.

- I trained a Word2Vec model on the dataset to convert words into vectors.

- Each text was represented by the average of its word vectors (embedding).

- I split the data into train and test sets.

- I tested four classifiers: Naive Bayes, Random Forest, Gradient Boosting, and XGBoost.

- The goal was to predict whether a text is spam or ham using these embeddings.

The results show that:

- Naive Bayes performed poorly, with accuracy close to chance (~50%).

- Random Forest and XGBoost models achieved the best results, with accuracy around 95%.

- Gradient Boosting also performed well, with accuracy around 93%.



