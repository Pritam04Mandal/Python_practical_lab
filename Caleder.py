months={1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
fdoy={2001:1,2002:2,2003:3,2004:4,2005:6,2006:0,2007:1,2008:2,2009:4,2010:5,2011:6,2012:0,2013:2,2014:3,2015:4,20162017:0,2018:1,2019:2,2020:3,2021:5,2022:6,2023:0,2024:1,2025:3,2026:4,2027:5,2028:6,2029:1,2030:2,2031:3}
days=["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
print("From year 2001 to 2031 .....")
date=int(input("Enter the date: "))
month=int(input("Enter the month: "))
year=int(input("Enter the year"))
idx=list(months.keys())
# idx1=list(days.keys())
total_days=0
if(year%4==0):
    for i in range(12):
        if(month!=idx[i]):
            date+=months[idx[i]]
            if(idx[i]==2):
                date=date+1
            
            
        else:
            break

else:
    for i in range(12):
        if(month!=idx[i]):
            date+=months[idx[i]]
        else:
            break
print(date)  
date=(date%7)
print(date)
print(fdoy[year])
op=fdoy[year]+date-1
print(days[op])


