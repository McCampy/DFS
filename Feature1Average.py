import pandas as pd
from functools import reduce

#import csv
df1 = pd.read_csv(r'C:\Users\William\Documents\Python Scripts\NBA_Boxscore\12-22-2020\GSW_BRK.csv', encoding='ISO-8859-1')
df2 = pd.read_csv(r'C:\Users\William\Documents\Python Scripts\NBA_Boxscore\12-25-2020\BRK_BOS.csv', encoding='ISO-8859-1')

#filtering
#gets rid of other team
df_new = df1[df1['Team'].ne('GSW')]
#sorts by last name 
sort = df_new.sort_values('Starters')

df_new1 = df2[df2['Team'].ne('BOS')]
sort2 = df_new1.sort_values('Starters')

#important data 
name = [sort["Starters"]]
mp = [sort["MP"]]
fga = [sort["FGA"]]
tpa = [sort["3PA"]]
fta = [sort["FTA"]]
trb = [sort["TRB"]]
ast = [sort["AST"]]
stl = [sort["STL"]]
blk = [sort["BLK"]]
tov = [sort["TOV"]]
pts = [sort["PTS"]]

name1 = [sort2["Starters"]]
mp1 = [sort2["MP"]]
fga1 = [sort2["FGA"]]
tpa1 = [sort2["3PA"]]
fta1 = [sort2["FTA"]]
trb1 = [sort2["TRB"]]
ast1 = [sort2["AST"]]
stl1 = [sort2["STL"]]
blk1 = [sort2["BLK"]]
tov1 = [sort2["TOV"]]
pts1 = [sort2["PTS"]]

#headers list
headers1 = ["Name"]
headers2 = ["MP"]
headers3 = ["FGA"]
headers4 = ["3PA"]
headers5 = ["FTA"]
headers6 = ["TRB"]
headers7 = ["AST"]
headers8 = ["STL"]
headers9 = ["BLK"]
headers10 = ["TOV"]
headers11 = ["PTS"]

#buildings dfs 
df3 = pd.concat(name, axis=1, keys=headers1)
df4 = pd.concat(mp, axis=1, keys=headers2)
df5 = pd.concat(fga, axis=1, keys=headers3)
df6 = pd.concat(tpa, axis=1, keys=headers4)
df7 = pd.concat(fta, axis=1, keys=headers5)
df8 = pd.concat(trb, axis=1, keys=headers6)
df9 = pd.concat(ast, axis=1, keys=headers7)
df10 = pd.concat(stl, axis=1, keys=headers8)
df11 = pd.concat(blk, axis=1, keys=headers9)
df12 = pd.concat(tov, axis=1, keys=headers10)
df13 = pd.concat(pts, axis=1, keys=headers11)

df14 = pd.concat(name1, axis=1, keys=headers1)
df15 = pd.concat(mp1, axis=1, keys=headers2)
df16 = pd.concat(fga1, axis=1, keys=headers3)
df17 = pd.concat(tpa1, axis=1, keys=headers4)
df18 = pd.concat(fta1, axis=1, keys=headers5)
df19 = pd.concat(trb1, axis=1, keys=headers6)
df20 = pd.concat(ast1, axis=1, keys=headers7)
df21 = pd.concat(stl1, axis=1, keys=headers8)
df22 = pd.concat(blk1, axis=1, keys=headers9)
df23 = pd.concat(tov1, axis=1, keys=headers10)
df24 = pd.concat(pts1, axis=1, keys=headers11)

#important data 
data = [df3["Name"], df4["MP"], df5["FGA"], df6["3PA"], df7["FTA"], df8["TRB"], df9["AST"], df10["STL"], df11["BLK"], df12["TOV"], df13["PTS"]]
headers12 = ["Name", "MP", "FGA", "3PA", "FTA", "TRB", "AST", "STL", "TOV", "PTS"]
df14 = pd.concat(data, axis=1, keys=headers12)

data1 = [df14["Name"], df15["MP"], df16["FGA"], df17["3PA"], df18["FTA"], df19["TRB"], df20["AST"], df21["STL"], df22["BLK"], df23["TOV"], df24["PTS"]]
df15 = pd.concat(data1, axis=1, keys=headers12)

#merge dataframes 
#dfs = [df14, df15] 
#df_final = reduce(lambda left,right: pd.merge(left,right,on='Name'), dfs)

print(df_final)