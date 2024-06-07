import requests
import pandas as pd

def get_wind_power_plants_in_operation():
    url = "https://api.nve.no/web/WindPowerplant/GetWindPowerPlantsInOperation"

    # Make the request, return data
    response = requests.get(url)
    data = response.json()

    #convert to pandas dataframe, write to Excel
    df=pd.DataFrame(data)
    df1=df.copy()
    del df1["Eiere"], df1["Turbiner"]
    df1.to_excel("wind_power_plants_in_operation.xlsx", index=False)

    #with one row for each owner
    df2 = df.explode('Eiere')
    #convert dict to columns
    df2 = pd.concat([df2.drop(['Eiere',"HovedEierNavn","HovedEierOrgNr","Turbiner"], axis=1), df2['Eiere'].apply(pd.Series)], axis=1)

    df2.to_excel("wind_power_plants_in_operation_owners.xlsx", index=False)

    #with one row for each turbine group
    df3 = df.explode('Turbiner')
    #convert dict to columns
    df3 = pd.concat([df3.drop(['Turbiner',"Eiere"], axis=1), df3['Turbiner'].apply(pd.Series)], axis=1)
    df3.to_excel("wind_power_plants_in_operation_turbines.xlsx", index=False)

if __name__ == '__main__':
    get_wind_power_plants_in_operation()