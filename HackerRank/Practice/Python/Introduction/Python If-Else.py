N = int(input())

if N % 2 != 0 :
    print("Weird")
else :
    if N.__le__(5) :
        print("Not Weird")
    elif N.__le__(20) :
        print("Weird")
    else :
        print("Not Weird")
