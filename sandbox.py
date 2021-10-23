l =[6,3,6,5,4,3,2]
x = sorted(l, reverse=True)
z= max(x)
num = [i for i in x if i !=z]
print(max(num))

