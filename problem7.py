list = input("Please enter a list : ")
List = list.split()
try:
    for i in List:
            New = int(i)
    print("True")
except:
    print("False")
