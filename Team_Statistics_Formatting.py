import pandas as pd

df1 = pd.read_csv(r'C:\Users\William\Documents\Python Scripts\NBA_Boxscore\12-22-2020\GSW_BRK.csv', encoding='ISO-8859-1')
df4 = pd.read_csv(r'C:\Users\William\Documents\Python Scripts\NBA_Boxscore\12-22-2020\GSW_BRK.csv', encoding='ISO-8859-1')


#gets rid of other team
df2 = df1[df1['Team'].ne('GSW')]
df5 = df4[df4['Team'].ne('BRK')]

#new dataframe
df3 = pd.DataFrame(df2,columns=['FGA', 'ORB', "TOV", "FTA", "PTS"])
df6 = pd.DataFrame(df5,columns=['FGA', 'ORB', "TOV", "FTA", "PTS"])

#sum stats 
sumdf = df3.sum(axis=0) 
sumdf1 = df6.sum(axis=0) 

#create new stats
sumdf['Possessions'] = sumdf["FGA"] - sumdf['ORB'] + sumdf['TOV'] + (.4*sumdf['FTA'])
sumdf1['Possessions'] = sumdf1["FGA"] - sumdf1['ORB'] + sumdf1['TOV'] + (.4*sumdf1['FTA'])

sumdf['OffEff'] = (sumdf["PTS"]/sumdf['Possessions'])*100 
sumdf['DefEff'] = (sumdf1["PTS"]/sumdf['Possessions'])*100 

sumdf['Pace'] = 48*((sumdf['Possessions']+sumdf1['Possessions'])/96)

print(sumdf)