import numpy as np

def death_overs_analysis(overs, batsman_runs, batting_team):
    # Step 1: Filter death overs
    death_mask = (overs >= 15) & (overs <= 19)

    # Step 2: Total runs in death overs
    total_runs = np.sum(batsman_runs[death_mask])

    # Step 3: Teams in death overs
    death_teams = batting_team[death_mask]
    death_runs = batsman_runs[death_mask]

    # Step 4: Unique teams
    unique_teams = np.unique(death_teams)

    team_runs = []

    for team in unique_teams:
        mask = death_teams == team
        runs = np.sum(death_runs[mask])
        team_runs.append((team, int(runs)))

    # Step 5: Find team with max runs
    team_runs = np.array(team_runs, dtype=object)

    max_index = np.argmax(team_runs[:, 1].astype(int))
    top_team = team_runs[max_index]

    return int(total_runs), top_team