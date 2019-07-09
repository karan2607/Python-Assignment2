value = input("Please proide a list : ")
List = value.split()
numbers = [ int(x) for x in List ]
new=[]
for i in numbers:
    if i%3==0:
        new.append(i)
print(new)
