List = ['~', ':', "'", '+', '[', '\\', '@', '^', '{', '%', '(', '-', '"', '*', '|', ',', '&', '<', '`', '}', '.', '_', '=', ']', '!', '>', ';', '?', '#', '$', ')', '/']
x = input("Please enter a string : ")
d = {}
for i in x:
    if i in List:
        d[i] = d.get(i,0)+1
print(d) 
