## Our file to write web-scraping functions for a variety of sites that provide NFL statistics.

import requests  # pip install requests
import pandas as pd
from bs4 import BeautifulSoup as bs
import os
import statistics as stat


def scrape_boxscore(date, home_id, away_id):
    """Scrapes the basketball_reference website for daily boxscores of NBA data. Parameters are:
       date in MM-DD-YYYY format (01/05/2021 would be 01052021,
       basket-reference ID of the home team,
       basket-reference ID of the away team."""

    # Sets up url to scrape and gets data for home and away boxscores
    date_triple = date.split('-')
    month = date_triple[0]
    day = date_triple[1]
    year = date_triple[2]
    url = 'https://www.basketball-reference.com/boxscores/' + year + month + day + '0' + home_id + '.html'
    # basic boxscore - away
    df_away = pd.read_html(url)[0]
    df_away = pd.concat([df_away['Unnamed: 0_level_0'], df_away['Basic Box Score Stats']], axis=1, sort=False)
    #advanced boxscore - away
    df_away_adv = pd.read_html(url)[7]
    # clean up advanced boxscore - away
    df_away_adv1 = pd.concat([df_away_adv['Unnamed: 0_level_0'],df_away_adv['Advanced Box Score Stats']], axis=1, sort=False)
    df_away_adv = df_away_adv1.drop(['Starters','MP'],axis=1)
    
    # basic boxscore - home
    df_home = pd.read_html(url)[8]
    df_home = pd.concat([df_home['Unnamed: 0_level_0'], df_home['Basic Box Score Stats']], axis=1, sort=False)
    # advanced boxscore - home
    df_home_adv = pd.read_html(url)[15]
    # clean up advanced boxscore - home
    df_home_adv1 = pd.concat([df_home_adv['Unnamed: 0_level_0'],df_home_adv['Advanced Box Score Stats']], axis=1, sort=False)
    df_home_adv = df_home_adv1.drop(['Starters','MP'],axis=1)
    # merge basic and advanced boxscores
    df_away_all = pd.concat([df_away, df_away_adv], axis=1, sort=False)
    df_home_all = pd.concat([df_home, df_home_adv], axis=1, sort=False)
    df_list = [df_away_all, df_home_all]
    ids = [away_id, home_id]

    for home_away in range(2):
        df = df_list[home_away]

        # Deletes unwanted rows and joins 2 sub-dataframes into a single dataframe
        rows = list(df.index.values)
        last_row = rows[len(rows) - 1]
        df = df.drop([5, last_row])

        # Creates and adds a "Starter" variable (1 if starter, 0 if reserve)
        starter = [0] * df.shape[0]
        for i in range(5):
            starter[i] = 1
        df.insert(1, 'Status', starter)

        # Creates and adds a "Team" (Team ID) and "Home" (Home team or Away team)
        home = [home_away] * df.shape[0]
        team = [ids[home_away]] * df.shape[0]
        df.insert(1, 'Team', team)
        df.insert(2, 'Home', home)

        # Changes "MP" time format from string '00:00' to float 0.0.
        # Did not play will appear as a 2 in staatus column. Did not dress willappear as 3
        rows = list(df.index.values)
        for i in rows:
            if df['MP'][i] == 'Did Not Play':
                df['Status'][i] = 2
            elif df['MP'][i] == 'Did Not Dress':
                df['Status'][i] = 3
            else:
                col_index = df['MP'][i].find(':')
                df['MP'][i] = int(df['MP'][i][:col_index]) + int(df['MP'][i][(col_index+1):])/60
                
        # Replace Did not play and did not dress with zeros
        df = df.replace('Did Not Play', 0)
        df = df.replace('Did Not Dress',0)

        # Changes values in the "+/-" column from strings to integers
        rows = list(df.index.values)
        for i in rows:
            if df['+/-'][i] == '0':
                df['+/-'][i] = 0
            elif df['+/-'][i] == 0:
                df['+/-'][i] = 0
            elif df['+/-'][i][0] == '+':
                df['+/-'][i] = int(df['+/-'][i][1:])
            else:
                df['+/-'][i] = -1 * int(df['+/-'][i][1:])

        # Drops any column that relates to efficiency stats
        df.drop(['FG%', '3P%', 'FT%'], inplace=True, axis=1)
        
        # Add fantasy points column
        fp = (df["PTS"].astype(float) + (1.2*df["TRB"].astype(float)) + (1.5*df["AST"].astype(float)) + (3*df["STL"].astype(float)) + (3*df["BLK"].astype(float)) - df["TOV"].astype(float))
        df.insert(4, 'FPTS', fp)
        
        
        print(df)

        boxscore_dir = r'/Users/jacobplata/Desktop/pp'
        dates = os.listdir(boxscore_dir)
        if date not in dates:
            os.mkdir(boxscore_dir + '/' + date)

        games = os.listdir(boxscore_dir + '/' + date)
        game_file = away_id + '_' + home_id + '.csv'
        if game_file not in games or home_away == 1:
            with open(boxscore_dir + '/' + date + '/' + away_id + '_' + home_id + '.csv', 'a') as f:
                if home_away == 0:
                    df.to_csv(f, header=True, index=False)
                else:
                    df.to_csv(f, header=False, index=False)


def scrape_all_boxscores(season):
    """Scrapes all the boxscore data from a single season in the NBA and stores the boxscores
       in folders by date (MONTH-DAY-YEAR) and
       as a csv file create as such: HOMEID_AWAYID.csv"""
    pass
