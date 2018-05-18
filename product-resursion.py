def prod(A):
    if A==[]:
        return 1
    else:
        x=A.pop()
        return x*prod(A)

A=[2,3,5,7,9]
print(prod(A))
