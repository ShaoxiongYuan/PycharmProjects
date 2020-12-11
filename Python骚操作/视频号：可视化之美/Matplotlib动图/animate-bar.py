import matplotlib.animation as ani
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# url = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv'
df = pd.read_csv('a.csv', delimiter=',', header='infer')
df_interest = df.loc[
    df['Country/Region'].isin(['United Kingdom', 'US', 'Italy', 'Germany']) & df['Province/State'].isna()]
df_interest.rename(index=lambda x: df_interest.at[x, 'Country/Region'], inplace=True)
df1 = df_interest.transpose()
df1 = df1.drop(['Province/State', 'Country/Region', 'Lat', 'Long'])
df1 = df1.loc[(df1 != 0).any(1)]
df1.index = pd.to_datetime(df1.index)

fig, ax = plt.subplots()
explode = [0.01, 0.01, 0.01, 0.01]  # pop out each slice from the pie


def getmepie(i):
    def absolute_value(val):
        a = np.round(val / 100. * df1.head(i).max().sum(), 0)
        return int(a)

    ax.clear()
    plot = df1.head(i).max().plot.pie(y=df1.columns, autopct=absolute_value, label='', explode=explode, shadow=True)
    plot.set_title('Total Number of Deaths\n' + str(df1.index[min(i, len(df1.index) - 1)].strftime('%Y-%m-%d')),
                   fontsize=12)


animator = ani.FuncAnimation(fig, getmepie, interval=200)
plt.show()
