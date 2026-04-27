import numpy as np

def top_5_batters(batter, batsman_runs):
    # Step 1: Get unique batters
    unique_batters = np.unique(batter)

    total_runs = []

    # Step 2: Calculate total runs per batter
    for player in unique_batters:
        mask = batter == player
        runs = np.sum(batsman_runs[mask])
        total_runs.append(runs)

    total_runs = np.array(total_runs)

    # Step 3: Sort in descending order
    sorted_indices = np.argsort(total_runs)[::-1]

    # Step 4: Pick top 5
    top_5 = []
    for i in sorted_indices[:5]:
        top_5.append((unique_batters[i], int(total_runs[i])))

    return top_5