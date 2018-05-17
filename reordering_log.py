import heapq

data = ["[a1 9 2 3 1]",
"[g1 act car]",
"[zo4 4 7]",
"[ab1 off key dog]",
"[a8 act zoo]"]



def reorderElements(logFileSize, logLines):
  
  strdata = []
  intdata = []

  for line in logLines:
    for i in range(len(line)):
      if line[i] == " ":
        if ord(line[i+1]) < 58:
          intdata.append(line)
          break
        else:
          heapq.heappush(strdata, line[i+1:]+"-"+line[:i+1])
          break
  res = []
  
  while strdata:
    temp = (heapq.heappop(strdata))
    word = ""
    for i in range(len(temp)):
      if temp[i] == "-":
        res.append(temp[i+1:]+word)
        break
      else: 
        word += temp[i]
  
  for x in intdata:
    res.append(x)
    
    
  return res
  
  
print(reorderElements(4,data))
