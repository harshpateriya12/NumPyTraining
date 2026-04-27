from data_loader import load_deliveries_data
from task1_total_run import total_runs_per_match

def main():
    # FIX: correct relative path (since running inside src/)
    file_path = "../data/deliveries.csv"

    # Load data
    match_ids, batting_team, batter, bowler, batsman_runs, overs = load_deliveries_data(file_path)

    # Task 1: Total Runs per Match
    results = total_runs_per_match(match_ids, batsman_runs)

    # Print first 10 results
    print("\n--- Total Runs Per Match ---")
    for match_id, runs in results[:10]:
        print(f"Match {match_id}: Total Runs = {runs}")

if __name__ == "__main__":
    main()