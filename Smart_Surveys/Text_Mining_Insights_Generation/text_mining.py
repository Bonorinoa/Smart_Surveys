import pandas as pd
import numpy as np
from typing import List, Dict, Union

class TextMining:
    def __init__(self):
        pass
    
    def data_preprocessing(self, data: pd.DataFrame) -> pd.DataFrame:
        """
        Applies preprocessing techniques on the dataframe, such as removing stop words, correcting spelling errors, and standardizing numerical variables
        :param data: DataFrame containing the survey responses
        :return: preprocessed DataFrame
        """
        pass

    def sentiment_analysis(self, data: pd.DataFrame) -> pd.DataFrame:
        """
        Computes the sentiment of the preprocessed text using NLTK's Vader sentiment analyzer
        Appends the sentiment scores as new columns in the preprocessed dataframe
        :param data: DataFrame containing the survey responses
        :return: DataFrame with added sentiment score columns
        """
        pass
    
    
    def text_classification(self, data: pd.DataFrame, technique: str) -> Union[pd.DataFrame, List[str]]:
        """
        Implements a machine learning technique for text classification
        :param data: DataFrame containing the survey responses
        :param technique: String specifying the technique to use (entity recognition, keywords extraction, topic modeling, parts of speech analysis, etc)
        :return: DataFrame or List of strings containing the results of the classification technique
        """
        pass