#!/usr/local/bin python3
# func.py : functions of Individual-Based Biological Model

"""
Individual-Based Biological Model for The Platform simulation.

Classes:
    UniversalFunc: Base class with common utility functions.
    ThePlatform: Main simulation class for the platform experiment.
"""

import random
from statistics import mean
import matplotlib.pyplot as plt
import time


class UniversalFunc:
    """Base class with common utility functions."""

    @staticmethod
    def get_parameter_from_list(items, index):
        """Extract a single element from a list by index.
        
        Args:
            items: List to extract from.
            index: Index of the element to extract.
            
        Returns:
            The element at the specified index.
        """
        return items[index]

    @staticmethod
    def plot_histogram(data, x_limit=(0, 1)):
        """Plot histogram of data.
        
        Args:
            data: List of numbers to plot.
            x_limit: Tuple of (min, max) for x-axis limits.
        """
        plt.xlim(x_limit[0], x_limit[1]) 
        plt.hist(data)
        plt.show()

    @staticmethod
    def plot_scatter(data):
        """Plot scatter plot of data.
        
        Args:
            data: List of numbers to plot.
        """
        plt.plot(data, "bo")
        plt.show()

    @staticmethod
    def calculate_mean(data):
        """Calculate mean of a list.
        
        Args:
            data: List of numbers.
            
        Returns:
            Mean value of the list.
        """
        return mean(data)

    @staticmethod
    def calculate_mean_and_append(data):
        """Calculate mean of data and return as a list.
        
        Args:
            data: List of numbers.
            
        Returns:
            List containing the mean value.
        """
        return [UniversalFunc.calculate_mean(data)]

    @staticmethod
    def start_timer():
        """Start a timer.
        
        Returns:
            Start time timestamp.
        """
        return time.time()

    @staticmethod
    def end_timer(start_time):
        """End timer and print elapsed time in days.
        
        Args:
            start_time: Start time timestamp.
        """
        elapsed_time = time.time() - start_time
        days = elapsed_time / 3600 / 24
        print(f"Elapsed time: {days:.6f} days")


class ThePlatform(UniversalFunc):
    """Individual-Based Biological Model for The Platform simulation."""

    @staticmethod
    def create_inhabitant():
        """Create a new inhabitant with random food requirements.
        
        Returns:
            List containing [food_require, food_greedy, alive_flag, food_consumed].
        """
        food_require = random.random()
        food_greedy = random.uniform(food_require, 1)
        alive_flag = True
        food_consumed = 0
        return [food_require, food_greedy, alive_flag, food_consumed]

    def create_hole(self, hole_depth):
        """Create the experimental building with inhabitants.
        
        Args:
            hole_depth: Number of floors in the hole.
            
        Returns:
            List of inhabitants, each with food requirements.
        """
        return [self.create_inhabitant() for _ in range(hole_depth)]

    def extract_requirements(self, hole):
        """Extract food requirements from all inhabitants.
        
        Args:
            hole: List of inhabitants.
            
        Returns:
            Tuple of (required_food_list, greedy_food_list).
        """
        required_list = [inhabitant[0] for inhabitant in hole]
        greedy_list = [inhabitant[1] for inhabitant in hole]
        return required_list, greedy_list

    def distribute_food(self, hole, food_amount):
        """Distribute food among inhabitants, prioritizing survival.
        
        Tracks actual food consumed for each inhabitant to calculate selfishness score.
        
        Args:
            hole: List of inhabitants [food_require, food_greedy, alive_flag, food_consumed].
            food_amount: Total food to distribute.
            
        Returns:
            Modified hole with updated inhabitant states and food_consumed values.
        """
        remaining_food = food_amount

        for inhabitant in hole:
            food_required, food_greedy, alive_flag = inhabitant[0], inhabitant[1], inhabitant[2]
            food_consumed = 0
            
            if food_greedy <= remaining_food:
                food_consumed = food_greedy
                remaining_food -= food_greedy
            elif food_required <= remaining_food:
                food_consumed = food_required
                remaining_food -= food_required
            else:
                remaining_food = 0
                alive_flag = 0  # Mark inhabitant as dead
            
            # Update inhabitant data: [food_require, food_greedy, alive_flag, food_consumed]
            inhabitant[2] = alive_flag
            if len(inhabitant) < 4:
                inhabitant.append(food_consumed)
            else:
                inhabitant[3] = food_consumed
            
            remaining_food = max(0, remaining_food)
        
        return hole

    def replace_dead_inhabitants(self, hole):
        """Replace dead inhabitants with new ones.
        
        Args:
            hole: List of inhabitants.
            
        Returns:
            Updated hole with dead inhabitants replaced.
        """
        for i, inhabitant in enumerate(hole):
            if inhabitant[2] == 0:  # Dead
                hole[i] = self.create_inhabitant()

        return hole

    def calculate_humanity_levels(self, hole):
        """Calculate humanity level for each inhabitant.
        
        Humanity level = food_greedy - food_required (measure of satisfaction capacity).
        
        Args:
            hole: List of inhabitants.
            
        Returns:
            List of humanity levels.
        """
        return [inhabitant[1] - inhabitant[0] for inhabitant in hole]

    @staticmethod
    def shuffle_inhabitants(inhabitants):
        """Shuffle the order of inhabitants (simulate randomness in each round).
        
        Args:
            inhabitants: List of inhabitants.
            
        Returns:
            Shuffled list of inhabitants.
        """
        random.shuffle(inhabitants)
        return inhabitants

    @staticmethod
    def calculate_selfishness_score(food_consumed, food_required, food_greedy):
        """Calculate selfishness score based on actual consumption.
        
        Selfishness score = (food_consumed - food_required) / (food_greedy - food_required)
        - 0 = restrained (high humanity)
        - 1 = selfish (low humanity)
        
        Args:
            food_consumed: Actual amount of food consumed.
            food_required: Minimum required amount.
            food_greedy: Amount needed to be fully satisfied.
            
        Returns:
            Selfishness score in range [0, 1]. Returns 0 if denominator is 0.
        """
        denominator = food_greedy - food_required
        if denominator <= 0:
            return 0
        
        numerator = min(food_consumed, food_greedy) - food_required
        score = max(0, min(1, numerator / denominator))
        return score

    @staticmethod
    def calculate_altruism_score(selfishness_score):
        """Calculate altruism score as complement of selfishness.
        
        Altruism score = 1 - selfishness_score
        - High altruism (restraint) = high score
        - Low altruism (selfishness) = low score
        
        Args:
            selfishness_score: Selfishness score in range [0, 1].
            
        Returns:
            Altruism score in range [0, 1].
        """
        return 1 - selfishness_score

    def calculate_average_selfishness(self, hole):
        """Calculate average selfishness score for all inhabitants.
        
        Args:
            hole: List of inhabitants.
            
        Returns:
            Average selfishness score.
        """
        if not hole:
            return 0
        
        selfishness_scores = []
        for inhabitant in hole:
            food_required = inhabitant[0]
            food_greedy = inhabitant[1]
            food_consumed = inhabitant[3] if len(inhabitant) > 3 else 0
            
            score = self.calculate_selfishness_score(food_consumed, food_required, food_greedy)
            selfishness_scores.append(score)
        
        return self.calculate_mean(selfishness_scores) if selfishness_scores else 0

    def order_inhabitants_by_score(self, hole, score_type='selfishness', reverse=True):
        """Order inhabitants by selfishness or altruism score.
        
        Args:
            hole: List of inhabitants.
            score_type: 'selfishness' or 'altruism'.
            reverse: If True, order from highest to lowest score.
            
        Returns:
            Re-ordered hole based on the specified score type.
        """
        scores = []
        for inhabitant in hole:
            food_required = inhabitant[0]
            food_greedy = inhabitant[1]
            food_consumed = inhabitant[3] if len(inhabitant) > 3 else 0
            
            selfishness = self.calculate_selfishness_score(food_consumed, food_required, food_greedy)
            
            if score_type == 'altruism':
                score = self.calculate_altruism_score(selfishness)
            else:  # selfishness
                score = selfishness
            
            scores.append((inhabitant, score))
        
        # Sort by score
        scores.sort(key=lambda x: x[1], reverse=reverse)
        return [inhabitant for inhabitant, score in scores]

    def simulate_scenario(self, hole, food_amount, num_rounds, scenario_type='A'):
        """Simulate a scenario with specific ordering rules.
        
        Scenario A: Random order (baseline)
        Scenario B: Order by selfishness (selfish individuals get priority)
        Scenario C: Order by altruism (altruistic individuals get priority)
        
        Args:
            hole: List of inhabitants.
            food_amount: Food to distribute each round.
            num_rounds: Number of rounds to simulate.
            scenario_type: 'A', 'B', or 'C'.
            
        Returns:
            Updated hole after simulation.
            List of average selfishness scores over time.
        """
        selfishness_history = []
        
        for _ in range(num_rounds):
            # Order inhabitants based on scenario
            if scenario_type == 'B':
                hole = self.order_inhabitants_by_score(hole, score_type='selfishness', reverse=True)
            elif scenario_type == 'C':
                hole = self.order_inhabitants_by_score(hole, score_type='altruism', reverse=True)
            else:  # Scenario A - random
                hole = self.shuffle_inhabitants(hole)
            
            # Distribute food and track consumption
            hole = self.distribute_food(hole, food_amount)
            
            # Record average selfishness before replacing dead inhabitants
            avg_selfishness = self.calculate_average_selfishness(hole)
            selfishness_history.append(avg_selfishness)
            
            # Replace dead inhabitants with new ones
            hole = self.replace_dead_inhabitants(hole)
        
        return hole, selfishness_history

    def plot_scenario_comparison(self, scenarios_data, scenario_labels, title="Selfishness Evolution"):
        """Plot line graph comparing average selfishness across scenarios.
        
        Args:
            scenarios_data: Dict with scenario names as keys and list of selfishness histories as values.
            scenario_labels: Dict with scenario names as keys and display labels as values.
            title: Title for the plot.
        """
        plt.figure(figsize=(12, 6))
        
        colors = {'A': 'blue', 'B': 'red', 'C': 'green'}
        
        for scenario_name, history_list in scenarios_data.items():
            # Average the history if multiple runs exist
            avg_history = self.calculate_mean_and_append([h for run_history in history_list for h in run_history])
            label = scenario_labels.get(scenario_name, scenario_name)
            color = colors.get(scenario_name, 'black')
            
            plt.plot(range(len(avg_history[0] if isinstance(avg_history[0], list) else avg_history)), 
                     avg_history[0] if isinstance(avg_history[0], list) else avg_history,
                     label=label, color=color, linewidth=2, marker='o', markersize=3)
        
        plt.xlabel('Generation')
        plt.ylabel('Average Selfishness Score')
        plt.title(title)
        plt.legend()
        plt.grid(True, alpha=0.3)
        plt.tight_layout()
        plt.show()

    def plot_distribution_subplots(self, hole, scenario_labels, num_scenarios=3):
        """Plot histograms of selfishness distribution for each scenario.
        
        Args:
            hole: Final state of inhabitants from each scenario.
            scenario_labels: Labels for each scenario.
            num_scenarios: Number of scenarios.
        """
        fig, axes = plt.subplots(1, num_scenarios, figsize=(15, 4))
        
        colors = ['blue', 'red', 'green']
        
        for idx, (scenario_name, inhabitants) in enumerate(hole.items()):
            selfishness_scores = []
            for inhabitant in inhabitants:
                food_required = inhabitant[0]
                food_greedy = inhabitant[1]
                food_consumed = inhabitant[3] if len(inhabitant) > 3 else 0
                
                score = self.calculate_selfishness_score(food_consumed, food_required, food_greedy)
                selfishness_scores.append(score)
            
            axes[idx].hist(selfishness_scores, bins=20, color=colors[idx], alpha=0.7, edgecolor='black')
            axes[idx].set_title(scenario_labels.get(scenario_name, scenario_name))
            axes[idx].set_xlabel('Selfishness Score')
            axes[idx].set_ylabel('Frequency')
            axes[idx].set_xlim(0, 1)
        
        plt.tight_layout()
        plt.show()