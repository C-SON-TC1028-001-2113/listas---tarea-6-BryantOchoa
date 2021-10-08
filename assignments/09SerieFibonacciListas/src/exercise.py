def main():
    x = -1
    y = 0
    a = 1
    b = 1
    serie = []
    while x <= -1:
        x = int(input())
    if x == 0:
        print(serie)
    elif x==1:
        serie.append(0)
        print(serie)
    elif x==2:
        serie.append(0)
        serie.append(1)
        print(serie)
    else :
        serie.append(0)
        serie.append(1)
        serie.append(1)
        for i in range(x-3) :
            y = a + b
            b = a
            a = y
            serie.append(y)
        print(serie)
if __name__=='__main__':
    main()
