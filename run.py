import statsapi
import pprint
import csv

SEASON_DATA = statsapi.latest_season()
# pprint.pprint(SEASON_DATA)

def get_schedule(start_date=None,end_date=None,team='',opponent=''):
    games = statsapi.schedule(start_date=start_date,end_date=end_date,team=team, opponent=opponent)
    # games = statsapi.schedule(start_date='07/01/2018',end_date='07/31/2018',team=143,opponent=121)
    
    # print("games: " + str(len(games)))
    # pprint.pprint(games[0])

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
            opp_name = g['away_name']
            opp_id = g['away_id']
        else:
            team_score = g['away_score']
            team_name = g['away_name']
            opp_score = g['home_score']
            opp_name = g['home_name']
            opp_id = g['home_id']

        if team_score > opp_score:
            outcome = "beat"
            team_won += 1
        else:
            outcome = "lost to"
            team_lost += 1

            if (opp_score - team_score) <= 1:
                team_lost_by_two += 1

        # print(f"The {team_name}({team_score}) {outcome} the {opp_name}(id: {opp_id})({opp_score}) on {g['game_date']}")
        # row = [team_name, team_score, outcome, opp_name, opp_id, opp_score, g['game_date']]
        # writer.writerow(row)

    # print(f"The {team_name} won {team_won} games.")
    # print(f"The {team_name} lost {team_lost} games.")
    # print(f"The {team_name} lost {team_lost_by_two} games by two or less runs.")
    row = [f'"{team_name}"', team_won, team_lost, team_lost_by_two]
    # writer.writerow(row)

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

    # pprint.pprint(standings)

    return standings

def get_mlb_teams():
    print("Getting MLB teams...")

    teams = statsapi.get(
        "teams",
        {"leagueIds": "103,104"}
    )

    # pprint.pprint(teams['teams'])
    # print("Team count: " + str(len(teams['teams'])))
    # pprint.pprint(teams['teams'][0])

    return teams['teams']



team_name = 'San Francisco Giants'
team_id = 137

opp_name = ''
opp_id = 0

teams_dict = {
    'Angels': 108,
    'Astros': 117,
    'Athletics': 133,
    'Blue Jays': 141,
    'Braves': 144,
    'Brewers': 158,
    'Cardinals': 138,
    'Cubs': 112,
    'Diamondbacks': 109,
    'Dodgers': 119,
    'Giants': 137,
    'Guardians': 114,
    'Mariners': 136,
    'Marlins': 146,
    'Mets': 121,
    'Nationals': 120,
    'Orioles': 110,
    'Padres': 135,
    'Phillies': 143,
    'Pirates': 134,
    'Rangers': 140,
    'Rays': 139,
    'Red Sox': 111,
    'Reds': 113,
    'Rockies': 115,
    'Royals': 118,
    'Tigers': 116,
    'Twins': 142,
    'White Sox': 145,
    'Yankees': 147
 }

# Open a CSV file for writing
with open('output.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, quotechar="'")
    headers = [f'"Team"', f'"Wins"', f'"Losses"', f'"Losses By Two or Less"']
    writer.writerow(headers)
    # get_standings()

    teams = get_mlb_teams()

    print("Getting MLB team records...")

    for team in teams:
        row = generate_team_record(team_id=team['id'])
        writer.writerow(row)
    
    print("Done!")
        