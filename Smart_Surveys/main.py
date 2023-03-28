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

#empty_survey['age'] = DataGeneration().generate_age(15, 65, 20)
#empty_survey['income'] = DataGeneration().generate_income(1000, 100000, 20)

# Alternatively, generate the questions with DataGeneration().generate_questions()
survey_questions = QuestionUpload().upload_questions("test_sample_questions.json", "json")
questions = [survey_questions["questions"][idx]['question'] for idx in range(len(survey_questions))]
questions_df = pd.DataFrame(questions, columns=['question'])
#print(questions)

sample_db = Database("sample_DB")
# load the contents of survey_questions.json to sample_db
with open("test_sample_atlasSurvey.json", "r") as f:
    sample_survey = json.load(f)

answers = [sample_survey['survey_responses'][idx]['response'] for idx in range(len(sample_survey['survey_responses']))]
answers_df = pd.DataFrame(answers, columns=['response'])

survey_results = pd.concat([empty_survey, questions_df, answers_df], axis=1)

sample_db.save_results(survey_results, "sample_atlasSurvey_TEST")

#print(survey_results)

atlas_saved_results = sample_db.load_results("sample_atlasSurvey_TEST")

#text_miner = TextMining()

# compute sentiment scores
# responses_sentiment = text_miner.sentiment_analysis(saved_results['response'])

#print(responses_sentiment)

# Extract keywords from the responses
# keywords = text_miner.text_classification(saved_results['response'])

#print(keywords)

# parts of speech analysis
# pos_tags = text_miner.text_classification(saved_results['response'], technique="parts_of_speech_analysis")

#print(pos_tags)

# entity recognition
# entities = text_miner.text_classification(saved_results['response'], technique="entity_recognition")

#print(entities)

# generate insights
atlas_test_df = pd.DataFrame(atlas_saved_results)
print(atlas_test_df)

insights = SmartInsights().atlas_analysis(api_key="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",
                                          data=atlas_test_df,
                                          n=1,
                                          max_tokens=500,
                                          temperature=0.75)

print(insights)