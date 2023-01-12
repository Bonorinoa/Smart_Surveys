import unittest
import numpy as np

import sys
sys.path.append("C:/Users/Bonoc/OneDrive/Winter_22_23/Smart_Surveys/code/Question_Upload_Data_Generation")

from data_generation import DataGeneration

class TestDataGeneration(unittest.TestCase):
    def test_generate_questions(self):
        data_gen = DataGeneration('questions')
        questions = data_gen.generate_questions()
        self.assertIsNotNone(questions)
        self.assertIsInstance(questions, str)
        
    def test_generate_responses(self):
        data_gen = DataGeneration('responses')
        responses = data_gen.generate_responses()
        self.assertIsNotNone(responses)
        self.assertIsInstance(responses, str)
        
    def test_generate_age(self):
        data_gen = DataGeneration('age')
        ages = data_gen.generate_age(18, 30, 10)
        self.assertIsNotNone(ages)
        self.assertIsInstance(ages, np.ndarray)
        
    def test_generate_gpa(self):
        data_gen = DataGeneration('gpa')
        gpa = data_gen.generate_gpa(1, 4, 10)
        self.assertIsNotNone(gpa)
        self.assertIsInstance(gpa, np.ndarray)
        
    def test_generate_income(self):
        data_gen = DataGeneration('income')
        income = data_gen.generate_income(20000, 100000, 10)
        self.assertIsNotNone(income)
        self.assertIsInstance(income, np.ndarray)

if __name__ == '__main__':
    unittest.main()
