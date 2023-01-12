from typing import Union
import pandas as pd
import json
import os

class SurveyDistribution:
    def __init__(self, emails: Union[str, list] = None, survey: Union[str, pd.DataFrame] = None):
        """
        Initialize the class with any necessary attributes or parameters
        :param emails: a list of emails or a file path containing the emails to send the survey to
        :param survey: a dataframe or file path containing the survey questions
        """
        self.emails = emails
        self.survey = survey
        self.distribution_method = None

    def select_distribution_method(self, method: str):
        """
        Select the method for distributing the survey
        :param method: the method of distribution, options include 'email', 'web-based', 'google form'
        """
        self.distribution_method = method

    def generate_survey(self):
        """
        Generate the survey based on the selected distribution method
        """
        pass

    def send_surveys(self):
        """
        Send out the surveys to the provided email addresses
        """
        pass

    def collect_responses(self):
        """
        Collect the responses from the survey
        """
        pass

    def transform_to_dataframe(self):
        """
        Transform the collected responses into a pandas dataframe
        """
        pass
