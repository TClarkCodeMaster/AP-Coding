from helperFunctions import weeklyPlayerStats

# Copy the new weeklyPlayerStats() function into your helperFunction.py file.

# Create a new python document caled  exercise3.py . Using th individual player helper function, 
# answer the following questions:

# NOTE = you will need to pass the position, year and week in as an agrument
# position example:
  
# - quarterback = 'QB'
# - runnerback = 'RB'
# - wide receiver = 'WR'

exampleData = weeklyPlayerStats(2024,'QB', 1) 
print(exampleData)
# NOTE = Please write your responses in string format 
'Please write your responses in string format'

# 1. Who are the top 5 quarterbacks by passing yards in 2024? 
# What was their average completion percentage (cmp_pct)?

# T. Tagovailo, 338 yards, 62.1% cmp_pct
# M. Stafford, 317 yards, 69.3% cmp_pct
# P. Mahomes, 291 yards, 71.4% cmp_pct
# B. Maayfield, 289 yards, 80% cmp_pct
# J. Hurts, 278 yards, 58.8% cmp_pct

# 2. What does a high cmp_pct (completion percentage) tell you about a
# quarterback’s style of play?

# A high completion percentage indicates that a quarterback is accurate and efficient in their passing.

# 3. Which RB had the highest rushing yards in 2024? 
# Which RB had the best yards per carry (rush_ypc) in 2024? Are these the same or different individuals?

# L. Jackson had the highest rushing yards with 122 yards.

# 4. If a RB has high rushing yard (rush_yards), but low rushing yards per carry (rush_ypc),
#  what could that mean?

# It could mean that the RB gets a lot of carries but doesnt gain a lot of yards each time they run the ball.