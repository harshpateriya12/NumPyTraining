from data_loader import load_deliveries_data
from task1_total_run import total_runs_per_match
from task2_top_batters import top_5_batters
from task3_strike_rate import strike_rate_per_batter
from task4_economy_rate import economy_rate_per_bowler
from task5_runs_per_over import runs_per_over
from task6_boundary_analysis import boundary_analysis

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

    # Task 4: Economy Rate
    economy_rates = economy_rate_per_bowler(bowler, batsman_runs)

    print("\n--- Best Economy Bowlers (Top 5) ---")

# Sort ascending (lower economy is better)
    economy_sorted = sorted(economy_rates, key=lambda x: x[1])

    for player, eco in economy_sorted[:5]:
        print(f"{player}: {eco}")

    #  Task 5: Runs per Over
    avg_runs = runs_per_over(overs, batsman_runs)

    print("\n--- Average Runs Per Over ---")

    for i, avg in enumerate(avg_runs):
      print(f"Over {i+1}: {avg}")

    #  Task 6: Boundary Analysis
    fours, sixes, top_team = boundary_analysis(batsman_runs, batting_team)

    print("\n--- Boundary Analysis ---")
    print(f"Total Fours: {fours}")
    print(f"Total Sixes: {sixes}")

    print("\nTeam with Most Boundaries:")
    print(f"{top_team[0]}: {top_team[1]} boundaries")


if __name__ == "__main__":
    main()