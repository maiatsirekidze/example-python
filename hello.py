def process_rotate(a , b):
    arr=list(range(1,n+1))
    if k % 2==0:
        return arr
    else:
        arr.reverse()
        return arr 
    
n,k= map(int, input().split())
print(process_rotate(n,k))
N,K=map(int,input().split())
arr=list(map(int,input().split()))
arr.sort()
print(arr[k-1])