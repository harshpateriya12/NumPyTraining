import numpy as np

def highest_scoring_match(match_ids, batsman_runs):
    # Step 1: Unique matches
    unique_matches = np.unique(match_ids)

    total_runs = []

    # Step 2: Compute total runs per match
    for match in unique_matches:
        mask = match_ids == match
        runs = np.sum(batsman_runs[mask])
        total_runs.append(runs)

    total_runs = np.array(total_runs)

    # Step 3: Find index of max runs
    max_index = np.argmax(total_runs)

    # Step 4: Get match ID and runs
    max_match_id = int(unique_matches[max_index])
    max_runs = int(total_runs[max_index])

    return max_match_id, max_runs