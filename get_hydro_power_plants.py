import requests
import pandas as pd

'''
Note: Includes hydro power plants under construction and decommisioned plants.
'''

def get_hydro_power_plants():
    url = "https://api.nve.no/web/Powerplant/GetHydroPowerPlants"

    # Make the request, return data
    response = requests.get(url)
    data = response.json()

    #convert to pandas dataframe, write to Excel
    df=pd.DataFrame(data)
    df.to_excel("hydro_power_plants.xlsx", index=False)

if __name__ == '__main__':
    get_hydro_power_plants()
