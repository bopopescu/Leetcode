def dungeon(m,n):
    result = [[0]*n for i in range(m)]
    for i in range(m):
        result[i][0]=1
    for j in range(n):
        result[0][j]=1

    for i in range(1,m):
        for j in range(1,n):
            result[i][j]=result[i-1][j]+result[i][j-1]

    return result[m-1][n-1]

print dungeon(3,4)