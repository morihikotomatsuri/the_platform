#!/usr/local/bin python3
# main.py: run Individual-Based Biological Model with scenario comparison

"""
Humanity-Evolution Experiment with Scenario Comparison
    Three scenarios to explore evolution of selfishness/altruism

Scenarios:
    A: Baseline (random order)
    B: Selfish priority (high selfishness individuals eat first)
    C: Altruistic priority (low selfishness/high altruism individuals eat first)
"""

import setting
from func import ThePlatform
import matplotlib.pyplot as plt

# Initialize simulation
platform = ThePlatform()
start_time = platform.start_timer()

# Configuration
floor_num = setting.floors
experimental_food_range = setting.experimental_food_range
number_of_rounds = setting.number_of_rounds

# Store results for each scenario
results = {
    'A': {'avg_selfishness': [], 'final_populations': []},
    'B': {'avg_selfishness': [], 'final_populations': []},
    'C': {'avg_selfishness': [], 'final_populations': []}
}

scenario_labels = {
    'A': 'Scenario A: Random (Baseline)',
    'B': 'Scenario B: Selfish Priority',
    'C': 'Scenario C: Altruistic Priority'
}

# Run all scenarios for each food amount
print("=" * 70)
print("Starting multi-scenario simulation...")
print("=" * 70)

for food_amount in experimental_food_range:
    print(f"\n--- Food Amount: {food_amount} ---")
    
    for scenario_type in ['A', 'B', 'C']:
        print(f"\n  Running Scenario {scenario_type}...")
        
        # Create initial population
        hole = platform.create_hole(floor_num)
        
        # Simulate the scenario
        final_hole, selfishness_history = platform.simulate_scenario(
            hole, food_amount, number_of_rounds, scenario_type
        )
        
        # Store results
        results[scenario_type]['avg_selfishness'].append(selfishness_history)
        results[scenario_type]['final_populations'].append(final_hole)
        
        # Calculate final average selfishness
        final_avg_selfishness = platform.calculate_average_selfishness(final_hole)
        print(f"    Final avg selfishness: {final_avg_selfishness:.4f}")
        print(f"    Final avg humanity: {1 - final_avg_selfishness:.4f}")

# Prepare data for visualization
print("\n" + "=" * 70)
print("Generating visualizations...")
print("=" * 70)

# Convert histories for comparison (average across food amounts)
scenarios_data = {}
for scenario in ['A', 'B', 'C']:
    # Flatten all histories and calculate average trajectory
    all_histories = results[scenario]['avg_selfishness']
    if all_histories:
        avg_trajectory = []
        max_len = max(len(h) for h in all_histories)
        for step in range(max_len):
            values = [h[step] for h in all_histories if step < len(h)]
            if values:
                avg_trajectory.append(platform.calculate_mean(values))
        scenarios_data[scenario] = [avg_trajectory]

# Plot 1: Line graph of average selfishness evolution
print("\nPlotting scenario comparison (line graph)...")

# Calculate average trajectory for each scenario
fig, ax = plt.subplots(figsize=(12, 6))
colors = {'A': 'blue', 'B': 'red', 'C': 'green'}

for scenario in ['A', 'B', 'C']:
    avg_trajectory = scenarios_data[scenario][0]
    color = colors[scenario]
    label = scenario_labels[scenario]
    ax.plot(range(len(avg_trajectory)), avg_trajectory, 
            label=label, color=color, linewidth=2, marker='o', markersize=4)

ax.set_xlabel('Generation', fontsize=12)
ax.set_ylabel('Average Selfishness Score', fontsize=12)
ax.set_title('Evolution of Selfishness Across Scenarios', fontsize=14)
ax.legend(fontsize=11)
ax.grid(True, alpha=0.3)
ax.set_ylim(0, 1)
plt.tight_layout()
plt.show()

# Plot 2: Distribution histograms for final state
print("Plotting final distribution (histograms)...")

import matplotlib.pyplot as plt
fig, axes = plt.subplots(1, 3, figsize=(15, 4))
colors_hist = ['blue', 'red', 'green']
scenario_list = ['A', 'B', 'C']

for idx, scenario in enumerate(scenario_list):
    final_populations = results[scenario]['final_populations']
    
    # Collect selfishness scores from all final populations
    all_scores = []
    for hole in final_populations:
        for inhabitant in hole:
            if len(inhabitant) > 3:
                score = platform.calculate_selfishness_score(
                    inhabitant[3], inhabitant[0], inhabitant[1]
                )
                all_scores.append(score)
    
    axes[idx].hist(all_scores, bins=30, color=colors_hist[idx], alpha=0.7, edgecolor='black')
    axes[idx].set_title(scenario_labels[scenario], fontsize=11)
    axes[idx].set_xlabel('Selfishness Score', fontsize=10)
    axes[idx].set_ylabel('Frequency', fontsize=10)
    axes[idx].set_xlim(0, 1)

plt.tight_layout()
plt.show()

# Print summary statistics
print("\n" + "=" * 70)
print("SUMMARY STATISTICS")
print("=" * 70)

for scenario in ['A', 'B', 'C']:
    all_scores = []
    for hole in results[scenario]['final_populations']:
        for inhabitant in hole:
            if len(inhabitant) > 3:
                score = platform.calculate_selfishness_score(
                    inhabitant[3], inhabitant[0], inhabitant[1]
                )
                all_scores.append(score)
    
    if all_scores:
        avg_score = platform.calculate_mean(all_scores)
        print(f"{scenario}: Avg selfishness = {avg_score:.4f}, Avg humanity = {1 - avg_score:.4f}")

platform.end_timer(start_time)
print("\n" + "=" * 70)
print("Simulation completed!")
print("=" * 70)