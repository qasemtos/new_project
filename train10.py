name='hebron'
for i in name:
    print(i)

def maximum(*args):
    mx = args[0]
    for i in args:

        if i>mx:
            mx=i
        return mx

print(maximum(1,55,44,34))
def power(x,n):
    if n==0:
        return 1
    else:
        return x*power(x,n-1)
print(power(4,2))
def sumelements(ar):
    if len(ar)==0:
        return 0
    else:
        return ar[0]+sumelements(ar[0:])
def hanoi(n,s,i,d):
    if n>0:
        hanoi(n-1,s,d,i)
        print('move'+s+'to'+d)
        hanoi(n-1,i,s,d)











