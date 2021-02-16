#import pydfs & features 
from pydfs_lineup_optimizer import get_optimizer, Site, Sport
from pydfs_lineup_optimizer import AfterEachExposureStrategy
from pydfs_lineup_optimizer import get_optimizer, Site, Sport, CSVLineupExporter
from pydfs_lineup_optimizer import PlayersGroup
from pydfs_lineup_optimizer import Stack
from pydfs_lineup_optimizer import TeamStack

#load Site & CSV
optimizer = get_optimizer(Site.FANDUEL, Sport.BASKETBALL)
optimizer.load_players_from_csv(r"E:\Drive_William\Optimizer_CSVs\Optimizer(inputs)\Scrape Csv\01-29-21\Fanduel1.csv")

#basic features 
optimizer.set_min_salary_cap(59600)
optimizer.set_max_repeating_players(5)
optimizer.set_total_teams(7)       # i want 7 team represented per lineup 
#optimizer.set_projected_ownership(max_projected_ownership=0.9)

# player per team 
#optimizer.set_players_from_one_team({'NY': 1})
#optimizer.set_players_from_one_team({'LAC': 2})
#optimizer.set_players_from_one_team({'ATL': 2})
#optimizer.set_players_from_one_team({'WAS': 3})
#optimizer.set_players_from_one_team({'HOU': 3})
#optimizer.set_players_from_one_team({'UTA': 1})  
#optimizer.set_players_from_one_team({'CHA': 1}) 

# restrict positional teammates (seems to do fuck all tho)
optimizer.restrict_positions_for_same_team(('PG', 'PG'))
optimizer.restrict_positions_for_same_team(('SG', 'SG'))
optimizer.restrict_positions_for_same_team(('SF', 'SF'))
optimizer.restrict_positions_for_same_team(('PF', 'PF'))
optimizer.restrict_positions_for_same_team(('PF', 'PF'))
optimizer.restrict_positions_for_same_team(('PF', 'C'))
optimizer.restrict_positions_for_same_team(('C', 'C'))



# restrict negatively correlated teammates 
#mate = PlayersGroup([optimizer.get_player_by_name(name) for name in ('', "")], max_from_group=1)
#optimizer.add_players_group(mate)

#team1 = optimizer.get_player_by_name("")
#team1.max_exposure = 0.1
#team2 = optimizer.get_player_by_name("")
#team2.max_exposure = 0.1

#mate1 = PlayersGroup([optimizer.get_player_by_name(name) for name in ('', '')], max_from_group=1)
#optimizer.add_players_group(mate1)

#team3 = optimizer.get_player_by_name("")
#team3.max_exposure = 0.2
#team4 = optimizer.get_player_by_name("")
#team4.max_exposure = 0.2

#mate2 = PlayersGroup([optimizer.get_player_by_name(name) for name in ('', "")], max_from_group=1)
#optimizer.add_players_group(mate2)

#team5 = optimizer.get_player_by_name("")
#team5.max_exposure = 0.1
#team6 = optimizer.get_player_by_name("")
#team6.max_exposure = 0.3



# filter by position and team 
#filter = filter(lambda p: p.team == '' and '' in p.positions, optimizer.players)
#for player in filter:
#    optimizer.remove_player(player)  # Remove all from optimizer




# set chalk exposures 
#player = optimizer.get_player_by_name('')
#player.max_exposure = 0.15
#optimizer.add_player_to_lineup(player)

#stud = optimizer.get_player_by_name("")
#stud.max_exposure = 0.25
#player1.min_exposure = 0.2 
#optimizer.add_player_to_lineup(player1)

#stud1 = optimizer.get_player_by_name("")
#stud1.max_exposure = 0.15

#stud2 = optimizer.get_player_by_name("")
#stud2.max_exposure = 0.25

#stud3 = optimizer.get_player_by_name("")
#stud3.max_exposure = 0.45

#stud4 = optimizer.get_player_by_name("")
#stud4.min_exposure = 0.1

#stud5 = optimizer.get_player_by_name("")
#stud5.max_exposure = 0.25

#stud6 = optimizer.get_player_by_name("")
#stud6.max_exposure = 0.4

#stud7 = optimizer.get_player_by_name("")
#stud7.max_exposure = 0.15

#stud8 = optimizer.get_player_by_name("")
#stud8.max_exposure = 0.5

#stud9 = optimizer.get_player_by_name("")
#stud9.max_exposure = 0.2

#stud9 = optimizer.get_player_by_name("")
#stud9.max_exposure = 0.25





#drop players 
#drop = optimizer.get_player_by_name('')
#optimizer.remove_player(drop)

#drop1 = optimizer.get_player_by_name("")
#drop2 = optimizer.get_player_by_name('')
#optimizer.remove_player(drop2)

#drop3 = optimizer.get_player_by_name('')
#optimizer.remove_player(drop3)

#drop4 = optimizer.get_player_by_name('')
#optimizer.remove_player(drop4)

#drop5 = optimizer.get_player_by_name('')
#optimizer.remove_player(drop5)

#drop6 = optimizer.get_player_by_name("")
#optimizer.remove_player(drop6)

#drop7 = optimizer.get_player_by_name("")
#optimizer.remove_player(drop7)

#drop8 = optimizer.get_player_by_name("")
#optimizer.remove_player(drop8)

#drop9 = optimizer.get_player_by_name("")
#optimizer.remove_player(drop9)

#drop10 = optimizer.get_player_by_name("")
#optimizer.remove_player(drop10)

#drop11 = optimizer.get_player_by_name("")
#optimizer.remove_player(drop11)

#drop12 = optimizer.get_player_by_name("")
#optimizer.remove_player(drop12)




# custom stacking
#stack1 = PlayersGroup([optimizer.get_player_by_name(name) for name in ('', '')], max_exposure=0.2)
#stack2 = PlayersGroup([optimizer.get_player_by_name(name) for name in ('', '')], max_exposure=0.2)
#stack3 = PlayersGroup([optimizer.get_player_by_name(name) for name in ('', '')], max_exposure=0.15)
#stack4 = PlayersGroup([optimizer.get_player_by_name(name) for name in ('', '')], max_exposure=0.1)
#stack5 = PlayersGroup([optimizer.get_player_by_name(name) for name in ('', '',)], max_exposure=0.1)
#stack6 = PlayersGroup([optimizer.get_player_by_name(name) for name in ('', '')], max_exposure=0.1)
#optimizer.add_stack(Stack([stack1, stack2]))

# team stack
#optimizer.add_stack(TeamStack(2, for_teams=['BKN', 'MIL'], max_exposure_per_team={'BKN': 0.1, 'MIL': 0.1}))  


# group teammates for correlation 
#group = PlayersGroup([optimizer.get_player_by_name(name) for name in ('', '')])
#group.max_exposure = 0.3
#optimizer.add_players_group(group)

#group2 = PlayersGroup([optimizer.get_player_by_name(name) for name in ('', '')])
#group2.max_exposure = 0.3
#optimizer.add_players_group(group2)

#group3 = PlayersGroup([optimizer.get_player_by_name(name) for name in ('', '')])
#group3.mix_exposure = 0.3
#optimizer.add_players_group(group2)



# set leverage players exposures 
#lev = optimizer.get_player_by_name('')
#lev.max_exposure = 0.05

#lev1 = optimizer.get_player_by_name("")
#lev1.max_exposure = 0.2

#lev2 = optimizer.get_player_by_name('')
#lev2.max_exposure = 0.1

#lev3 = optimizer.get_player_by_name('')
#lev3.max_exposure = 0.15

#lev4 = optimizer.get_player_by_name('')
#lev4.min_exposure = 0.1

#lev5 = optimizer.get_player_by_name('')
#lev5.min_exposure = 0.2

#lev6 = optimizer.get_player_by_name('')
#lev6.max_exposure = 0.1

#print & export
for lineup in optimizer.optimize(n=10, exposure_strategy=AfterEachExposureStrategy):
    print(lineup)
    print(lineup.players)  # list of players
    print(lineup.fantasy_points_projection)
    print(lineup.salary_costs)
optimizer.export(r'E:\Drive_William\Optimizer_CSVs\OptimizerExport\export(27)1.csv')