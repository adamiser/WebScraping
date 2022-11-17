# WebScraping

This Github repo explores the collection of data from this website: https://population.un.org/dataportal.

Their website features an interactive display to explore data on various characteristics of populations, such as fertility rate, life expectancy, net migration, etc. They also feature a public api to extract the raw data. This repo explores how to use this api to collect meaningful data which can then be used to perform your own analyses. The code is in part based on the instructions found on the website: https://population.un.org/dataportal/about/dataapi

I use packages "requests" and "pandas" in my python code.

The folder "oldCode" contains past attempts. Nothing within is necessary to generate the data.

The files "population_api_web_scrape.ipynb" and "population_api_web_scrape.py" contain identical code to be used in a python notebook (jupyter notebook, for example) or a python script (visual studio code) respectively. This code contains calls to the api and basic data cleaning to create the dataset.

The dataset "population_data.csv" contains our workable data as created by the python code. We explore 6 countries (USA, and 5 Oceanic countries Australia, New Zealand, Tonga, Fiji, and Samoa) and 5 main variables (fertility rate, infant mortality rate, life expectancy at birth, population density, and crude birth rate). The api contains data on many other countries with many other variables.
