import pandas as pd
import numpy as np
import json
import os
from typing import Union, List, Dict

class QuestionUpload:
    def __init__(self, file_uploaded: Union[str, pd.DataFrame] = None, 
                 save_as: str = "Default_DB" # file_name: str = None 
                 ):
        """
        Initialize the class with any necessary attributes or parameters
        :param file_uploaded: file name or dataframe that contains the questions to upload
        """
        self.file_uploaded = file_uploaded
        self.save_as = save_as
        self.file_format = None

    def upload_questions(self, file_, file_type: str = "csv"):
        """
        Uploads questions from a file and converts it to a pandas DataFrame
        :param file_: file object or file path
        :param file_type: type of file being uploaded i.e csv, txt or json. Defaults to csv.
        :return: DataFrame containing the questions
        """
        if file_type == 'csv':
            questions_df = pd.read_csv(file_)
            self.file_format = "csv"
            
        elif file_type == 'txt':
            questions_df = pd.read_csv(file_, delimiter='\t')
            self.file_format = "txt"
            
        elif file_type == 'json':
            questions_df = pd.read_json(file_)
            self.file_format = "json"
            
        else:
            raise ValueError(f"Invalid file type: {file_type}. Supported types are 'csv', 'txt', and 'json'.")
        
        return questions_df

            
    def save_questions(self, questions: Union[list, pd.Series, str]) -> None:
        """
        Saves the questions to the specified file format
        :param questions: list, pandas series or json of questions
        """
        if os.path.isfile(self.save_as):
            raise FileExistsError(f"File {self.save_as} already exists.")
            
        if isinstance(questions, list):
            if self.file_format == "csv":
                pd.DataFrame(questions).to_csv(self.save_as, index=False)
            elif self.file_format == "json":
                with open(self.save_as, "w") as f:
                    json.dump(questions, f)
            else:
                raise ValueError(f"Invalid file format: {self.file_format}. Only csv and json are supported.")
            
        elif isinstance(questions, pd.Series):
            if self.file_format == "csv":
                questions.to_csv(self.save_as, index=False)
            elif self.file_format == "json":
                with open(self.save_as, "w") as f:
                    json.dump(questions.to_list(), f)


    def edit_questions(self, questions: Union[List[str], pd.Series, dict], 
                       index: int, 
                       new_question: str):
        """
        Edits a question at a given index
        :param questions: list, pandas series, or dict containing questions
        :param index: index of the question to edit
        :param new_question: the new question to replace the old one
        :return: the updated list, pandas series, or dict
        """
        if isinstance(questions, list):
            questions[index] = new_question
            
        elif isinstance(questions, pd.Series):
            questions.iloc[index] = new_question
            
        elif isinstance(questions, dict):
            questions[index] = new_question
            
        else:
            raise TypeError("Invalid type for questions. Should be list, pandas series, or dict.")
        
        return questions
