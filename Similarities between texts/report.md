In this task, I used a Nike product description dataset to measure how similar the texts are. First, I cleaned the text by lowering letters, removing punctuation, stopwords in english, and lemmatizing the words. Then, I used two methods to calculate similarity: cosine similarity with TF-IDF and Jaccard similarity.

Results:
Cosine similarity (TF-IDF) between first 5 products:
0 vs 1: 0.03
0 vs 2: 0.02
0 vs 3: 0.09
0 vs 4: 0.03
1 vs 2: 0.04
1 vs 3: 0.00
1 vs 4: 0.03
2 vs 3: 0.02
2 vs 4: 0.04
3 vs 4: 0.14

Jaccard similarity between first 5 products:
0 vs 1: 0.03
0 vs 2: 0.01
0 vs 3: 0.06
0 vs 4: 0.04
1 vs 2: 0.03
1 vs 3: 0.00
1 vs 4: 0.03
2 vs 3: 0.02
2 vs 4: 0.04
3 vs 4: 0.05

The results showed low similarity scores between the first five products, which means the descriptions are mostly different from each other. The highest cosine similarity was 0.14, and the highest Jaccard score was 0.06. Cosine similarity considers word frequency and text length, while Jaccard just counts common words.

