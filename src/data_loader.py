import numpy as np

def load_deliveries_data(file_path):
    data = np.genfromtxt(
        file_path,
        delimiter=',',
        dtype=str,
        skip_header=1,
        filling_values="0"
    )

    print("Data Shape:", data.shape)

    # Correct column extraction
    match_ids = data[:, 0].astype(int)
    batting_team = data[:, 2]
    overs = data[:, 4].astype(int)
    batter = data[:, 6]
    bowler = data[:, 7]
    batsman_runs = data[:, 9].astype(int)

    return match_ids, batting_team, batter, bowler, batsman_runs, overs