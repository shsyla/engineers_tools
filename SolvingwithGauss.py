#here you will find the code for Solving with Gauss
def gauss_solve( A, b ):
    Anzahl= len(b)
    for i in range(0,Anzahl-1):
        for z in range(i+1,Anzahl):
            factor= A[z][i]/A[i][i]
            for j in range(i,Anzahl):
                A[z][j]=A[z][j]-A[i][j]*factor  
            b[z]= b[z]-factor*b[i]                     
    x= bwd_subs(A,b)    
    return x

def bwd_subs( U, y ):
    n=len(y)
    x=np.zeros(n)
    #ab null wird angefangen zu zaehlen
    x[n-1]=y[n-1]/U[n-1][n-1]
    for i in range(len(y)-2,-1,-1):
        sum=0
        for j in range(i+1,n):
            sum+=U[i][j]*x[j]
        x[i]= (y[i]-sum)/U[i][i]    
    return x
def fwd_subs( L, b ):
    y=np.zeros(len(b))
    y[0]=b[0]/L[0][0]
    for i in range(1,len(b)):
        sum=0
        for j in range(0,i):
            sum+=L[i][j]*y[j]
        y[i]= (b[i]-sum)/L[i][i]  
    return y