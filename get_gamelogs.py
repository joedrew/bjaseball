#!/usr/bin/env python

from pybaseball import team_ids
from pybaseball import teams
from pybaseball import schedule_and_record

import pandas as pd

years = range(1900, 2021)

def team_ids_for_year(year):
    teams = team_ids(year)
    idx, teamIDs = pd.factorize(teams['teamID'])
    return teamIDs

for year in years:
    team_ids = team_ids_for_year(year)

    for team_id in team_ids:
        print(year, team_id)
        schedule_and_record(year, team_id).to_csv(f"{year}-{team_id}.csv")
