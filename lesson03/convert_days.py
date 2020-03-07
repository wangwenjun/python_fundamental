DAYS_PER_YEAR=365
DAYS_PER_WEEK=7
days = input("Please give me the days:")
days = int(days)
years = days//DAYS_PER_YEAR
weeks = (days%DAYS_PER_YEAR)//DAYS_PER_WEEK
remaining_days = days-((years*DAYS_PER_YEAR)+(weeks*DAYS_PER_WEEK))

print("Years:",years)
print("Weeks:",weeks)
print("Days:",remaining_days)
