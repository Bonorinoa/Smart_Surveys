import pandas as pd
import numpy as np
import openai
import os

class SmartInsights():
    def __init__(self) -> None:
        pass
    
    def strength_and_weaknesses(self, 
                                api_key: str, 
                                data: pd.DataFrame, 
                                n: int, 
                                max_tokens: int, 
                                temperature: float, 
                                stop: str) -> str:
        """
        Generate a summary of the strengths and weaknesses of the surveyed object
        :param api_key: OpenAI API key
        :param data: dataframe containing the data to generate the insights from
        :param n: number of insights to generate
        :param max_tokens: maximum number of tokens to generate
        :param temperature: temperature for the model
        :param stop: stop sequence for the model
        :return: a string containing the generated insights
        """
        if not isinstance(api_key, str):
            raise TypeError(f"Expected a string but got {type(api_key)}")
        if not api_key:
            raise ValueError("Please provide an API key")
        
        openai.api_key = api_key
        
        features = data.columns.tolist()
        responses = [data["survey_responses"][idx]['response'] for idx in range(len(data))]
        
        prompt = f"Given the following variables [{str(features)}] and responses [{str(responses)}]," \
               + f" what are the strengths and weaknesses of the surveyed object?"
        
        try:
            completions = openai.Completion.create(engine="text-davinci-003", 
                                                prompt=prompt, 
                                                max_tokens=max_tokens, 
                                                n=n,
                                                stop=stop,
                                                temperature=temperature)
            summary = completions.choices[0].text
            
        except openai.error.OpenAiError as e:
            raise ValueError(f"An error occurred while calling the OpenAI API: {e}")
        
        return summary               
    

    