import pandas as pd
from functools import reduce
import os

#find csvs 
basepath = r'E:\Drive_William\NBA_Boxscore\Bos\\'


for dirpath, dirnames, files in os.walk(r'E:\Drive_William\NBA_Boxscore\Bos\\'):
                for file_name in files:
                 if file_name.startswith('BOS'):
                    dfs =  [file_name]
                    list_of_dataframes = []
                    for filename in dfs:
                        list_of_dataframes.append(pd.read_csv(basepath + file_name))
                    df_final = pd.concat(list_of_dataframes, ignore_index=True)
                    df_final.drop(df_final[df_final['Home'] == 1].index, inplace = True)
                    print(df_final)
                 #elif file_name.startswith('BRK'):
                    #print(file_name) 
                    
                    
                    
