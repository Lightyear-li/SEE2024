from utils_imports import *

combo_weight = [0,1.0,1.2,1.3,1.5,1.8,2.3,3.1,4.4,6.5,9.9,15.4,24.3,38.7,62.0,99.7,160.7,259.4,419.1]
pointype_weight = [1.1,1.3,1.3,1.1]
gametype_weight = [1,1,1.5,1.5,1.1]

def normalize_score(row):
    p1 = row["p1_score"]
    p2 = row["p2_score"]
    if 4 in [p1, p2]:
        p1_normalized = (5 - p2) / (10 - p1 - p2)
        p2_normalized = (5 - p1) / (10 - p1 - p2)
    else:
        p1_normalized = (4 - p2) / (8 - p1 -p2)
        p2_normalized = (4 - p1) / (8 - p1 -p2)
    return pd.Series([p1_normalized, p2_normalized], index=["p1_score", "p2_score"])

def normalize_game(row):
    p1 = row["p1_games"]
    p2 = row["p2_games"]
    if 6 in [p1, p2]:
        p1_normalized = (7 - p2) / (14 - p1 - p2)
        p2_normalized = (7 - p1) / (14 - p1 - p2)
    else:
        p1_normalized = (6 - p2) / (12 - p1 -p2)
        p2_normalized = (6 - p1) / (12 - p1 -p2)
    return pd.Series([p1_normalized, p2_normalized], index=["p1_games", "p2_games"])

def normalize_set(row):
    p1 = row["p1_sets"]
    p2 = row["p2_sets"]
    p1_normalized = (3 - p2) / (6 - p1 -p2)
    p2_normalized = (3 - p1) / (6 - p1 -p2)
    return pd.Series([p1_normalized, p2_normalized], index=["p1_sets", "p2_sets"])

def normalize_speed(col):
    return (col - col.min()) / (col.max() - col.min())

def point_count(data):
    win_count = 0
    lose_count = 0
    for index, row in data.iterrows():
        if row['point_victor']==1:
            win_count += 1
            lose_count = 0
        else:
            lose_count += 1
            win_count = 0

        data.at[index, 'cont_victor'] = win_count
        data.at[index, 'cont_lose'] = lose_count

def game_count(data):
    win_count = 0
    lose_count = 0
    for index, row in data.iterrows():
        if row['game_victor']==0:
            data.at[index, 'cont_victor'] = 0
            data.at[index, 'cont_lose'] = 0
        elif row['game_victor']==1:
            win_count += 1
            lose_count = 0
            data.at[index, 'cont_victor'] = win_count
            data.at[index, 'cont_lose'] = lose_count
        elif row['game_victor']==-1:
            lose_count += 1
            win_count = 0
            data.at[index, 'cont_victor'] = win_count
            data.at[index, 'cont_lose'] = lose_count

def set_count(data):
    win_count = 0
    lose_count = 0
    for index, row in data.iterrows():
        if row['set_victor']==0:
            data.at[index, 'cont_victor'] = 0
            data.at[index, 'cont_lose'] = 0
        elif row['set_victor']==1:
            win_count += 1
            lose_count = 0
            data.at[index, 'cont_victor'] = win_count
            data.at[index, 'cont_lose'] = lose_count
        elif row['set_victor']==-1:
            lose_count += 1
            win_count = 0
            data.at[index, 'cont_victor'] = win_count
            data.at[index, 'cont_lose'] = lose_count    

def type_identify(row):
    ptype = 1
    if row['game_victor']!=0:
        ptype = 2
    if row['p1_break_pt_won']!=0 or row['p2_break_pt_won']!=0:
        ptype = 3
    if row['set_victor']!=0:
        ptype = 4
    return pd.Series(ptype, index=["ptype"])

def calculate_motum(row):
    if 'server' in row:
        mt = row['point_victor'] * combo_weight[row['conti_pt']] * pointype_weight[row['server']+row['point_victor']+1] \
            + row['game_victor'] * combo_weight[row['conti_gm']] * gametype_weight[row['server']] \
            + row['set_victor'] * combo_weight[row['conti_st']]
        return pd.Series(mt,index=["delta_motum"])
    else:
        return pd.Series(0,index=["delta_motum"])






'''
data['set_sum'] = content.p1_sets + content.p2_sets
data['set_gap'] = content.p1_sets - content.p2_sets
data['game_sum'] = content.p1_games + content.p2_games
data['game_gap'] = content.p1_games - content.p2_games
data['point_sum'] = content.p1_score + content.p2_score
data['point_gap'] = content.p1_score - content.p2_score
'''