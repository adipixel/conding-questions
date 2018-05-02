def main():
    def rps(n):
        if data[n] == data[n+1]:
            print("DRAW")
            return 'D'
        elif data[n:n+2] == "RS":
            print("A WINS")
            return 'A'
        elif data[n:n+2] == "SP":
            print("A WINS")
            return 'A'
        elif data[n:n+2] == "PR":
            print("A WINS")
            return 'A'
        elif data[n:n+2] == "SR":
            print("B WINS")
            return 'B'
        elif data[n:n+2] == "PS":
            print("B WINS")
            return 'B'
        elif data[n:n+2] == "RP":
            print("B WINS")
            return 'B'

    
    
    num = int(input())
    data = input()
    pointer=0
    score = dict()
    score['A'] = 0
    score['B'] = 0
    score['D'] = 0

    while pointer<len(data):
        res = rps(pointer)
        score[res] += 1
        pointer += 2
      
    if score['B'] < score['A']:
        print("A WINS TOURNAMENT")
    elif score['B'] > score['A']:
        print("B WINS TOURNAMENT")
    else:
        print("DRAW")

    

main()
