#Smart Surveys

##Motivation

Conducting surveys is a common method for gathering data and understanding different perspectives. However, the process of creating and distributing surveys can be time-consuming and error-prone. Additionally, analyzing survey data can be difficult and may require specialized knowledge and tools. Smart Surveys aims to overcome these drawbacks by leveraging state-of-the-art Natural Language Processing models and techniques to simplify the process of generating both surveys and insights.

##Objective

The objective of Smart Surveys is to design and implement an architecture that can automatically generate professional and custom questions for surveys, distribute and collect the surveys, and offer advanced text mining and AI capabilities for generating insights and full reports. This package can be of great help for undergraduate students conducting independent research for the first time as well as for course evaluations, report generation, automatic insight extraction, and other survey-related analysis.

##Features

Generate professional and custom questions for surveys using state-of-the-art Natural Language Processing models
Distribute and collect surveys using various methods such as email and web-based platforms
Perform advanced text mining and AI capabilities for generating insights and full reports
Store and retrieve data and results using a database management system
Getting Started
To use Smart Surveys, you will need to install the package and its dependencies. Once installed, you can use the package to generate questions, distribute surveys, collect responses, and generate insights and reports.

##Documentation

Detailed documentation and usage examples can be found in the package's documentation.

## OpenAI API Usage

In order to use the functionality provided by the Smart Surveys package that relies on the OpenAI API, you will need to provide your own API key. You can sign up for an API key on the OpenAI website (https://beta.openai.com/signup/).

Once you have obtained your API key, you will need to provide it as an argument when initializing certain classes or when calling certain methods within the package. For example, when initializing the DataGeneration class, you will need to pass in your API key as the api_key argument.

It is important to note that usage of the OpenAI API is subject to the terms and conditions outlined on their website, and usage of the Smart Surveys package is subject to those terms as well.

## Directory Structure (note that as of 1/12/2023 some test programs are still in development)

.
└── Smart_surveys/
    ├── smart_surveys/
    │   ├── __init__.py
    │   ├── question_upload/
    │   │   ├── __init__.py
    │   │   ├── data_generation.py
    │   │   └── question_upload.py
    │   ├── storage/
    │   │   ├── __init__.py
    │   │   └── database.py
    │   ├── text_mining/
    │   │   ├── __init__.py
    │   │   ├── insights_generation.py
    │   │   ├── report_generation.py
    │   │   ├── text_mining.py
    │   │   └── utils_mining.py
    │   └── survey_distribution/
    │       ├── __init__.py
    │       ├── data_collection.py
    │       ├── survey_distribution.py
    │       └── utils_distribution.py
    ├── tests/
    │   ├── question_upload/
    │   │   ├── test_data_generation.py
    │   │   └── test_question_upload.py
    │   ├── storage/
    │   │   ├── test_database.py
    │   ├── text_mining/
    │   │   ├── test_insights_generation.py
    │   │   ├── test_report_generation.py
    │   │   ├── test_text_mining.py
    │   │   └── test_utils_mining.py
    │   └── survey_distribution/
    │       ├── test_data_collection.py
    │       ├── test_survey_distribution.py
    │       └── test_utils_distribution.py
    ├── setup.py
    ├── README.md
    ├── .gitignore
    ├── requirements.txt
    └── smart_surveys_Recipe.docx

##Contribution

We welcome contributions to Smart Surveys. If you are interested in contributing, please feel free to reach out to us or submit a pull request.

##License

Smart Surveys is licensed under [insert license here].