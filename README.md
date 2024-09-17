# mlb-stats-api

This project uses MLB stats for teams and their current season schedule to see w/L ratio and how many games they have lost by 2 or less runs. Generates a CSV output for analysis.

Working to add a Django Project to host an API to deliver these findings upon request from a front-end dashboard.

This project uses a Python wrapper for the official MLB Stats API found here: https://github.com/toddrob99/MLB-StatsAPI

Refer to Wiki/Documentation here: https://github.com/toddrob99/MLB-StatsAPI/wiki

# Notes

American and NAtional League Teams and `id` values from MLB API.

```python
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
```