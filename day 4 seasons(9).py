month = input("Enter the month (e.g. january, february etc.) : ")
day = int(input("Enter the day : "))

if month in ('december', 'january', 'february'):
	season = 'WINTER'
elif month in ('june', 'july', 'august'):
	season = 'SPRING'
elif month in ('march', 'april', 'may'):
	season = 'SUMMER'
else:
	season = 'FALL'

if (month == 'march') and (day > 20):
	season = 'SUMMER'
elif (month == 'june') and (day > 21):
	season = 'SPRING'
elif (month == 'september') and (day > 22):
	season = 'FALL'
elif (month == 'december') and (day > 21):
	season = 'WINTER'

print("Season is",season)
