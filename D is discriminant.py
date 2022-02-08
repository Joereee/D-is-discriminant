a=int(input())
b=int(input())
c=int(input())
D=int()
D=(b**2)-4*(a)*(c)
if D>=0:
    x1=(-(b)+(D**0.5))/(2*(a))
    x2=(-(b)-(D**0.5))/(2*(a))
    print(x1,x2)
else:
    print("no roots")
