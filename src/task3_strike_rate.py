import numpy as np

def strike_rate_per_batter(batter, batsman_runs):
    # Step 1: Unique batters
    unique_batters = np.unique(batter)

    strike_rates = []

    for player in unique_batters:
        mask = batter == player

        # Step 2: Balls faced
        balls = np.sum(mask)

        # Step 3: Total runs
        runs = np.sum(batsman_runs[mask])

        # Step 4: Strike rate calculation
        if balls > 0:
            sr = (runs / balls) * 100
        else:
            sr = 0

        strike_rates.append((player, round(sr, 2)))

    return strike_rates