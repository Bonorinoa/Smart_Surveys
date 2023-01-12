import pandas as pd
from typing import Union, List, Dict
import openai
import numpy as np
import os

class DataGeneration:
    def __init__(self):
        """
        Initialize the class with any necessary attributes or parameters
        :param data_type: type of data to generate i.e question, responses, age, gpa or income
        :param data_file: file name or dataframe that contains the data to generate from
        """
        self.sample_questions = None
        self.sample_responses = None
        self.sample_ages = None
        self.sample_gpas = None
        self.sample_incomes = None
        
    def generate_questions(self, 
                           api_key: str, 
                           sample_questions: Union[List[str], str], 
                           n: int, 
                           max_tokens: int, 
                           temperature: float, 
                           stop: str) -> Union[List[str], str]:
        """
        Generates questions based on the specified parameters
        :param api_key: OpenAI API key
        :param sample_questions: a list of strings representing the sample_questions, or a long String containing the sample_questions
        :param n: number of questions to generate
        :param max_tokens: maximum number of tokens to generate
        :param temperature: temperature for the model
        :param stop: stop sequence for the model
        """
        if not isinstance(api_key, str):
            raise TypeError(f"Expected a string but got {type(api_key)}")
        if not api_key:
            raise ValueError("Please provide an API key")
        
        openai.api_key = api_key
        
        if isinstance(sample_questions, list):
            self.sample_questions = "".join(sample_questions)
        elif isinstance(sample_questions, str):
            if os.path.splitext(sample_questions)[1] != '.txt':
                raise ValueError(f"Invalid file type. Expected .txt file but got {os.path.splitext(sample_questions)[1]}")
            with open(sample_questions, 'r') as f:
                self.sample_questions = f.read()
            
        prompt = f""
        
        try:
            completions = openai.Completion.create(engine="text-davinci-003", 
                                                prompt=prompt, 
                                                max_tokens=1024, 
                                                n=1,
                                                stop=None,
                                                temperature=0.5)
            questions = completions.choices[0].text
        except openai.error.OpenAiError as e:
            raise ValueError(f"An error occurred while calling the OpenAI API: {e}")
        
        return (questions, questions)
    
    def provide_sample_questions(self, 
                                 sample_questions: Union[List[str], str]):
        """
        Provide sample_questions for the question generation model
        :param sample_questions: a list of strings representing the sample_questions, or a file path to a .txt file containing the sample_questions
        """
        if isinstance(sample_questions, list):
            self.sample_questions = sample_questions
        elif isinstance(sample_questions, str):
            if os.path.splitext(sample_questions)[1] != '.txt':
                raise ValueError(f"Invalid file type. Expected .txt file but got {os.path.splitext(sample_questions)[1]}")
            with open(sample_questions, 'r') as f:
                self.sample_questions = f.read().splitlines()
        else:
            raise TypeError(f"Expected a list of strings or a file path but got {type(sample_questions)}")

    def generate_responses(self, 
                           api_key: str, 
                           sample_responses: Union[List[str], str], 
                           n: int, 
                           max_tokens: int, 
                           temperature: float, 
                           stop: str) -> Union[List[str], str]:
        """
        Generates responses based on the specified parameters
        :param api_key: OpenAI API key
        :param sample_responses: a list of strings representing the sample_responses, or a long String containing the sample_responses
        :param n: number of responses to generate
        :param max_tokens: maximum number of tokens to generate
        :param temperature: temperature for the model
        :param stop: stop sequence for the model
        """
        if not isinstance(api_key, str):
            raise TypeError(f"Expected a string but got {type(api_key)}")
        if not api_key:
            raise ValueError("Please provide an API key")
        
        openai.api_key = api_key
        
        prompt = f""
        
        try:
            completions = openai.Completion.create(engine="text-davinci-003", 
                                                prompt=prompt, 
                                                max_tokens=1024, 
                                                n=1,
                                                stop=None,
                                                temperature=0.5)
            answers = completions.choices[0].text
        except openai.error.OpenAiError as e:
            raise ValueError(f"An error occurred while calling the OpenAI API: {e}")
        
        return (answers, completions)

    def generate_age(self, 
                     start: float, 
                     end: float, 
                     size: int) -> np.ndarray:
        """
        Generates age based on the specified parameters
        :param start: start value for the range
        :param end: end value for the range
        :param size: number of age values to generate
        :return: array of generated ages
        """
        if not all(map(lambda x: isinstance(x, (int, float)), (start, end, size))):
            raise TypeError("'start', 'end', and 'size' must be numerical values.")
        if not all(map(lambda x: x > 0, (start, end, size))):
            raise ValueError("'start', 'end', and 'size' must be positive values.")
        if start > end:
            raise ValueError("'start' must be less than or equal to 'end'.")

        return np.random.uniform(start, end, size).round(2)

    def generate_gpa(self, 
                     start: float, 
                     end: float, 
                     size: int) -> np.ndarray:
        """
        Generates gpa based on the specified parameters
        :param start: start value for the range
        :param end: end value for the range
        :param size: number of gpa values to generate
        :return: array of generated gpa
        """
        if not all(map(lambda x: isinstance(x, (int, float)), (start, end, size))):
            raise TypeError("'start', 'end', and 'size' must be numerical values.")
        if not all(map(lambda x: x > 0, (start, end, size))):
            raise ValueError("'start', 'end', and 'size' must be positive values.")
        if start > end:
            raise ValueError("'start' must be less than or equal to 'end'.")
        if start > 4 or end > 4:
            raise ValueError("'start' and 'end' must be less than or equal to 4.")
        
        return np.random.uniform(start, end, size).round(2)

    def generate_income(self, 
                        start: float, 
                        end: float, 
                        size: int) -> np.ndarray:
        """
        Generates income based on the specified parameters
        :param start: start value for the range
        :param end: end value for the range
        :param size: number of income values to generate
        :return: array of generated income
        """
        if not all(map(lambda x: isinstance(x, (int, float)), (start, end, size))):
            raise TypeError("'start', 'end', and 'size' must be numerical values.")
        if not all(map(lambda x: x > 0, (start, end, size))):
            raise ValueError("'start', 'end', and 'size' must be positive values.")
        if start > end:
            raise ValueError("'start' must be less than or equal to 'end'.")
        if start < 1000 or end > 1000000000:
            raise ValueError("'start' must be greater than or equal to 1000 and 'end' must be less than or equal to 1000000000.")
        
        return np.random.uniform(start, end, size).round(2)
