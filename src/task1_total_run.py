import numpy as np

def total_runs_per_match(match_ids, batsman_runs):
    # Step 1: Get unique match IDs
    unique_matches = np.unique(match_ids)

    result = []

    # Step 2: Loop through each match (allowed here since unique matches are small)
    for match in unique_matches:
        # Step 3: Boolean mask
        mask = match_ids == match

        # Step 4: Sum runs for that match
        total_runs = np.sum(batsman_runs[mask])

        # Step 5: Store result
        result.append((int(match), int(total_runs)))

    return result