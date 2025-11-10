from helperFunctions import weeklyPlayerStats, plot_weekly_player_stats, plot_player_stat
import matplotlib.pyplot as plt

stats = weeklyPlayerStats(2024, "QB")
plot_player_stat(stats, stat="passing_yards", top_n=20, title= "QB Passing Yards (2024 Season)", save_path="qb_passing_yards_2024.png" )
