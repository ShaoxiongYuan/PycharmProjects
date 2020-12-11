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

color = ['red', 'green', 'blue', 'orange']
fig = plt.figure()
plt.xticks(rotation=45, ha="right", rotation_mode="anchor")
plt.subplots_adjust(bottom=0.2, top=0.9)
plt.ylabel('No of Deaths')
plt.xlabel('Dates')


# 此函数是绘制动画的回调函数
# 有且仅有一个参数 i
def showLine(i):
    plt.legend(df1.columns)
    p = plt.plot(df1[:i].index, df1[:i].values)
    for i in range(0, 4):
        p[i].set_color(color[i])


animator = ani.FuncAnimation(fig, showLine, interval=10)
plt.show()
