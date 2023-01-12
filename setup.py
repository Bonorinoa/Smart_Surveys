from setuptools import setup, find_packages

setup(
    name='Smart_Surveys',
    version='0.1',
    packages=find_packages(),
    url='https://github.com/Bonorinoa/Smart_Surveys',
    license='MIT',
    author='Augusto Gonzalez Bonorino',
    author_email='augusto.gonzalez-bonorino@cgu.com',
    description='A package for generating professional and custom questions for surveys, distributing and collecting them and offering text mining as well as AI capabilities to generate advanced insights and full reports',
    install_requires=[
        'numpy',
        'pandas',
        'openai',
        # Other dependencies here
    ],
)
