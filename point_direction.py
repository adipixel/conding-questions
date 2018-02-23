def directions(x1,y1, x2, y2):
    if x1 == x2 and y1 == y2:
        return "SAME"
    if x2 > x1: # east
        if y1 == y2:
            return "E"
        elif y2 > y1:
            return "NE"
        else:
            return "SE"
    elif x2 < x1: # west        
        if y1 == y2:
            return "W"
        elif y2 > y1:
            return "NW"
        else:
            return "SW"
    elif y2 > y1: # north
        if x1 == x2:
            return "N"
        elif x2 > x1:
            return "NE"
        else:
            return "NW"
    else: # South        
        if x1 == x2:
            return "S"
        elif x2 > x1:
            return "SW"
        else:
            return "SE"
        
        
def directions1(x1,y1, x2, y2):        
    E, W, N, S = "", "", "", ""
    res = ""
    if x1 == x2 and y1 == y2:
        return "SAME"

    if y2 > y1:
        res += "N"
    elif y2 < y1:
        res += "S"
    
    if x1 != x2:
        if y1 == y2:
            if x2 > x1:
                res += "E"
            else:
                res += "W"
        else:
            if x2 > x1:
                res += "E"
            else:
                res += "W"
    return res
        
    
def directions3(x1,y1, x2, y2):        
    E, W, N, S = "", "", "", ""
    res = ""
    if x1 == x2 and y1 == y2:
        return "SAME"

    if y2 > y1:
        res += "N"
    elif y2 < y1:
        res += "S"
    
    if x1 != x2:
        if y1 == y2:
            res = ""

        if x2 > x1:
            res += "E"
        else:
                res += "W"
    return res
        
    
    
print directions(150, 180, 160, 180)
print directions1(150, 180, 160, 180)
print directions3(150, 180, 160, 180)
