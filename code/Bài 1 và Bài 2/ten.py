class Player:
    def __init__(self, name, nation, position, team, age):
        self.name = name
        self.nation = nation
        self.team = team
        self.position = position
        self.age = age

        self.playing_time = {
            "matches_played": "N/a",
            "starts": "N/a",
            "minutes": "N/a"
        }

        # Performance
        self.performance = {
            "non_penalty_goals": "N/a",
            "penalty_goals": "N/a",
            "assists": "N/a",
            "yellow_cards": "N/a",
            "red_cards": "N/a"
        }

        # Expected
        self.expected = {
            "xG": "N/a",
            "npxG": "N/a",
            "xAG": "N/a"
        }

        # Progression
        self.progression = {
            "PrgC": "N/a",
            "PrgP": "N/a",
            "PrgR": "N/a"
        }

        # Per 90 minutes
        self.per_90 = {
            "Gls": "N/a",
            "Ast": "N/a",
            "G+A": "N/a",
            "G-PK": "N/a",
            "G+A-PK": "N/a",
            "xG": "N/a",
            "xAG": "N/a",
            "xG+xAG": "N/a",
            "npxG": "N/a",
            "npxG+xAG": "N/a"
        }

        # Goalkeeping
        self.goalkeeping = {
            "Performance": {
                "GA": "N/a",
                "GA90": "N/a",
                "SoTA": "N/a",
                "Saves": "N/a",
                "Save%": "N/a",
                "W": "N/a",
                "D": "N/a",
                "L": "N/a",
                "CS": "N/a",
                "CS%": "N/a"
            },
            "Penalty Kicks": {
                "PKatt": "N/a",
                "PKA": "N/a",
                "PKsv": "N/a",
                "PKm": "N/a",
                "Save%": "N/a"
            }
        }

        # Shooting
        self.shooting = {
            "Standard": {
                "Gls": "N/a",
                "Sh": "N/a",
                "SoT": "N/a",
                "SoT%": "N/a",
                "Sh/90": "N/a",
                "SoT/90": "N/a",
                "G/Sh": "N/a",
                "G/SoT": "N/a",
                "Dist": "N/a",
                "FK": "N/a",
                "PK": "N/a",
                "PKatt": "N/a"
            },
            "Expected": {
                "xG": "N/a",
                "npxG": "N/a",
                "npxG/Sh": "N/a",
                "G-xG": "N/a",
                "np:G-xG": "N/a"
            }
        }

        # Passing
        self.passing = {
            "Total": {
                "Cmp": "N/a",
                "Att": "N/a",
                "Cmp%": "N/a",
                "TotDist": "N/a",
                "PrgDist": "N/a"
            },
            "Short": {
                "Cmp": "N/a",
                "Att": "N/a",
                "Cmp%": "N/a"
            },
            "Medium": {
                "Cmp": "N/a",
                "Att": "N/a",
                "Cmp%": "N/a"
            },
            "Long": {
                "Cmp": "N/a",
                "Att": "N/a",
                "Cmp%": "N/a"
            },
            "Expected": {
                "Ast": "N/a",
                "xAG": "N/a",
                "xA": "N/a",
                "A-xAG": "N/a",
                "KP": "N/a",
                "1/3": "N/a",
                "PPA": "N/a",
                "CrsPA": "N/a",
                "PrgP": "N/a"
            }
        }

        # Pass Types
        self.pass_types = {
            "Pass Types": {
                "Live": "N/a",
                "Dead": "N/a",
                "FK": "N/a",
                "TB": "N/a",
                "Sw": "N/a",
                "Crs": "N/a",
                "TI": "N/a",
                "CK": "N/a"
            },
            "Corner Kicks": {
                "In": "N/a",
                "Out": "N/a",
                "Str": "N/a"
            },
            "Outcomes": {
                "Cmp": "N/a",
                "Off": "N/a",
                "Blocks": "N/a"
            }
        }

        # Goal and Shot Creation
        self.goal_shot_creation = {
            "SCA": {
                "SCA": "N/a",
                "SCA90": "N/a"
            },
            "SCA Types": {
                "PassLive": "N/a",
                "PassDead": "N/a",
                "TO": "N/a",
                "Sh": "N/a",
                "Fld": "N/a",
                "Def": "N/a"
            },
            "GCA": {
                "GCA": "N/a",
                "GCA90": "N/a"
            },
            "GCA Types": {
                "PassLive": "N/a",
                "PassDead": "N/a",
                "TO": "N/a",
                "Sh": "N/a",
                "Fld": "N/a",
                "Def": "N/a"
            }
        }

        # Defensive Actions
        self.defensive_actions = {
            "Tackles": {
                "Tkl": "N/a",
                "TklW": "N/a",
                "Def 3rd": "N/a",
                "Mid 3rd": "N/a",
                "Att 3rd": "N/a"
            },
            "Challenges": {
                "Tkl": "N/a",
                "Att": "N/a",
                "Tkl%": "N/a",
                "Lost": "N/a"
            },
            "Blocks": {
                "Blocks": "N/a",
                "Sh": "N/a",
                "Pass": "N/a",
                "Int": "N/a",
                "Tkl + Int": "N/a",
                "Clr": "N/a",
                "Err": "N/a"
            }
        }

        # Possession
        self.possession = {
            "Touches": {
                "Touches": "N/a",
                "Def Pen": "N/a",
                "Def 3rd": "N/a",
                "Mid 3rd": "N/a",
                "Att 3rd": "N/a",
                "Att Pen": "N/a",
                "Live": "N/a"
            },
            "Take-Ons": {
                "Att": "N/a",
                "Succ": "N/a",
                "Succ%": "N/a",
                "Tkld": "N/a",
                "Tkld%": "N/a"
            },
            "Carries": {
                "Carries": "N/a",
                "TotDist": "N/a",
                "ProDist": "N/a",
                "ProgC": "N/a",
                "1/3": "N/a",
                "CPA": "N/a",
                "Mis": "N/a",
                "Dis": "N/a"
            },
            "Receiving": {
                "Rec": "N/a",
                "PrgR": "N/a"
            }
        }

        # Playing Time
        self.playing_time_detail = {
            "Starts": {
                "Starts": "N/a",
                "Mn/Start": "N/a",
                "Compl": "N/a"
            },
            "Subs": {
                "Subs": "N/a",
                "Mn/Sub": "N/a",
                "unSub": "N/a"
            },
            "Team Success": {
                "PPM": "N/a",
                "onG": "N/a",
                "onGA": "N/a"
            },
            "Team Success xG": {
                "onxG": "N/a",
                "onxGA": "N/a"
            }
        }

        # Miscellaneous Stats
        self.misc_stats = {
            "Performance": {
                "Fls": "N/a",
                "Fld": "N/a",
                "Off": "N/a",
                "Crs": "N/a",
                "OG": "N/a",
                "Recov": "N/a"
            },
            "Aerial Duels": {
                "Won": "N/a",
                "Lost": "N/a",
                "Won%": "N/a"
            }
        }

    def setPlaying_time(self,arr):
        self.playing_time["matches_played"]=arr[0]
        self.playing_time["starts"]=arr[1]
        self.playing_time["minutes"]=arr[2]
    
    def setPerformance(self, arr):
        self.performance["non_penalty_goals"] = arr[0]
        self.performance["penalty_goals"] = arr[1]
        self.performance["assists"] = arr[2]
        self.performance["yellow_cards"] = arr[3]
        self.performance["red_cards"] = arr[4]

    def setExpected(self, arr):
        self.expected["xG"] = arr[0]
        self.expected["npxG"] = arr[1]
        self.expected["xAG"] = arr[2]

    def setProgression(self, arr):
        self.progression["PrgC"] = arr[0]
        self.progression["PrgP"] = arr[1]
        self.progression["PrgR"] = arr[2]

    def setPer90(self, arr):
        self.per_90["Gls"] = arr[0]
        self.per_90["Ast"] = arr[1]
        self.per_90["G+A"] = arr[2]
        self.per_90["G-PK"] = arr[3]
        self.per_90["G+A-PK"] = arr[4]
        self.per_90["xG"] = arr[5]
        self.per_90["xAG"] = arr[6]
        self.per_90["xG+xAG"] = arr[7]
        self.per_90["npxG"] = arr[8]
        self.per_90["npxG+xAG"] = arr[9]

    def setGoalkeeping(self, performance_arr, penalty_arr):
        self.goalkeeping["Performance"]["GA"] = performance_arr[0]
        self.goalkeeping["Performance"]["GA90"] = performance_arr[1]
        self.goalkeeping["Performance"]["SoTA"] = performance_arr[2]
        self.goalkeeping["Performance"]["Saves"] = performance_arr[3]
        self.goalkeeping["Performance"]["Save%"] = performance_arr[4]
        self.goalkeeping["Performance"]["W"] = performance_arr[5]
        self.goalkeeping["Performance"]["D"] = performance_arr[6]
        self.goalkeeping["Performance"]["L"] = performance_arr[7]
        self.goalkeeping["Performance"]["CS"] = performance_arr[8]
        self.goalkeeping["Performance"]["CS%"] = performance_arr[9]

        self.goalkeeping["Penalty Kicks"]["PKatt"] = penalty_arr[0]
        self.goalkeeping["Penalty Kicks"]["PKA"] = penalty_arr[1]
        self.goalkeeping["Penalty Kicks"]["PKsv"] = penalty_arr[2]
        self.goalkeeping["Penalty Kicks"]["PKm"] = penalty_arr[3]
        self.goalkeeping["Penalty Kicks"]["Save%"] = penalty_arr[4]

    def setShooting(self, standard_arr, expected_arr):
        self.shooting["Standard"]["Gls"] = standard_arr[0]
        self.shooting["Standard"]["Sh"] = standard_arr[1]
        self.shooting["Standard"]["SoT"] = standard_arr[2]
        self.shooting["Standard"]["SoT%"] = standard_arr[3]
        self.shooting["Standard"]["Sh/90"] = standard_arr[4]
        self.shooting["Standard"]["SoT/90"] = standard_arr[5]
        self.shooting["Standard"]["G/Sh"] = standard_arr[6]
        self.shooting["Standard"]["G/SoT"] = standard_arr[7]
        self.shooting["Standard"]["Dist"] = standard_arr[8]
        self.shooting["Standard"]["FK"] = standard_arr[9]
        self.shooting["Standard"]["PK"] = standard_arr[10]
        self.shooting["Standard"]["PKatt"] = standard_arr[11]

        self.shooting["Expected"]["xG"] = expected_arr[0]
        self.shooting["Expected"]["npxG"] = expected_arr[1]
        self.shooting["Expected"]["npxG/Sh"] = expected_arr[2]
        self.shooting["Expected"]["G-xG"] = expected_arr[3]
        self.shooting["Expected"]["np:G-xG"] = expected_arr[4]

    def setPassing(self, total_arr, short_arr, medium_arr, long_arr, expected_arr):
        self.passing["Total"]["Cmp"] = total_arr[0]
        self.passing["Total"]["Att"] = total_arr[1]
        self.passing["Total"]["Cmp%"] = total_arr[2]
        self.passing["Total"]["TotDist"] = total_arr[3]
        self.passing["Total"]["PrgDist"] = total_arr[4]

        self.passing["Short"]["Cmp"] = short_arr[0]
        self.passing["Short"]["Att"] = short_arr[1]
        self.passing["Short"]["Cmp%"] = short_arr[2]

        self.passing["Medium"]["Cmp"] = medium_arr[0]
        self.passing["Medium"]["Att"] = medium_arr[1]
        self.passing["Medium"]["Cmp%"] = medium_arr[2]

        self.passing["Long"]["Cmp"] = long_arr[0]
        self.passing["Long"]["Att"] = long_arr[1]
        self.passing["Long"]["Cmp%"] = long_arr[2]

        self.passing["Expected"]["Ast"] = expected_arr[0]
        self.passing["Expected"]["xAG"] = expected_arr[1]
        self.passing["Expected"]["xA"] = expected_arr[2]
        self.passing["Expected"]["A-xAG"] = expected_arr[3]
        self.passing["Expected"]["KP"] = expected_arr[4]
        self.passing["Expected"]["1/3"] = expected_arr[5]
        self.passing["Expected"]["PPA"] = expected_arr[6]
        self.passing["Expected"]["CrsPA"] = expected_arr[7]
        self.passing["Expected"]["PrgP"] = expected_arr[8]

    def setPassTypes(self, pass_types_arr, corner_kicks_arr, outcomes_arr):
        self.pass_types["Pass Types"]["Live"] = pass_types_arr[0]
        self.pass_types["Pass Types"]["Dead"] = pass_types_arr[1]
        self.pass_types["Pass Types"]["FK"] = pass_types_arr[2]
        self.pass_types["Pass Types"]["TB"] = pass_types_arr[3]
        self.pass_types["Pass Types"]["Sw"] = pass_types_arr[4]
        self.pass_types["Pass Types"]["Crs"] = pass_types_arr[5]
        self.pass_types["Pass Types"]["TI"] = pass_types_arr[6]
        self.pass_types["Pass Types"]["CK"] = pass_types_arr[7]

        self.pass_types["Corner Kicks"]["In"] = corner_kicks_arr[0]
        self.pass_types["Corner Kicks"]["Out"] = corner_kicks_arr[1]
        self.pass_types["Corner Kicks"]["Str"] = corner_kicks_arr[2]

        self.pass_types["Outcomes"]["Cmp"] = outcomes_arr[0]
        self.pass_types["Outcomes"]["Off"] = outcomes_arr[1]
        self.pass_types["Outcomes"]["Blocks"] = outcomes_arr[2]

    def setGoalShotCreation(self, sca_arr,sca_types_arr, gca_arr, gca_types_arr):
        self.goal_shot_creation["SCA"]["SCA"] = sca_arr[0]
        self.goal_shot_creation["SCA"]["SCA90"] = sca_arr[1]

        self.goal_shot_creation["SCA Types"]["PassLive"] = sca_types_arr[0]
        self.goal_shot_creation["SCA Types"]["PassDead"] = sca_types_arr[1]
        self.goal_shot_creation["SCA Types"]["TO"] = sca_types_arr[2]
        self.goal_shot_creation["SCA Types"]["Sh"] = sca_types_arr[3]
        self.goal_shot_creation["SCA Types"]["Fld"] = sca_types_arr[4]
        self.goal_shot_creation["SCA Types"]["Def"] = sca_types_arr[5]

        self.goal_shot_creation["GCA"]["GCA"] = gca_arr[0]
        self.goal_shot_creation["GCA"]["GCA90"] = gca_arr[1]

        self.goal_shot_creation["GCA Types"]["PassLive"] = gca_types_arr[0]
        self.goal_shot_creation["GCA Types"]["PassDead"] = gca_types_arr[1]
        self.goal_shot_creation["GCA Types"]["TO"] = gca_types_arr[2]
        self.goal_shot_creation["GCA Types"]["Sh"] = gca_types_arr[3]
        self.goal_shot_creation["GCA Types"]["Fld"] = gca_types_arr[4]
        self.goal_shot_creation["GCA Types"]["Def"] = gca_types_arr[5]

    def setDefensiveActions(self, tackles_arr, challenges_arr, blocks_arr):
        self.defensive_actions["Tackles"]["Tkl"] = tackles_arr[0]
        self.defensive_actions["Tackles"]["TklW"] = tackles_arr[1]
        self.defensive_actions["Tackles"]["Def 3rd"] = tackles_arr[2]
        self.defensive_actions["Tackles"]["Mid 3rd"] = tackles_arr[3]
        self.defensive_actions["Tackles"]["Att 3rd"] = tackles_arr[4]

        self.defensive_actions["Challenges"]["Tkl"] = challenges_arr[0]
        self.defensive_actions["Challenges"]["Att"] = challenges_arr[1]
        self.defensive_actions["Challenges"]["Tkl%"] = challenges_arr[2]
        self.defensive_actions["Challenges"]["Lost"] = challenges_arr[3]

        self.defensive_actions["Blocks"]["Blocks"] = blocks_arr[0]
        self.defensive_actions["Blocks"]["Sh"] = blocks_arr[1]
        self.defensive_actions["Blocks"]["Pass"] = blocks_arr[2]
        self.defensive_actions["Blocks"]["Int"] = blocks_arr[3]
        self.defensive_actions["Blocks"]["Tkl + Int"] = blocks_arr[4]
        self.defensive_actions["Blocks"]["Clr"] = blocks_arr[5]
        self.defensive_actions["Blocks"]["Err"] = blocks_arr[6]

    def setPossession(self, touches_arr, take_ons_arr, carries_arr, receiving_arr):
        self.possession["Touches"]["Touches"] = touches_arr[0]
        self.possession["Touches"]["Def Pen"] = touches_arr[1]
        self.possession["Touches"]["Def 3rd"] = touches_arr[2]
        self.possession["Touches"]["Mid 3rd"] = touches_arr[3]
        self.possession["Touches"]["Att 3rd"] = touches_arr[4]
        self.possession["Touches"]["Att Pen"] = touches_arr[5]
        self.possession["Touches"]["Live"] = touches_arr[6]

        self.possession["Take-Ons"]["Att"] = take_ons_arr[0]
        self.possession["Take-Ons"]["Succ"] = take_ons_arr[1]
        self.possession["Take-Ons"]["Succ%"] = take_ons_arr[2]
        self.possession["Take-Ons"]["Tkld"] = take_ons_arr[3]
        self.possession["Take-Ons"]["Tkld%"] = take_ons_arr[4]

        self.possession["Carries"]["Carries"] = carries_arr[0]
        self.possession["Carries"]["TotDist"] = carries_arr[1]
        self.possession["Carries"]["ProDist"] = carries_arr[2]
        self.possession["Carries"]["ProgC"] = carries_arr[3]
        self.possession["Carries"]["1/3"] = carries_arr[4]
        self.possession["Carries"]["CPA"] = carries_arr[5]
        self.possession["Carries"]["Mis"] = carries_arr[6]
        self.possession["Carries"]["Dis"] = carries_arr[7]

        self.possession["Receiving"]["Rec"] = receiving_arr[0]
        self.possession["Receiving"]["PrgR"] = receiving_arr[1]

    def setPlayingTimeDetail(self, starts_arr, subs_arr, team_success_arr, team_success_xg_arr):
        self.playing_time_detail["Starts"]["Starts"] = starts_arr[0]
        self.playing_time_detail["Starts"]["Mn/Start"] = starts_arr[1]
        self.playing_time_detail["Starts"]["Compl"] = starts_arr[2]

        self.playing_time_detail["Subs"]["Subs"] = subs_arr[0]
        self.playing_time_detail["Subs"]["Mn/Sub"] = subs_arr[1]
        self.playing_time_detail["Subs"]["unSub"] = subs_arr[2]

        self.playing_time_detail["Team Success"]["PPM"] = team_success_arr[0]
        self.playing_time_detail["Team Success"]["onG"] = team_success_arr[1]
        self.playing_time_detail["Team Success"]["onGA"] = team_success_arr[2]

        self.playing_time_detail["Team Success xG"]["onxG"] = team_success_xg_arr[0]
        self.playing_time_detail["Team Success xG"]["onxGA"] = team_success_xg_arr[1]

    def setMiscStats(self, performance_arr, aerial_duels_arr):
        self.misc_stats["Performance"]["Fls"] = performance_arr[0]
        self.misc_stats["Performance"]["Fld"] = performance_arr[1]
        self.misc_stats["Performance"]["Off"] = performance_arr[2]
        self.misc_stats["Performance"]["Crs"] = performance_arr[3]
        self.misc_stats["Performance"]["OG"] = performance_arr[4]
        self.misc_stats["Performance"]["Recov"] = performance_arr[5]

        self.misc_stats["Aerial Duels"]["Won"] = aerial_duels_arr[0]
        self.misc_stats["Aerial Duels"]["Lost"] = aerial_duels_arr[1]
        self.misc_stats["Aerial Duels"]["Won%"] = aerial_duels_arr[2]

    def __str__(self) -> str:
        return self.name+" "+str(self.age)+" "+self.team+"\n"+str(self.performance)+ \
                    "\n"+str(self.per_90)+ \
                    "\n"+str(self.goalkeeping)+\
                    "\n"+str(self.shooting)
    def to_dict(self):
        return self.__dict__

class Player_Manager:
    def __init__(self) -> None:
        self.list_player=[]


    def add_Player(self,player):
        self.list_player.append(player)

    def findPlayerByNameandTeam(self,name,team):
        for i in self.list_player:
            if i.name==name and i.team==team:
                return i
        return None
    def filtering(self):
        self.list_player = list(filter(lambda p: p.playing_time["minutes"] != 'N/a' and float(p.playing_time["minutes"]) > 90, self.list_player))

    def show(self):
        for i in self.list_player:
            print(i)

    def sortingByName(self):
        self.list_player=sorted(self.list_player,key=lambda x:(x.name,-x.age))
