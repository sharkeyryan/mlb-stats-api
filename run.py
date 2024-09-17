import statsapi
import pprint
import csv

SEASON_DATA = statsapi.latest_season()

def get_schedule(start_date=None,end_date=None,team='',opponent=''):
    games = statsapi.schedule(start_date=start_date,end_date=end_date,team=team, opponent=opponent)
    
    return games

def generate_team_record(team_id=None):
    games = get_schedule(start_date=SEASON_DATA['regularSeasonStartDate'],end_date=SEASON_DATA['regularSeasonEndDate'],team=team_id)
    
    team_won = 0
    team_lost = 0
    team_lost_by_two = 0

    for g in games:
        if g['game_type'] != 'R' or g['status'] != 'Final':
            continue

        if g['home_id'] == team_id:
            team_score = g['home_score']
            team_name = g['home_name']
            opp_score = g['away_score']
        else:
            team_score = g['away_score']
            team_name = g['away_name']
            opp_score = g['home_score']

        if team_score > opp_score:
            team_won += 1
        else:
            team_lost += 1

            if (opp_score - team_score) <= 2:
                team_lost_by_two += 1

    row = [f'"{team_name}"', team_won, team_lost, team_lost_by_two]

    return row

def get_standings():
    print("Getting standings!")

    standings = statsapi.standings_data(
        leagueId="103,104", 
        division="all", 
        include_wildcard=True, 
        season=None, 
        standingsTypes=None, 
        date=None
    )

    return standings

def get_mlb_teams():
    print("Getting MLB teams...")

    teams = statsapi.get(
        "teams",
        {"leagueIds": "103,104"}
    )

    return teams['teams']

with open('output.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, quotechar="'")
    headers = [f'"Team"', f'"Wins"', f'"Losses"', f'"Losses By Two or Less"']
    writer.writerow(headers)

    teams = get_mlb_teams()

    print("Getting MLB team records...")

    for team in teams:
        row = generate_team_record(team_id=team['id'])
        writer.writerow(row)
    
    print("Done!")