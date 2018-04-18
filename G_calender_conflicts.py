class Appt
  start, end
  ...
  bool has_conflict = False

def detect_conflicts(appts):
  for x in range(len(appts)):
    curStart = appts[x].start
    curEnd = appts[x].end	
  for i in range(0, x):
    if not ((curStart < appts[i].start and curStart < appts[i].end and curEnd < appts[i].start and curEnd < appts[i].end) or (curStart >appts[i].start and curStart > appts[i].end and curEnd > appts[i].start and curEnd > appts[i].end)):
      appts[x].has_conflict  = True
	    appts[i].has_conflict  = True
  return appts
