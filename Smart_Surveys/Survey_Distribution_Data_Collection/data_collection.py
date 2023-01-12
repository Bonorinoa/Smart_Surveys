import pandas as pd
import json
import os
import numpy as np

class DataCollection:
    def __init__(self, distribution_method: str = None, survey_file: str = None):
        """
        Initialize the class with any necessary attributes or parameters
        :param distribution_method: method used to distribute the survey (email, web-based, google form, etc)
        :param survey_file: file containing the survey responses
        """
        self.distribution_method = distribution_method
        self.survey_file = survey_file
        
    def collect_data(self):
        """
        Collects the survey responses
        """
        if self.distribution_method == "email":
            pass
            # code to collect data from email responses
        elif self.distribution_method == "web-based":
            pass
            # code to collect data from web-based responses
        elif self.distribution_method == "google form":
            pass
            # code to collect data from google form responses
        else:
            raise ValueError(f"Invalid distribution method: {self.distribution_method}. Supported methods are 'email', 'web-based', and 'google form'.")
            
    def to_dataframe(self):
        """
        Converts the collected data into a pandas DataFrame
        """
        pass
    
    def load_responses(self):
        """
        loads the survey responses from a file
        """
        pass
