import json
import os
import pandas as pd
from typing import List, Union, Dict

class Database:
    def __init__(self, root_folder_path: str):
        """
        Initialize the class with the root folder path where all the data will be stored
        :param root_folder_path: root folder path where all the data will be stored
        """
        self.root_folder_path = root_folder_path
        self.question_folder_path = os.path.join(root_folder_path, 'questions')
        self.results_folder_path = os.path.join(root_folder_path, 'results')

    def save_questions(self, questions: Union[List[str], pd.Series], file_name: str):
        """
        Saves the questions to the specified file format
        :param questions: list or pandas series of questions
        :param file_name: name of the file to save the questions to
        """
        if not os.path.exists(self.question_folder_path):
            os.makedirs(self.question_folder_path)

        if isinstance(questions, list):
            with open(os.path.join(self.question_folder_path, file_name), "w") as f:
                json.dump(questions, f)
        elif isinstance(questions, pd.Series):
            questions.to_json(os.path.join(self.question_folder_path, file_name))
        else:
            raise TypeError(f"Invalid type for questions: {type(questions)}. Only list or pandas series are supported.")
        
    def load_questions(self, file_name: str, format: str = "json") -> Union[List[str], pd.Series]:
        """
        Loads the questions from the specified file
        :param file_name: name of the file to load the questions from
        :param format: format of the file (json or csv)
        :return: list of questions or pandas series containing the questions
        """
        file_path = os.path.join(self.question_folder_path, file_name)
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File not found: {file_path}")

        if format == "json":
            with open(file_path, "r") as f:
                questions = json.load(f)
                return questions
        elif format == "csv":
            return pd.read_csv(file_path)
        else:
            raise ValueError(f"Invalid file format: {format}. Only json and csv are supported.")
        
    def save_results(self, results: Union[Dict, pd.DataFrame], file_name: str):
        """
        Saves the results to the specified file format
        :param results: dictionary or pandas DataFrame containing the results
        :param file_name: name of the file to save the results to
        """
        if not os.path.exists(self.results_folder_path):
            os.makedirs(self.results_folder_path)

        if isinstance(results, dict):
            with open(os.path.join(self.results_folder_path, file_name), "w") as f:
                json.dump(results, f)
        elif isinstance(results, pd.DataFrame):
            results.to_json(os.path.join(self.results_folder_path, file_name))
        else:
            raise TypeError(f"Invalid type for results: {type(results)}. Only dictionary or pandas DataFrame are supported.")

    def load_questions(self, file_name: str, format: str = "json") -> Union[List[str], pd.Series]:
        """
        Loads the questions from the specified file
        :param file_name: name of the file to load the questions from
        :param format: format of the file (json or csv)
        :return: list of questions or pandas series containing the questions
        """
        file_path = os.path.join(self.question_folder_path, file_name)
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File not found at {file_path}")

        if format == "json":
            with open(file_path, "r") as f:
                questions = json.load(f)
                return questions
        elif format == "csv":
            return pd.read_csv(file_path)
        else:
            raise ValueError(f"Invalid file format: {format}. Only json and csv are supported.")

