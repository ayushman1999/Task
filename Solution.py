from datetime import datetime
import calendar

def solution(d):
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
        
    return days_dict
    

# input
d = {'2020-01-01':4,'2020-01-02':4,'2020-01-03':6,'2020-01-04':8,'2020-01-05':2,
     '2020-01-06':-6,'2020-01-07':2,'2020-01-01':-2 }

output = solution(d)

# print output
print(output)


# Unit Test 1
t1 = {'2020-01-01':1,'2020-01-08':4,'2020-01-04':3,'2020-01-05':2,
     '2020-01-05':-6,'2020-01-07':2,'2020-01-01':-2 }
expected1 = {'Wednesday': -2, 'day': 2, 'Saturday': 3, 'Sunday': -6, 'Tuesday': 2, 'Monday': -4, 'Thursday': -4, 'Friday': 1}

o1 = solution(t1)

if expected1 == o1:
    print("!!!Test Case 1 Passed Successfully!!!")
else:
    print("!!!Test Case 1 Failed!!!")
    
# Unit Test 2
t2 = {'2020-01-01':10,'2020-01-02':4,'2020-01-05':2,
     '2020-01-06':-6,'2020-01-08':-2,'2020-01-04':6 }
expected2 = {'Wednesday': 10, 'Thursday': 4, 'Sunday': 2, 'Monday': -6, 'day': 8, 'Saturday': 6, 'Tuesday': 4, 'Friday': 16}

o2 = solution(t2)

if expected2 == o2:
    print("!!!Test Case 2 Passed Successfully!!!")
else:
    print("!!!Test Case 2 Failed!!!")
    
# Unit Test 3
t3 = {'2020-01-01':8,'2020-01-02':4,'2020-01-03':10,'2020-01-05':2,
     '2020-01-06':-6,'2020-01-07':2,'2020-01-01':-1 }
expected3 = {'Wednesday': -1, 'Thursday': 4, 'Friday': 10, 'Sunday': 2, 'Monday': -6, 'Tuesday': 2, 'Saturday': 12}

o3 = solution(t3)

if expected3 == o3:
    print("!!!Test Case 3 Passed Successfully!!!")
else:
    print("!!!Test Case 3 Failed!!!")

'''
OUTPUT:
{'Wednesday': -2, 'Thursday': 4, 'Friday': 6, 'Saturday': 8, 'Sunday': 2, 'Monday': -6, 'Tuesday': 2}
!!!Test Case 1 Passed Successfully!!!
!!!Test Case 2 Passed Successfully!!!
!!!Test Case 3 Passed Successfully!!!
'''
