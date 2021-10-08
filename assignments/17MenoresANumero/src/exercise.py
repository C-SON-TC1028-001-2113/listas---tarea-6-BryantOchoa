def minus (x) :
    variable = []
    for i in range(len(x) ):
        for j in range(len(x[i])) :
            if x[i][j]<10 :
                variable.append(x[i][j])
    return(variable)           
def main():
    listA = []
    row = int(input())
    column = int(input())
    for i in range (row) :
        listA.append([])
        for j in range (column) :
            n = int(input())
            listA[i].append(n)
    ans = minus (listA)
    print(ans)
if __name__=='__main__':
    main()
