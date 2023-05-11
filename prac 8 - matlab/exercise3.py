week_days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
week_days1 = week_days[1:] + week_days[:1]
print(week_days)
print (week_days1)

months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
days_in_each_month = [31,28,31,30,31,30,31,31,30,31,30,31]
months

months_and_days = list(zip(months, days_in_each_month))

print(months_and_days[4])

dict_months_and_days = dict(months_and_days)

print(dict_months_and_days['May'])
