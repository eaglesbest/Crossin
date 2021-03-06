#!/usr/bin/env python2.7
# 另一种实现方式
import pandas

def uniqueDay(start,end):
    result=set()
    dates = pandas.date_range(start, end)
    dates = (dt.strftime('%Y%m%d') for dt in dates)
    [result.add(dt) for dt in dates if len(set(dt))==8]
    if result:
        print(max(result))

uniqueDay('19700101','20180101')


from itertools import permutations
num_list = ['0','1','2','3','4','5','6','7','8','9']
month_1 = ['01','03','05','07','08','10','12']
month_2 = ['04','06','09','11']
month_3 = ['02']
count = 0
result_list = []
 
for bir in permutations(num_list,8):
    num = ''.join(bir)
    year = num[0:4]
    month = num[4:6]
    day = num[6:8]
    if int(year) > 2017:
        break
    else:
        if month in month_1:
            if int(day) > 32:
                continue
        elif month in month_2:
            if int(day) > 31:
                continue 
        elif month in month_3:
            if ((int(year) % 4 == 0) & (int(year) % 100 != 0)) | (int(year) % 400 == 0):
                if int(day) > 30:
                    continue
            else:
                if int(day) > 29:
                    continue 
        else:
            continue
        result_list.append(num)
print len(result_list)
print result_list[-1]
