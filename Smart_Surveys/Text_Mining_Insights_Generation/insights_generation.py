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
    

    def atlas_analysis(self, 
                    api_key: str, 
                    data: pd.DataFrame, 
                    n: int, 
                    max_tokens: int, 
                    temperature: float) -> str:
    
        '''
        Test prompt for the atlas_analysis function
        params:
            api_key: OpenAI API key
            data: dataframe containing the data to generate the insights from
            n: number of insights to generate
            max_tokens: maximum number of tokens to generate
            temperature: temperature for the model 
        '''
        
        if not isinstance(api_key, str):
            raise TypeError(f"Expected a string but got {type(api_key)}")
        if not api_key:
            raise ValueError("Please provide an API key")
        
        openai.api_key = api_key
        
        #features = data.columns.tolist()
        questions = data.question.to_list()
        responses = data.response.to_list()
        keywords = "[well-being, happiness, sadness, anger, fear, disgust, surprise, trust, anticipation, joy, sadness, love, hate, contentment, satisfaction, gratitude, compassion, empathy, kindness, generosity, sympathy, guilt, shame, pride, embarrassment, regret, hope, optimism, pessimism, confidence, self-esteem, self-worth, self-respect, self-confidence, self-consciousness, self-awarenes]"
        
        # topics that could be used to evaluate a given survey according to the PERMA+4 measures
        #survey_assesment_topics = "[positive emotions, engagement, relationships, meaning, accomplishment, physical health, mindset, work environment, economic security]"
        
        prompt = f"Given the following questions [{str(questions)}] and responses [{str(responses)}]," \
            + f" provide a well being assessment of the surveyed object. Be descriptive, insightful, and calm."
            
        sys_prompt = f"You are a well-being expert. You are tasked with providing a well-being assessment of the surveyed object." \
            + f" You can use the following keywords to help you: {keywords}. \n"
         
        # this will change to ChatCompletion endpoint when their apir errors are fixed   
        try:
            completion = openai.Completion.create(engine="text-davinci-003",
                                                prompt= sys_prompt + prompt,
                                                temperature=temperature,
                                                n=n,
                                                max_tokens=max_tokens)
            
            
            insight = completion.choices[0].text
            
        except openai.error.OpenAIError as e:
            raise ValueError(f"An error occurred while calling the OpenAI API: {e}")
                
        return insight
    