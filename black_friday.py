#!/usr/bin/enc python
#coding:utf-8

import datetime

def cal_black_friday(year):
    date_list = []
    for month in range(1,13):
        if datetime.datetime.weekday(datetime.date(int(year),month,13)) == 4:
            date_list.append("%s-%s-%s" % (year,month,13))
    return date_list

if __name__ == "__main__":
    while True:
        year = raw_input("查询年份:")
        if int(year) < 2017:
            print "输入的年份需大于2017，请重新输入"
            continue
        print "符合日期："
        for black_date in cal_black_friday(year):
            print black_date
        break
