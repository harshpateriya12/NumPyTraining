import numpy as np

def economy_rate_per_bowler(bowler, batsman_runs):
    # Step 1: Unique bowlers
    unique_bowlers = np.unique(bowler)

    economy_list = []

    for player in unique_bowlers:
        mask = bowler == player

        # Step 2: Balls bowled
        balls = np.sum(mask)

        # Step 3: Runs conceded
        runs = np.sum(batsman_runs[mask])

        # Step 4: Convert balls to overs
        overs = balls / 6

        # Step 5: Economy calculation
        if overs > 0:
            economy = runs / overs
        else:
            economy = 0

        economy_list.append((player, round(economy, 2)))

    return economy_list