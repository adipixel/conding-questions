import datetime

def solution(s):
  timeMap = dict()
  for x in s:
    if x != ':':
      if x in timeMap:
        timeMap[x] += 1
      else:
        timeMap[x] = 1
      
  times=s.split(':')
  t = datetime.datetime.combine(datetime.date.today(), datetime.time(int(times[0]), int(times[1])))
  
  time = t + datetime.timedelta(minutes=1)  

  while(t != time):  
    tstr = str(time.time())[:5]
    timeMap1 = dict()
    for x in tstr:
      if x != ':':
        if x in timeMap1:
          timeMap1[x] += 1
        else:
          timeMap1[x] = 1
    if timeMap1 == timeMap:
      return str(time.time())[:5]
    
    time = time + datetime.timedelta(minutes=1)    
    if time.hour == 0 and time.minute==0:
      time.replace(day = time.day -1)
    
  return str(t.time())[:5]

def main():
  s = "12:12"
  print solution(s)
main()
