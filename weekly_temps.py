weekly_temps = [
    [12, 15, 18, 20, 17], 
    [22, 25, 20, 19, 21],
    [16, 19, 21, 23, 18]
]

min_temp = float("inf")
max_temp = 0
for week_num, week in enumerate(weekly_temps):
    average = sum(week) / len(week)
    print(f"The average temperature of week {week_num + 1 } is {average}.")
    for daily_temp in week:
        if daily_temp > max_temp:
            max_temp = daily_temp

        elif daily_temp < min_temp:
            min_temp = daily_temp 
print(f"Highest temperature: {max_temp}")
print(f"Minimum temperature: {min_temp}")

