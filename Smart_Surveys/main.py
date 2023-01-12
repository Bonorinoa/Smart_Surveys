from Question_Upload_Data_Generation.data_generation import DataGeneration
from Question_Upload_Data_Generation.question_upload import QuestionUpload
from Storage.database import Database
from Text_Mining_Insights_Generation.insights_generation import SmartInsights
from Text_Mining_Insights_Generation.report_generation import ReportGeneration
from Text_Mining_Insights_Generation.text_mining import TextMining
from Survey_Distribution_Data_Collection.survey_distribution import SurveyDistribution
from Survey_Distribution_Data_Collection.data_collection import DataCollection

import pandas as pd
import numpy as np
import json

empty_survey = pd.DataFrame()

empty_survey['age'] = DataGeneration().generate_age(15, 65, 100)
empty_survey['income'] = DataGeneration().generate_income(1000, 100000, 100)

print(empty_survey)