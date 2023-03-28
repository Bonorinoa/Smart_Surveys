import pandas as pd
import numpy as np
import re
from typing import List, Tuple, Union
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.corpus import stopwords
from rake_nltk import Rake
from collections import defaultdict, Counter
from textblob import TextBlob
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer

class TextMining:
    """
    This class contains methods for text pre-processing, sentiment analysis, and text classification using NLP techniques
    """
    def __init__(self):
        self.r = Rake()
    
    def data_preprocessing(self, response: str) -> str:
        """
        Applies preprocessing techniques on the dataframe, such as removing stop words, correcting spelling errors, and standardizing numerical variables
        :param data: DataFrame or List of string containing the survey responses
        :type data: Union[pd.DataFrame, List[str]]
        :return: preprocessed List of strings
        """

        # lowercase all responses
        response = response.lower()
        
        # Remove punctuation and special characters
        response = re.sub(r'[^a-z0-9\s]', '', response)
        
        # Remove extra whitespace
        response = re.sub(r'\s+', ' ', response)
            
        return response

    def sentiment_analysis(self, 
                           responses: Union[pd.DataFrame, List[str]]) -> pd.DataFrame:
        """
        Computes the sentiment of the preprocessed text using NLTK's Vader sentiment analyzer
        Appends the sentiment scores as new columns in the preprocessed dataframe
        :param data: DataFrame containing the survey responses
        :type data: Union[pd.DataFrame, List[str]]
        :return: DataFrame with added sentiment score columns
        """
        # Initialize the SentimentIntensityAnalyzer
        sid = SentimentIntensityAnalyzer()

        # Create an empty list to store the results
        results = []

        # Loop through the responses and analyze each one
        for response in responses:
            # Preprocess the response string
            if type(response) == str:
                preprocessed_response = self.data_preprocessing(response)

                # Get the sentiment scores
                sentiment_scores = sid.polarity_scores(preprocessed_response)

                # Append the sentiment scores to the results list
                results.append(sentiment_scores)
            
            else:
                results.append(np.nan)

        # Return the results as a dictionary
        return results
    
        
    def entity_recognition(self, data: Union[pd.DataFrame, List[str]]) -> List[List[str]]:
        """
        Extracts entities from the survey responses
        :param data: DataFrame containing the survey responses or list of strings
        :return: List of lists containing the entities found in each response
        """
        entities = []
        if isinstance(data, pd.DataFrame):
            data = data['response']
            
        for response in data:
            blob = TextBlob(response)
            entities.append(blob.noun_phrases)
            
        return entities
    
    
    def keyword_extraction(self, 
                           data: Union[pd.DataFrame, List[str]]) -> Union[pd.DataFrame, List[str]]:
        """
        Extracts keywords from the text using the RAKE algorithm
        :param data: DataFrame containing the survey responses or List of strings containing the survey responses
        :type data: Union[pd.DataFrame, List[str]]
        :return: DataFrame or List of strings containing the keywords for each survey response
        """
        keywords = []
        for response in data:
            self.r.extract_keywords_from_text(response)
            keywords.append(self.r.get_ranked_phrases())
        return keywords
    
    def parts_of_speech_analysis(self, text: Union[pd.Series, List[str]]):
        """
        Function that performs parts of speech analysis on the given text
        :param text: pandas series or list of strings to perform analysis on
        :return: list of dictionaries of parts of speech and their count in each text
        """
        pos_count_list = []
        for t in text:
            # initialize a TextBlob object
            blob = TextBlob(t)

            # create a dictionary to store parts of speech and their count
            pos_count = {}

            # iterate through the words in the text and update the pos_count dictionary
            for _, pos in blob.tags:
                if pos in pos_count:
                    pos_count[pos] += 1
                else:
                    pos_count[pos] = 1
            
            pos_count_list.append(pos_count)
        return pos_count_list
    
    
    def text_classification(self, 
                            data: Union[pd.DataFrame, List[str]], 
                            technique = "keyword_extraction") -> Union[pd.DataFrame, List[str]]:
        """
        Implements a machine learning technique for text classification
        :param data: DataFrame containing the survey responses
        :type data: Union[pd.DataFrame, List[str]]
        :param technique: String specifying the technique to use (entity recognition, keywords extraction, topic modeling, parts of speech analysis, etc)
        :type technique: str
        :return: DataFrame or List of strings containing the results of the classification technique
        """
        if technique == 'entity_recognition':
            results = self.entity_recognition(data)
        elif technique == 'keyword_extraction':
            results = self.keyword_extraction(data)
        elif technique == 'parts_of_speech_analysis':
            results = self.parts_of_speech_analysis(data)
        else:
            raise ValueError(f"Invalid technique specified: {technique}")
        return results
    
    def most_common_words(self, text: Union[pd.Series, List[str]], n: int) -> List[Tuple[str, int]]:
        """
        Returns a list of the most common words in the given text, along with their frequency
        :param text: pandas series or list of strings to perform analysis on
        :param n: the number of most common words to return
        :return: a list of tuples, where each tuple contains a word and its frequency
        """
        # join all text elements into one string
        all_text = " ".join(text)
        
        # tokenize the text and remove stop words
        all_words = [word for word in all_text.split() if word not in stopwords.words("english")]
        
        # count the frequency of each word
        word_counts = Counter(all_words)
        
        # return the n most common words
        return word_counts.most_common(n)
    
    def least_common_words(self, text: Union[pd.Series, List[str]], n: int) -> List[Tuple[str, int]]:
        """
        Returns a list of the least common words in the given text, along with their frequency
        :param text: pandas series or list of strings to perform analysis on
        :param n: the number of least common words to return
        :return: a list of tuples, where each tuple contains a word and its frequency
        """
        # join all text elements into one string
        all_text = " ".join(text)
        
        # tokenize the text and remove stop words
        all_words = [word for word in all_text.split() if word not in stopwords.words("english")]
        
        # count the frequency of each word
        word_counts = Counter(all_words)
        
        # return the n least common words
        return word_counts.most_common()[:-n-1:-1]
    
    def most_similar_text(self, text: Union[pd.Series, List[str]], comparison_text: str) -> Union[pd.Series, List[str]]:
        """
        Finds the text in the input that is most similar to the comparison text using cosine similarity
        :param text: pandas series or list of strings to compare
        :param comparison_text: string to compare the input text to
        :return: list of strings with the most similar text
        """
        # Initialize the TfidfVectorizer and fit to the input text
        vectorizer = TfidfVectorizer()
        tfidf = vectorizer.fit_transform(text)
        
        # Create a tf-idf representation of the comparison text
        comparison_tfidf = vectorizer.transform([comparison_text])
        
        # Compute cosine similarity between the input text and the comparison text
        cosine_similarities = cosine_similarity(tfidf, comparison_tfidf).flatten()
        
        # Find the index of the most similar text
        most_similar_index = cosine_similarities.argmax()
        
        # Return the most similar text
        return text[most_similar_index]
    
text_miner = TextMining()

list_test = ['I love this course!', 'I hate this course!', 'I am neutral about this course.']

#sentiment = text_miner.sentiment_analysis(list_test)

# entity recognition
entities = text_miner.entity_recognition(list_test)

print(entities)