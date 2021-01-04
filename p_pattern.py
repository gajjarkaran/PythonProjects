for _ in range(int(input())):
    n=int(input())
    m=[]
    for i in range(n):
        m.append([0 for i in range(n)])
    #print(m)
    k1=n*n
    k=1
    for i in range(n):
        t=i
        #print(type(m)
        p=n-i-1
        for j in range(0,i+1):
            #print(type(m))
            #print(m,j,t)
            m[j][t]=k
            k+=1
            t-=1
            if(k1>(n*n)-(n*n-n)//2):
                m[n-j-1][p]=k1
                p+=1
                k1-=1
    for i in range(n):
        print(*m[i])