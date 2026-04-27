from data_loader import load_deliveries_data
from task1_total_run import total_runs_per_match
from task2_top_batters import top_5_batters
from task3_strike_rate import strike_rate_per_batter

def main():
    file_path = "../data/deliveries.csv"

    match_ids, batting_team, batter, bowler, batsman_runs, overs = load_deliveries_data(file_path)

    # Task 1
    results = total_runs_per_match(match_ids, batsman_runs)

    print("\n--- Total Runs Per Match ---")
    for match_id, runs in results[:5]:
        print(f"Match {match_id}: Total Runs = {runs}")

    # Task 2
    top_batters = top_5_batters(batter, batsman_runs)

    print("\n--- Top 5 Batters ---")
    for player, runs in top_batters:
        print(f"{player}: {runs} runs")

    # Task 3: Strike Rate
    strike_rates = strike_rate_per_batter(batter, batsman_runs)

    print("\n--- Strike Rate (Top 5) ---")

# Sort by strike rate descending
    strike_rates_sorted = sorted(strike_rates, key=lambda x: x[1], reverse=True)

    for player, sr in strike_rates_sorted[:5]:
         print(f"{player}: {sr}")

if __name__ == "__main__":
    main()