User = input("Please provide a sentence : ")
Words = User.split()
New = [len(x) for x in Words]
S = dict(zip(Words,New))
print(S)
    
