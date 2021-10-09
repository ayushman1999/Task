from datetime import datetime
import calendar

# input
d = {'2020-01-01':4,'2020-01-02':4,'2020-01-03':6,'2020-01-05':2,
     '2020-01-06':-6,'2020-01-07':2,'2020-01-01':-2 }

# empty dict to store days and their values
days_dict = {}

# iterate over input 
for key in d:
    k1 = key
    v1 = d[key]
    s1 = datetime.fromisoformat(k1)
    day = calendar.day_name[s1.weekday()]
    if day in days_dict.keys():
        val = days_dict[day]
        sum = val + v1
        days_dict.update(day = sum )
    else:
        days_dict[day] = v1

# days list
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Wednesday", "Friday", "Saturday", "Sunday"];

# handle not inputed days
for i in range(0, len(days)):
    if days[i] not in days_dict.keys():
        pre = days[i-1]
        nex = days[i+1]
        val = days_dict[pre] + days_dict[nex]
        days_dict[days[i]] = val
        
# print output
print(days_dict)
