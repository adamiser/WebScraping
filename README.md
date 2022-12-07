# WebScraping - UN Population Data

The blog post featuring the work here is found [at this link](https://adamiser.github.io/stat386-projects/).

This Github repo explores the collection of data from this website: https://population.un.org/dataportal.

Their website features an interactive display to explore data on various characteristics of populations, such as fertility rate, life expectancy, net migration, etc. They also feature a public api to extract the raw data. This repo explores how to use this api to collect meaningful data which can then be used to perform your own analyses. The code is in part based on the instructions found on the website: https://population.un.org/dataportal/about/dataapi

I use packages "requests", "pandas", and "matplotlib" in my python code.

The folder "oldCode" contains past attempts. Nothing within is necessary to generate the data.

The folder "EDA" contains plots and sub-datasets used in my EDA blog posts.

The files "population_api_web_scrape.ipynb" and "eda.ipynb" contain code to be used in a python notebook. The former details data collection using the API and cleaning the resulting data frame. The latter creates multiple plots, charts and tables used to explore the data and create the final data story.

The dataset "population_data_updated.csv" contains our workable data as created by the python code. We explore 10 countries (USA, Japan, China, Congo, Ethiopia, Egypt, India, Pakistan, Nigeria, and Phillipines) and 5 main variables (fertility rate, infant mortality rate, life expectancy at birth, population density, and crude birth rate). 
