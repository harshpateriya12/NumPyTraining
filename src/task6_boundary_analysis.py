import numpy as np

def boundary_analysis(batsman_runs, batting_team):
    # Step 1: Count fours
    fours = np.sum(batsman_runs == 4)

    # Step 2: Count sixes
    sixes = np.sum(batsman_runs == 6)

    # Step 3: Total boundaries mask
    boundary_mask = (batsman_runs == 4) | (batsman_runs == 6)

    # Step 4: Get teams for boundary deliveries
    boundary_teams = batting_team[boundary_mask]

    # Step 5: Count boundaries per team
    unique_teams = np.unique(boundary_teams)

    team_counts = []

    for team in unique_teams:
        mask = boundary_teams == team
        count = np.sum(mask)
        team_counts.append((team, int(count)))

    # Step 6: Find team with max boundaries
    team_counts = np.array(team_counts, dtype=object)

    max_index = np.argmax(team_counts[:, 1].astype(int))
    top_team = team_counts[max_index]

    return fours, sixes, top_team