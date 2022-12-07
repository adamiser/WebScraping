import pandas as pd
import numpy as np
import requests as re
from bs4 import BeautifulSoup

def callAPI(relative_path, topic_list = False) -> pd.DataFrame:

    base_url = "https://population.un.org/dataportalapi/api/v1"
    url = base_url + relative_path
    r = re.get(url)
    r.status_code

    j = r.json()
    
    if topic_list:
        df = pd.json_normalize(j, 'indicators')
        return(df)
    
    df = pd.json_normalize(j['data'])
    while j['nextPage'] != None:
        response = re.get(j['nextPage'])
        j = response.json()
        df_temp = pd.json_normalize(j['data'])
        #df = df.append(df_temp)
        df = pd.concat([df, df_temp])
    
    return(df)


# What locations do I want?

# 36 - Australia
# 554 - NZ
# 882 - Samoa
# 776 - Tonga
# 242 - Fiji

# What data do I want?

# 75, 76 - life expectancy
# 74 - births by age of mother
# 70,71 - population by age groups
# 67 - median age population
# 66 - migration
# 65 - net-migration
# 63 - probability of dying between 15 and 60
# 61 - life expectancy at birth
# 56 - net reproduction rate (daughters per woman)
# 55 - crude birth rate
# 54 - population density
# 43 - currently married (number)
# 42 - currently married (percent)
# 22 - infant mortality rate
# 19 - total fertility rate

# KEEP - 0, 1, 16, 31

# Fertility rate
# Only want variantLabel = Median
fert = callAPI("/data/indicators/19/locations/840,36,554,882,776,242/start/1980/end/2020")
fert = fert[fert['variantLabel'] == 'Median']
fert = fert.rename(columns={'value':'Fertility_rate'})
fert = fert.drop(fert.columns[[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 17, 18,
                       19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]], axis = 1)

# Infant mortality rate 
# Only want sex = Both sexes
inf_mort = callAPI("/data/indicators/22/locations/840,36,554,882,776,242/start/1980/end/2020")
inf_mort = inf_mort[inf_mort['sex'] == 'Both sexes']
inf_mort = inf_mort.rename(columns={'value':'Inf_Mortality_rate'})
inf_mort = inf_mort.drop(inf_mort.columns[[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 17, 18,
                       19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]], axis = 1)

# Life expectancy at birth 
# Only want sex = Both sexes
life = callAPI("/data/indicators/61/locations/840,36,554,882,776,242/start/1980/end/2020")
life = life[life['sex'] == 'Both sexes']
life = life.rename(columns={'value':'Life_expectancy'})
life = life.drop(life.columns[[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 17, 18,
                       19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]], axis = 1)

# Population density 
pop_dens = callAPI("/data/indicators/54/locations/840,36,554,882,776,242/start/1980/end/2020")
pop_dens = pop_dens.rename(columns={'value':'Pop_density'})
pop_dens = pop_dens.drop(pop_dens.columns[[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 17, 18,
                       19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]], axis = 1)

# Crude birth rate 
birth_rate = callAPI("/data/indicators/55/locations/840,36,554,882,776,242/start/1980/end/2020")
birth_rate = birth_rate.rename(columns={'value':'Birth_rate'})
birth_rate = birth_rate.drop(birth_rate.columns[[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 17, 18,
                       19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]], axis = 1)

df = pd.merge(fert, inf_mort, on=["locationId", "location", "timeLabel"])
df = pd.merge(df, life, on=["locationId", "location", "timeLabel"])
df = pd.merge(df, pop_dens, on=["locationId", "location", "timeLabel"])
df = pd.merge(df, birth_rate, on=["locationId", "location", "timeLabel"])

df.to_csv('population_data.csv')
