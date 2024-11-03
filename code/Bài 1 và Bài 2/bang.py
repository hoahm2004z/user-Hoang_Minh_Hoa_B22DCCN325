
# Tạo tiêu đề CSV từ tất cả các thuộc tính của Player
header = [
    "name", "nation", "team", "position", "age",
    # Playing Time
    "matches_played", "starts", "minutes",
    # Performance
    "non_penalty_goals", "penalty_goals", "assists", "yellow_cards", "red_cards",
    # Expected
    "xG", "npxG", "xAG",
    # Progression
    "PrgC", "PrgP", "PrgR",
    # Per 90 minutes
    "per90_Gls", "per90_Ast", "per90_G+A", "per90_G-PK", "per90_G+A-PK",
    "per90_xG", "per90_xAG", "per90_xG+xAG", "per90_npxG", "per90_npxG+xAG",
    # Goalkeeping
    "GA", "GA90", "SoTA", "Saves", "Save%", "W", "D", "L", "CS", "CS%",
    # Goalkeeping Penalty Kicks
    "PKatt", "PKA", "PKsv", "PKm", "GK_Save%",
    
    # Shooting Standard
    "Gls", "Sh", "SoT", "SoT%", "Sh/90", "SoT/90", "G/Sh", "G/SoT", "Dist", "FK", "PK", "PKatt",
    # Shooting Expected
    "xG", "npxG", "npxG/Sh", "G-xG", "np:G-xG",


    # Passing Total
    "Pass_Cmp", "Pass_Att", "Pass_Cmp%", "TotDist", "PrgDist",
    # Passing Short
    "Short_Cmp", "Short_Att", "Short_Cmp%",
    # Passing Medium
    "Medium_Cmp", "Medium_Att", "Medium_Cmp%",
    # Passing Long
    "Long_Cmp", "Long_Att", "Long_Cmp%",
    # Expected Passing
    "Ast","xAG", "xA", "A-xAG", "KP", "1/3", "PPA", "CrsPA", "PrgP",


    # Pass Types
    "Pass_Live", "Pass_Dead", "Pass_FK", "Pass_TB", "Pass_Sw", "Pass_Crs", "Pass_TI", "Pass_CK",
    # Pass Outcomes
    "Pass_Corner_In", "Pass_Corner_Out", "Pass_Corner_Str",
    "Pass_Cmp_outcome", "Pass_Off", "Pass_Blocks",



    #Goal and shot
    "SCA","SCA90","SCA PassLive","SCA PassDead","SCA TO","SCA Sh","SCA Fld","SCA Def",
    "GCA","GCA90", "GCA PassLive", "GCA PassDead", "GCA TO", "GCA Sh", "GCA Fld", "GCA Def",
    
    
    # Defensive Actions
    "Tkl", "TklW", "Def_3rd", "Mid_3rd", "Att_3rd",
    "Challenges_Tkl", "Challenges_Att", "Challenges_Tkl%", "Challenges_Lost",
    "Blocks","Blocks_Sh", "Blocks_Pass", "Blocks_Int", "Blocks_Tkl+Int", "Blocks_Clr", "Blocks_Err",
    
    
    # Possession
    "Touches", "Def_Pen", "Def_3rd", "Mid_3rd", "Att_3rd", "Att_Pen", "Live",
    # Take-ons
    "Take_Att", "Take_Succ", "Take_Succ%", "Take_Tkld", "Take_Tkld%",
    # Carries
    "Carries", "Carries_TotDist", "Carries_ProDist", "Carries_ProgC", "Carries_1/3", "Carries_CPA", "Carries_Mis", "Carries_Dis",
    "Receiving_Rec","Receiving_PrgR",

    #playing detail
    "Starts","Mn/Start", "Compl",
    "Subs", "Mn/Sub", "unSub", 
    "PPM", "onG", "onGA", 
    "onxG", "onxGA",

    # Miscellaneous Stats
    "Fls", "Fld", "Off", "Crs", "OG", "Recov", 
    "Aerial_Won", "Aerial_Lost", "Aerial_Won%",
]
# print(len(header))

def row(player):
    return [
    player.name,player.nation, player.team, player.position, player.age,
    # Playing Time
    player.playing_time["matches_played"], player.playing_time["starts"], player.playing_time["minutes"],
    # Performance
    player.performance["non_penalty_goals"], player.performance["penalty_goals"], player.performance["assists"],
    player.performance["yellow_cards"], player.performance["red_cards"],
    # Expected
    player.expected["xG"], player.expected["npxG"], player.expected["xAG"],
    # Progression
    player.progression["PrgC"], player.progression["PrgP"], player.progression["PrgR"],
    # Per 90 minutes
    player.per_90["Gls"], player.per_90["Ast"], player.per_90["G+A"], player.per_90["G-PK"],
    player.per_90["G+A-PK"], player.per_90["xG"], player.per_90["xAG"], player.per_90["xG+xAG"],
    player.per_90["npxG"], player.per_90["npxG+xAG"],
    # Goalkeeping Performance
    player.goalkeeping["Performance"]["GA"], player.goalkeeping["Performance"]["GA90"], 
    player.goalkeeping["Performance"]["SoTA"], player.goalkeeping["Performance"]["Saves"],
    player.goalkeeping["Performance"]["Save%"], player.goalkeeping["Performance"]["W"],
    player.goalkeeping["Performance"]["D"], player.goalkeeping["Performance"]["L"],
    player.goalkeeping["Performance"]["CS"], player.goalkeeping["Performance"]["CS%"],
    # Goalkeeping Penalty Kicks
    player.goalkeeping["Penalty Kicks"]["PKatt"], player.goalkeeping["Penalty Kicks"]["PKA"],
    player.goalkeeping["Penalty Kicks"]["PKsv"], player.goalkeeping["Penalty Kicks"]["PKm"],
    player.goalkeeping["Penalty Kicks"]["Save%"],
    # Shooting Standard
    player.shooting["Standard"]["Gls"], player.shooting["Standard"]["Sh"], 
    player.shooting["Standard"]["SoT"], player.shooting["Standard"]["SoT%"], 
    player.shooting["Standard"]["Sh/90"], player.shooting["Standard"]["SoT/90"], 
    player.shooting["Standard"]["G/Sh"], player.shooting["Standard"]["G/SoT"], 
    player.shooting["Standard"]["Dist"], player.shooting["Standard"]["FK"], 
    player.shooting["Standard"]["PK"], player.shooting["Standard"]["PKatt"],
    # Shooting Expected
    player.shooting["Expected"]["xG"], player.shooting["Expected"]["npxG"], 
    player.shooting["Expected"]["npxG/Sh"], player.shooting["Expected"]["G-xG"], 
    player.shooting["Expected"]["np:G-xG"],


    # Passing Total
    player.passing["Total"]["Cmp"], player.passing["Total"]["Att"], 
    player.passing["Total"]["Cmp%"], player.passing["Total"]["TotDist"], 
    player.passing["Total"]["PrgDist"],
    # Passing Short
    player.passing["Short"]["Cmp"], player.passing["Short"]["Att"], 
    player.passing["Short"]["Cmp%"],
    # Passing Medium
    player.passing["Medium"]["Cmp"], player.passing["Medium"]["Att"], 
    player.passing["Medium"]["Cmp%"],
    # Passing Long
    player.passing["Long"]["Cmp"], player.passing["Long"]["Att"], 
    player.passing["Long"]["Cmp%"],
    # Expected Passing
    player.passing["Expected"]["Ast"], player.passing["Expected"]["xAG"], 
    player.passing["Expected"]["xA"], player.passing["Expected"]["A-xAG"], 
    player.passing["Expected"]["KP"], player.passing["Expected"]["1/3"], 
    player.passing["Expected"]["PPA"], player.passing["Expected"]["CrsPA"], 
    player.passing["Expected"]["PrgP"],


    # Pass Types
    player.pass_types["Pass Types"]["Live"], player.pass_types["Pass Types"]["Dead"], 
    player.pass_types["Pass Types"]["FK"], player.pass_types["Pass Types"]["TB"], 
    player.pass_types["Pass Types"]["Sw"], player.pass_types["Pass Types"]["Crs"], 
    player.pass_types["Pass Types"]["TI"], player.pass_types["Pass Types"]["CK"],
    #conner Kick
    player.pass_types["Corner Kicks"]["In"],
    player.pass_types["Corner Kicks"]["Out"],
    player.pass_types["Corner Kicks"]["Str"],
    # Pass Outcomes
    player.pass_types["Outcomes"]["Cmp"], player.pass_types["Outcomes"]["Off"], 
    player.pass_types["Outcomes"]["Blocks"],



    #goal_shot_creation
    player.goal_shot_creation["SCA"]["SCA"],
    player.goal_shot_creation["SCA"]["SCA90"],
    player.goal_shot_creation["SCA Types"]["PassLive"],
    player.goal_shot_creation["SCA Types"]["PassDead"],
    player.goal_shot_creation["SCA Types"]["TO"],
    player.goal_shot_creation["SCA Types"]["Sh"],
    player.goal_shot_creation["SCA Types"]["Fld"],
    player.goal_shot_creation["SCA Types"]["Def"],
    player.goal_shot_creation["GCA"]["GCA"],
    player.goal_shot_creation["GCA"]["GCA90"],
    player.goal_shot_creation["GCA Types"]["PassLive"],
    player.goal_shot_creation["GCA Types"]["PassDead"],
    player.goal_shot_creation["GCA Types"]["TO"],
    player.goal_shot_creation["GCA Types"]["Sh"],
    player.goal_shot_creation["GCA Types"]["Fld"],
    player.goal_shot_creation["GCA Types"]["Def"],
    # Defensive Actions
    player.defensive_actions["Tackles"]["Tkl"], player.defensive_actions["Tackles"]["TklW"], 
    player.defensive_actions["Tackles"]["Def 3rd"], player.defensive_actions["Tackles"]["Mid 3rd"], 
    player.defensive_actions["Tackles"]["Att 3rd"],
    player.defensive_actions["Challenges"]["Tkl"], player.defensive_actions["Challenges"]["Att"], 
    player.defensive_actions["Challenges"]["Tkl%"], player.defensive_actions["Challenges"]["Lost"],
    
    player.defensive_actions["Blocks"]["Blocks"], 
    player.defensive_actions["Blocks"]["Sh"],
    player.defensive_actions["Blocks"]["Pass"],
    player.defensive_actions["Blocks"]["Int"],
    player.defensive_actions["Blocks"]["Tkl + Int"],
    player.defensive_actions["Blocks"]["Clr"],
    player.defensive_actions["Blocks"]["Err"],


    # Possession
    player.possession["Touches"]["Touches"], player.possession["Touches"]["Def Pen"], 
    player.possession["Touches"]["Def 3rd"], player.possession["Touches"]["Mid 3rd"], 
    player.possession["Touches"]["Att 3rd"], player.possession["Touches"]["Att Pen"], 
    player.possession["Touches"]["Live"],
    player.possession["Take-Ons"]["Att"], player.possession["Take-Ons"]["Succ"], 
    player.possession["Take-Ons"]["Succ%"], player.possession["Take-Ons"]["Tkld"], 
    player.possession["Take-Ons"]["Tkld%"],

    player.possession["Carries"]["Carries"], player.possession["Carries"]["TotDist"], 
    player.possession["Carries"]["ProDist"], player.possession["Carries"]["ProgC"], 
    player.possession["Carries"]["1/3"], player.possession["Carries"]["CPA"], 
    player.possession["Carries"]["Mis"], player.possession["Carries"]["Dis"],

    player.possession["Receiving"]["Rec"],
    player.possession["Receiving"]["PrgR"],

    # Playing Time
    player.playing_time_detail["Starts"]["Starts"],
    player.playing_time_detail["Starts"]["Mn/Start"],
    player.playing_time_detail["Starts"]["Compl"],
    player.playing_time_detail["Subs"]["Subs"],
    player.playing_time_detail["Subs"]["Mn/Sub"],
    player.playing_time_detail["Subs"]["unSub"],
    player.playing_time_detail["Team Success"]["PPM"],
    player.playing_time_detail["Team Success"]["onG"],
    player.playing_time_detail["Team Success"]["onGA"],
    player.playing_time_detail["Team Success xG"]["onxG"],
    player.playing_time_detail["Team Success xG"]["onxGA"],


    # Miscellaneous Stats
    player.misc_stats["Performance"]["Fls"], player.misc_stats["Performance"]["Fld"], 
    player.misc_stats["Performance"]["Off"], player.misc_stats["Performance"]["Crs"], 
    player.misc_stats["Performance"]["OG"], player.misc_stats["Performance"]["Recov"], 
    player.misc_stats["Aerial Duels"]["Won"], player.misc_stats["Aerial Duels"]["Lost"], 
    player.misc_stats["Aerial Duels"]["Won%"]
]



def rowsquad(squad):
    return [
    squad.players,squad.name,squad.numberOfPlayer, squad.poss, squad.age,
    # Playing Time
    squad.playing_time["matches_played"], squad.playing_time["starts"], squad.playing_time["minutes"],
    # Performance
    squad.performance["non_penalty_goals"], squad.performance["penalty_goals"], squad.performance["assists"],
    squad.performance["yellow_cards"], squad.performance["red_cards"],
    # Expected
    squad.expected["xG"], squad.expected["npxG"], squad.expected["xAG"],
    # Progression
    squad.progression["PrgC"], squad.progression["PrgP"], squad.progression["PrgR"],
    # Per 90 minutes
    squad.per_90["Gls"], squad.per_90["Ast"], squad.per_90["G+A"], squad.per_90["G-PK"],
    squad.per_90["G+A-PK"], squad.per_90["xG"], squad.per_90["xAG"], squad.per_90["xG+xAG"],
    squad.per_90["npxG"], squad.per_90["npxG+xAG"],
    # Goalkeeping Performance
    squad.goalkeeping["Performance"]["GA"], squad.goalkeeping["Performance"]["GA90"], 
    squad.goalkeeping["Performance"]["SoTA"], squad.goalkeeping["Performance"]["Saves"],
    squad.goalkeeping["Performance"]["Save%"], squad.goalkeeping["Performance"]["W"],
    squad.goalkeeping["Performance"]["D"], squad.goalkeeping["Performance"]["L"],
    squad.goalkeeping["Performance"]["CS"], squad.goalkeeping["Performance"]["CS%"],
    # Goalkeeping Penalty Kicks
    squad.goalkeeping["Penalty Kicks"]["PKatt"], squad.goalkeeping["Penalty Kicks"]["PKA"],
    squad.goalkeeping["Penalty Kicks"]["PKsv"], squad.goalkeeping["Penalty Kicks"]["PKm"],
    squad.goalkeeping["Penalty Kicks"]["Save%"],
    # Shooting Standard
    squad.shooting["Standard"]["Gls"], squad.shooting["Standard"]["Sh"], 
    squad.shooting["Standard"]["SoT"], squad.shooting["Standard"]["SoT%"], 
    squad.shooting["Standard"]["Sh/90"], squad.shooting["Standard"]["SoT/90"], 
    squad.shooting["Standard"]["G/Sh"], squad.shooting["Standard"]["G/SoT"], 
    squad.shooting["Standard"]["Dist"], squad.shooting["Standard"]["FK"], 
    squad.shooting["Standard"]["PK"], squad.shooting["Standard"]["PKatt"],
    # Shooting Expected
    squad.shooting["Expected"]["xG"], squad.shooting["Expected"]["npxG"], 
    squad.shooting["Expected"]["npxG/Sh"], squad.shooting["Expected"]["G-xG"], 
    squad.shooting["Expected"]["np:G-xG"],


    # Passing Total
    squad.passing["Total"]["Cmp"], squad.passing["Total"]["Att"], 
    squad.passing["Total"]["Cmp%"], squad.passing["Total"]["TotDist"], 
    squad.passing["Total"]["PrgDist"],
    # Passing Short
    squad.passing["Short"]["Cmp"], squad.passing["Short"]["Att"], 
    squad.passing["Short"]["Cmp%"],
    # Passing Medium
    squad.passing["Medium"]["Cmp"], squad.passing["Medium"]["Att"], 
    squad.passing["Medium"]["Cmp%"],
    # Passing Long
    squad.passing["Long"]["Cmp"], squad.passing["Long"]["Att"], 
    squad.passing["Long"]["Cmp%"],
    # Expected Passing
    squad.passing["Expected"]["Ast"], squad.passing["Expected"]["xAG"], 
    squad.passing["Expected"]["xA"], squad.passing["Expected"]["A-xAG"], 
    squad.passing["Expected"]["KP"], squad.passing["Expected"]["1/3"], 
    squad.passing["Expected"]["PPA"], squad.passing["Expected"]["CrsPA"], 
    squad.passing["Expected"]["PrgP"],


    # Pass Types
    squad.pass_types["Pass Types"]["Live"], squad.pass_types["Pass Types"]["Dead"], 
    squad.pass_types["Pass Types"]["FK"], squad.pass_types["Pass Types"]["TB"], 
    squad.pass_types["Pass Types"]["Sw"], squad.pass_types["Pass Types"]["Crs"], 
    squad.pass_types["Pass Types"]["TI"], squad.pass_types["Pass Types"]["CK"],
    #conner Kick
    squad.pass_types["Corner Kicks"]["In"],
    squad.pass_types["Corner Kicks"]["Out"],
    squad.pass_types["Corner Kicks"]["Str"],
    # Pass Outcomes
    squad.pass_types["Outcomes"]["Cmp"], squad.pass_types["Outcomes"]["Off"], 
    squad.pass_types["Outcomes"]["Blocks"],



    #goal_shot_creation
    squad.goal_shot_creation["SCA"]["SCA"],
    squad.goal_shot_creation["SCA"]["SCA90"],
    squad.goal_shot_creation["SCA Types"]["PassLive"],
    squad.goal_shot_creation["SCA Types"]["PassDead"],
    squad.goal_shot_creation["SCA Types"]["TO"],
    squad.goal_shot_creation["SCA Types"]["Sh"],
    squad.goal_shot_creation["SCA Types"]["Fld"],
    squad.goal_shot_creation["SCA Types"]["Def"],
    squad.goal_shot_creation["GCA"]["GCA"],
    squad.goal_shot_creation["GCA"]["GCA90"],
    squad.goal_shot_creation["GCA Types"]["PassLive"],
    squad.goal_shot_creation["GCA Types"]["PassDead"],
    squad.goal_shot_creation["GCA Types"]["TO"],
    squad.goal_shot_creation["GCA Types"]["Sh"],
    squad.goal_shot_creation["GCA Types"]["Fld"],
    squad.goal_shot_creation["GCA Types"]["Def"],
    # Defensive Actions
    squad.defensive_actions["Tackles"]["Tkl"], squad.defensive_actions["Tackles"]["TklW"], 
    squad.defensive_actions["Tackles"]["Def 3rd"], squad.defensive_actions["Tackles"]["Mid 3rd"], 
    squad.defensive_actions["Tackles"]["Att 3rd"],
    squad.defensive_actions["Challenges"]["Tkl"], squad.defensive_actions["Challenges"]["Att"], 
    squad.defensive_actions["Challenges"]["Tkl%"], squad.defensive_actions["Challenges"]["Lost"],
    
    squad.defensive_actions["Blocks"]["Blocks"], 
    squad.defensive_actions["Blocks"]["Sh"],
    squad.defensive_actions["Blocks"]["Pass"],
    squad.defensive_actions["Blocks"]["Int"],
    squad.defensive_actions["Blocks"]["Tkl + Int"],
    squad.defensive_actions["Blocks"]["Clr"],
    squad.defensive_actions["Blocks"]["Err"],


    # Possession
    squad.possession["Touches"]["Touches"], squad.possession["Touches"]["Def Pen"], 
    squad.possession["Touches"]["Def 3rd"], squad.possession["Touches"]["Mid 3rd"], 
    squad.possession["Touches"]["Att 3rd"], squad.possession["Touches"]["Att Pen"], 
    squad.possession["Touches"]["Live"],
    squad.possession["Take-Ons"]["Att"], squad.possession["Take-Ons"]["Succ"], 
    squad.possession["Take-Ons"]["Succ%"], squad.possession["Take-Ons"]["Tkld"], 
    squad.possession["Take-Ons"]["Tkld%"],

    squad.possession["Carries"]["Carries"], squad.possession["Carries"]["TotDist"], 
    squad.possession["Carries"]["ProDist"], squad.possession["Carries"]["ProgC"], 
    squad.possession["Carries"]["1/3"], squad.possession["Carries"]["CPA"], 
    squad.possession["Carries"]["Mis"], squad.possession["Carries"]["Dis"],

    squad.possession["Receiving"]["Rec"],
    squad.possession["Receiving"]["PrgR"],

    # Playing Time
    squad.playing_time_detail["Starts"]["Starts"],
    squad.playing_time_detail["Starts"]["Mn/Start"],
    squad.playing_time_detail["Starts"]["Compl"],
    squad.playing_time_detail["Subs"]["Subs"],
    squad.playing_time_detail["Subs"]["Mn/Sub"],
    squad.playing_time_detail["Subs"]["unSub"],
    squad.playing_time_detail["Team Success"]["PPM"],
    squad.playing_time_detail["Team Success"]["onG"],
    squad.playing_time_detail["Team Success"]["onGA"],
    squad.playing_time_detail["Team Success xG"]["onxG"],
    squad.playing_time_detail["Team Success xG"]["onxGA"],


    # Miscellaneous Stats
    squad.misc_stats["Performance"]["Fls"], squad.misc_stats["Performance"]["Fld"], 
    squad.misc_stats["Performance"]["Off"], squad.misc_stats["Performance"]["Crs"], 
    squad.misc_stats["Performance"]["OG"], squad.misc_stats["Performance"]["Recov"], 
    squad.misc_stats["Aerial Duels"]["Won"], squad.misc_stats["Aerial Duels"]["Lost"], 
    squad.misc_stats["Aerial Duels"]["Won%"]
]


# header2=[]
# for i in header[5:]:
#     header2.append("Median of "+i)
#     header2.append("Mean of "+i)
#     header2.append("Std of "+i)
# print(header2)

header2=[' ',' ','Median of matches_played', 'Mean of matches_played', 'Std of matches_played', 'Median of starts', 'Mean of starts', 'Std of starts', 
         'Median of minutes', 'Mean of minutes', 'Std of minutes', 'Median of non_penalty_goals', 'Mean of non_penalty_goals', 
         'Std of non_penalty_goals', 'Median of penalty_goals', 'Mean of penalty_goals', 'Std of penalty_goals', 'Median of assists', 
         'Mean of assists', 'Std of assists', 'Median of yellow_cards', 'Mean of yellow_cards', 'Std of yellow_cards', 'Median of red_cards', 
         'Mean of red_cards', 'Std of red_cards', 'Median of xG', 'Mean of xG', 'Std of xG', 'Median of npxG', 'Mean of npxG', 'Std of npxG', 
         'Median of xAG', 'Mean of xAG', 'Std of xAG', 'Median of PrgC', 'Mean of PrgC', 'Std of PrgC', 'Median of PrgP', 'Mean of PrgP', 
         'Std of PrgP', 'Median of PrgR', 'Mean of PrgR', 'Std of PrgR', 'Median of per90_Gls', 'Mean of per90_Gls', 'Std of per90_Gls',
           'Median of per90_Ast', 'Mean of per90_Ast', 'Std of per90_Ast', 'Median of per90_G+A', 'Mean of per90_G+A', 'Std of per90_G+A', 
           'Median of per90_G-PK', 'Mean of per90_G-PK', 'Std of per90_G-PK', 'Median of per90_G+A-PK', 'Mean of per90_G+A-PK', 
           'Std of per90_G+A-PK', 'Median of per90_xG', 'Mean of per90_xG', 'Std of per90_xG', 'Median of per90_xAG', 'Mean of per90_xAG', 
           'Std of per90_xAG', 'Median of per90_xG+xAG', 'Mean of per90_xG+xAG', 'Std of per90_xG+xAG', 'Median of per90_npxG', 
           'Mean of per90_npxG', 'Std of per90_npxG', 'Median of per90_npxG+xAG', 'Mean of per90_npxG+xAG', 'Std of per90_npxG+xAG', 
           'Median of GA', 'Mean of GA', 'Std of GA', 'Median of GA90', 'Mean of GA90', 'Std of GA90', 'Median of SoTA', 'Mean of SoTA', 
           'Std of SoTA', 'Median of Saves', 'Mean of Saves', 'Std of Saves', 'Median of Save%', 'Mean of Save%', 'Std of Save%', 'Median of W', 
           'Mean of W', 'Std of W', 'Median of D', 'Mean of D', 'Std of D', 'Median of L', 'Mean of L', 'Std of L', 'Median of CS', 'Mean of CS', 
           'Std of CS', 'Median of CS%', 'Mean of CS%', 'Std of CS%', 'Median of PKatt', 'Mean of PKatt', 'Std of PKatt', 'Median of PKA', 
           'Mean of PKA', 'Std of PKA', 'Median of PKsv', 'Mean of PKsv', 'Std of PKsv', 'Median of PKm', 'Mean of PKm', 'Std of PKm', 
           'Median of GK_Save%', 'Mean of GK_Save%', 'Std of GK_Save%', 'Median of Gls', 'Mean of Gls', 'Std of Gls', 'Median of Sh', 
           'Mean of Sh', 'Std of Sh', 'Median of SoT', 'Mean of SoT', 'Std of SoT', 'Median of SoT%', 'Mean of SoT%', 'Std of SoT%', 
           'Median of Sh/90', 'Mean of Sh/90', 'Std of Sh/90', 'Median of SoT/90', 'Mean of SoT/90', 'Std of SoT/90', 'Median of G/Sh',
            'Mean of G/Sh', 'Std of G/Sh', 'Median of G/SoT', 'Mean of G/SoT', 'Std of G/SoT', 'Median of Dist', 'Mean of Dist', 'Std of Dist',
            'Median of FK', 'Mean of FK', 'Std of FK', 'Median of PK', 'Mean of PK', 'Std of PK', 'Median of PKatt', 'Mean of PKatt', 
            'Std of PKatt', 'Median of xG', 'Mean of xG', 'Std of xG', 'Median of npxG', 'Mean of npxG', 'Std of npxG', 'Median of npxG/Sh', 
            'Mean of npxG/Sh', 'Std of npxG/Sh', 'Median of G-xG', 'Mean of G-xG', 'Std of G-xG', 'Median of np:G-xG', 'Mean of np:G-xG', 
            'Std of np:G-xG', 'Median of Pass_Cmp', 'Mean of Pass_Cmp', 'Std of Pass_Cmp', 'Median of Pass_Att', 'Mean of Pass_Att', 
            'Std of Pass_Att', 'Median of Pass_Cmp%', 'Mean of Pass_Cmp%', 'Std of Pass_Cmp%', 'Median of TotDist', 'Mean of TotDist', 
            'Std of TotDist', 'Median of PrgDist', 'Mean of PrgDist', 'Std of PrgDist', 'Median of Short_Cmp', 'Mean of Short_Cmp', 
            'Std of Short_Cmp', 'Median of Short_Att', 'Mean of Short_Att', 'Std of Short_Att', 'Median of Short_Cmp%', 'Mean of Short_Cmp%', 
            'Std of Short_Cmp%', 'Median of Medium_Cmp', 'Mean of Medium_Cmp', 'Std of Medium_Cmp', 'Median of Medium_Att', 'Mean of Medium_Att', 
            'Std of Medium_Att', 'Median of Medium_Cmp%', 'Mean of Medium_Cmp%', 'Std of Medium_Cmp%', 'Median of Long_Cmp', 
            'Mean of Long_Cmp', 'Std of Long_Cmp', 'Median of Long_Att', 'Mean of Long_Att', 'Std of Long_Att', 'Median of Long_Cmp%', 
            'Mean of Long_Cmp%', 'Std of Long_Cmp%', 'Median of Ast', 'Mean of Ast', 'Std of Ast', 'Median of xAG', 'Mean of xAG', 
            'Std of xAG', 'Median of xA', 'Mean of xA', 'Std of xA', 'Median of A-xAG', 'Mean of A-xAG', 'Std of A-xAG', 'Median of KP', 
            'Mean of KP', 'Std of KP', 'Median of 1/3', 'Mean of 1/3', 'Std of 1/3', 'Median of PPA', 'Mean of PPA', 'Std of PPA', 
            'Median of CrsPA', 'Mean of CrsPA', 'Std of CrsPA', 'Median of PrgP', 'Mean of PrgP', 'Std of PrgP', 'Median of Pass_Live', 
            'Mean of Pass_Live', 'Std of Pass_Live', 'Median of Pass_Dead', 'Mean of Pass_Dead', 'Std of Pass_Dead', 'Median of Pass_FK', 
            'Mean of Pass_FK', 'Std of Pass_FK', 'Median of Pass_TB', 'Mean of Pass_TB', 'Std of Pass_TB', 'Median of Pass_Sw', 'Mean of Pass_Sw', 
            'Std of Pass_Sw', 'Median of Pass_Crs', 'Mean of Pass_Crs', 'Std of Pass_Crs', 'Median of Pass_TI', 'Mean of Pass_TI', 
            'Std of Pass_TI', 'Median of Pass_CK', 'Mean of Pass_CK', 'Std of Pass_CK', 'Median of Pass_Corner_In', 'Mean of Pass_Corner_In', 
            'Std of Pass_Corner_In', 'Median of Pass_Corner_Out', 'Mean of Pass_Corner_Out', 'Std of Pass_Corner_Out', 
            'Median of Pass_Corner_Str', 'Mean of Pass_Corner_Str', 'Std of Pass_Corner_Str', 'Median of Pass_Cmp_outcome', 
            'Mean of Pass_Cmp_outcome', 'Std of Pass_Cmp_outcome', 'Median of Pass_Off', 'Mean of Pass_Off', 'Std of Pass_Off', 
            'Median of Pass_Blocks', 'Mean of Pass_Blocks', 'Std of Pass_Blocks', 'Median of SCA', 'Mean of SCA', 'Std of SCA', 
            'Median of SCA90', 'Mean of SCA90', 'Std of SCA90', 'Median of SCA PassLive', 'Mean of SCA PassLive', 'Std of SCA PassLive', 
            'Median of SCA PassDead', 'Mean of SCA PassDead', 'Std of SCA PassDead', 'Median of SCA TO', 'Mean of SCA TO', 'Std of SCA TO', 
            'Median of SCA Sh', 'Mean of SCA Sh', 'Std of SCA Sh', 'Median of SCA Fld', 'Mean of SCA Fld', 'Std of SCA Fld', 'Median of SCA Def', 
            'Mean of SCA Def', 'Std of SCA Def', 'Median of GCA', 'Mean of GCA', 'Std of GCA', 'Median of GCA90', 'Mean of GCA90', 'Std of GCA90', 
            'Median of GCA PassLive', 'Mean of GCA PassLive', 'Std of GCA PassLive', 'Median of GCA PassDead', 'Mean of GCA PassDead', 
            'Std of GCA PassDead', 'Median of GCA TO', 'Mean of GCA TO', 'Std of GCA TO', 'Median of GCA Sh', 'Mean of GCA Sh', 'Std of GCA Sh', 
            'Median of GCA Fld', 'Mean of GCA Fld', 'Std of GCA Fld', 'Median of GCA Def', 'Mean of GCA Def', 'Std of GCA Def', 'Median of Tkl', 
            'Mean of Tkl', 'Std of Tkl', 'Median of TklW', 'Mean of TklW', 'Std of TklW', 'Median of Def_3rd', 'Mean of Def_3rd', 
            'Std of Def_3rd', 'Median of Mid_3rd', 'Mean of Mid_3rd', 'Std of Mid_3rd', 'Median of Att_3rd', 'Mean of Att_3rd', 'Std of Att_3rd', 
            'Median of Challenges_Tkl', 'Mean of Challenges_Tkl', 'Std of Challenges_Tkl', 'Median of Challenges_Att', 'Mean of Challenges_Att', 
            'Std of Challenges_Att', 'Median of Challenges_Tkl%', 'Mean of Challenges_Tkl%', 'Std of Challenges_Tkl%', 'Median of Challenges_Lost', 
            'Mean of Challenges_Lost', 'Std of Challenges_Lost', 'Median of Blocks', 'Mean of Blocks', 'Std of Blocks', 'Median of Blocks_Sh', 
            'Mean of Blocks_Sh', 'Std of Blocks_Sh', 'Median of Blocks_Pass', 'Mean of Blocks_Pass', 'Std of Blocks_Pass', 'Median of Blocks_Int', 
            'Mean of Blocks_Int', 'Std of Blocks_Int', 'Median of Blocks_Tkl+Int', 'Mean of Blocks_Tkl+Int', 'Std of Blocks_Tkl+Int', 
            'Median of Blocks_Clr', 'Mean of Blocks_Clr', 'Std of Blocks_Clr', 'Median of Blocks_Err', 'Mean of Blocks_Err', 'Std of Blocks_Err', 
            'Median of Touches', 'Mean of Touches', 'Std of Touches', 'Median of Def_Pen', 'Mean of Def_Pen', 'Std of Def_Pen', 'Median of Def_3rd', 
            'Mean of Def_3rd', 'Std of Def_3rd', 'Median of Mid_3rd', 'Mean of Mid_3rd', 'Std of Mid_3rd', 'Median of Att_3rd', 'Mean of Att_3rd', 
            'Std of Att_3rd', 'Median of Att_Pen', 'Mean of Att_Pen', 'Std of Att_Pen', 'Median of Live', 'Mean of Live', 'Std of Live', 
            'Median of Take_Att', 'Mean of Take_Att', 'Std of Take_Att', 'Median of Take_Succ', 'Mean of Take_Succ', 'Std of Take_Succ', 
            'Median of Take_Succ%', 'Mean of Take_Succ%', 'Std of Take_Succ%', 'Median of Take_Tkld', 'Mean of Take_Tkld', 'Std of Take_Tkld', 
            'Median of Take_Tkld%', 'Mean of Take_Tkld%', 'Std of Take_Tkld%', 'Median of Carries', 'Mean of Carries', 'Std of Carries', 
            'Median of Carries_TotDist', 'Mean of Carries_TotDist', 'Std of Carries_TotDist', 'Median of Carries_ProDist', 
            'Mean of Carries_ProDist', 'Std of Carries_ProDist', 'Median of Carries_ProgC', 'Mean of Carries_ProgC', 'Std of Carries_ProgC', 
            'Median of Carries_1/3', 'Mean of Carries_1/3', 'Std of Carries_1/3', 'Median of Carries_CPA', 'Mean of Carries_CPA', 
            'Std of Carries_CPA', 'Median of Carries_Mis', 'Mean of Carries_Mis', 'Std of Carries_Mis', 'Median of Carries_Dis', 
            'Mean of Carries_Dis', 'Std of Carries_Dis', 'Median of Receiving_Rec', 'Mean of Receiving_Rec', 'Std of Receiving_Rec', 
            'Median of Receiving_PrgR', 'Mean of Receiving_PrgR', 'Std of Receiving_PrgR', 'Median of Starts', 'Mean of Starts', 'Std of Starts', 
            'Median of Mn/Start', 'Mean of Mn/Start', 'Std of Mn/Start', 'Median of Compl', 'Mean of Compl', 'Std of Compl', 'Median of Subs', 
            'Mean of Subs', 'Std of Subs', 'Median of Mn/Sub', 'Mean of Mn/Sub', 'Std of Mn/Sub', 'Median of unSub', 'Mean of unSub', 
            'Std of unSub', 'Median of PPM', 'Mean of PPM', 'Std of PPM', 'Median of onG', 'Mean of onG', 'Std of onG', 'Median of onGA', 
            'Mean of onGA', 'Std of onGA', 'Median of onxG', 'Mean of onxG', 'Std of onxG', 'Median of onxGA', 'Mean of onxGA', 'Std of onxGA', 
            'Median of Fls', 'Mean of Fls', 'Std of Fls', 'Median of Fld', 'Mean of Fld', 'Std of Fld', 'Median of Off', 'Mean of Off', 
            'Std of Off', 'Median of Crs', 'Mean of Crs', 'Std of Crs', 'Median of OG', 'Mean of OG', 'Std of OG', 'Median of Recov', 
            'Mean of Recov', 'Std of Recov', 'Median of Aerial_Won', 'Mean of Aerial_Won', 'Std of Aerial_Won', 'Median of Aerial_Lost', 
            'Mean of Aerial_Lost', 'Std of Aerial_Lost', 'Median of Aerial_Won%', 'Mean of Aerial_Won%', 'Std of Aerial_Won%']


def row2(stt,teamName,median_value_list,mean_value_list,std_dev_list):
    arr=[stt,teamName]
    for i in range(len(median_value_list)):
        arr.append(median_value_list[i])
        arr.append(mean_value_list[i])
        arr.append(std_dev_list[i])
    return arr