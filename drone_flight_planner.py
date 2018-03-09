def calc_drone_min_energy(route):
  extra = 0
  curEnergy = 0
  needed = 0
  for i in range(0, len(route)-1):
    if route[i][2] < route[i+1][2]: # ascending
      needed = curEnergy - (route[i+1][2] - route[i][2])
      if needed < 0:
        extra += abs(needed)
        curEnergy = 0
      else:
        curEnergy = needed
        
    else: #descending
      curEnergy += route[i][2] - route[i+1][2]

  return extra
      
