def solution(n):
    if n%2 == 0:
        return (n/2+1)*n/2
    else:
        return ((n-1)/2+1)*(n-1)/2