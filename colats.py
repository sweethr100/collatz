def colats(n):
    x = n
    while x != 1:
        if x%2 == 0:
            x= x/2
        else:
            x = 3*x + 1
    return n

if __name__ == "__main__":
    n = 1
    while True:
        print(colats(n))
        n+=1
        if n == 2**68:
            print("2^68 달성")