import numpy as np

def runs_per_over(overs, batsman_runs):
    avg_runs_per_over = []

    # Loop only over 20 overs (allowed)
    for i in range(20):
        # Step 1: mask for that over
        mask = overs == i

        # Step 2: total runs in that over
        total_runs = np.sum(batsman_runs[mask])

        # Step 3: number of balls in that over
        balls = np.sum(mask)

        # Step 4: average runs
        if balls > 0:
            avg = total_runs / balls
        else:
            avg = 0

        avg_runs_per_over.append(round(avg, 2))

    return avg_runs_per_over